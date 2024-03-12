class PropertyStatementListAPIView(APIView):
    serializer_class = TenantSerializer

    def get(self, request, *args, **kwargs):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')
        property_id = request.query_params.get('property_id')

        if not (start_date_str and end_date_str):
            return Response({'error': 'start_date and end_date are required'}, status=status.HTTP_400_BAD_REQUEST)

        start_date, end_date = self.parse_date_range(
            start_date_str, end_date_str)

        queryset = Tenant.objects.all()

        if property_id:
            queryset = queryset.filter(property=property_id)

        response_data = []

        property_instance = None
        total_amount_paid = 0
        total_category_amounts = {
            'Rent': 0,
            'Water Bill': 0,
            'Deposit Invoices': 0,
            'Other Bills': 0,
            'Amount Due': 0
        }
        total_balance = 0

        if property_id:
            try:
                property_instance = Property.objects.get(id=property_id)
                property_data = self.get_property_data(
                    property_instance, start_date, end_date)
            except Property.DoesNotExist:
                property_data = {}

        for tenant_data in self.get_tenants_data(queryset):
            tenant_response = {
                'tenant_id': tenant_data['id'],
                'unit': tenant_data['unit'],
                'property_name': tenant_data['property'],
                'phone_number': tenant_data['phone_number'],
                'category_sums': self.calculate_category_sums(tenant_data, start_date, end_date),
                'total_amount_due': 0,
                'balance_carried_forward': 0,
                'amount_paid': 0,
                'balance': 0,
            }

            tenant_response['total_amount_due'] = tenant_response['category_sums']['Amount Due']
            tenant_response['balance_carried_forward'] = self.calculate_balance_carried_forward(
                tenant_data, start_date)
            tenant_response['amount_paid'] = self.calculate_amount_paid(
                tenant_data, start_date, end_date)
            tenant_response['balance'] = tenant_response['total_amount_due'] - \
                tenant_response['amount_paid']

            total_amount_paid += tenant_response['amount_paid']
            for category, amount in tenant_response['category_sums'].items():
                total_category_amounts[category] += amount

            total_balance += tenant_response['balance']

            response_data.append({
                'tenant_data': tenant_response,
            })

        return Response({
            'tenants': response_data,
            'property_data': property_data,  # Include property data for the entire range
            'total_amount_paid': total_amount_paid,
            'total_category_amounts': total_category_amounts,
            'total_balance': total_balance
        })

    def get_expenses(self, property_instance, start_date, end_date):
        expenses = Expense.objects.filter(
            property=property_instance,
            expense_date__range=(start_date, end_date)
        ).values('id', 'amount', 'payment_method', 'expense_category', 'expense_date', 'status', 'notes', 'file_upload', 'property', 'unit')
        total_expense_amount = expenses.aggregate(total=Sum('amount'))['total']
        return {
            'expenses': list(expenses),
            'total_expense_amount': total_expense_amount if total_expense_amount else Decimal(0)
        }
