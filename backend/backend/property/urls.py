from django.urls import path
from .views import (

    PropertyListView,
    PropertyCreateView,
    PropertyUpdateView,
    PropertyDeleteView,
    PropertyDetailView,

    UnitListCreateAPIView,
    UnitRetrieveAPIView,
    UnitUpdateAPIView,
    UnitDestroyAPIView,

    MaintenanceListCreateAPIView,
    MaintenanceRetrieveUpdateDestroyAPIView,

    PropertyOtherRecurringBillListCreateAPIView,
    PropertyOtherRecurringBillRetrieveUpdateDestroyAPIView,

    UnitOtherRecurringBillListCreateAPIView,
    UnitOtherRecurringBillRetrieveUpdateDestroyAPIView,

    UtilitiesListCreateAPIView,
    UtilitiesRetrieveUpdateDestroyAPIView,

    PropertyStatementListAPIView,
    PropertyStatementHTMLView,
    PropertyStatementPDFView
)

urlpatterns = [

    # Property URLS
    path('', PropertyListView.as_view(), name='property-list'),
    path('<int:pk>/', PropertyDetailView.as_view(),
         name='property-detail'),
    path('create/', PropertyCreateView.as_view(), name='property-create'),
    path('update/<int:pk>/',
         PropertyUpdateView.as_view(), name='property-update'),
    path('delete/<int:pk>/',
         PropertyDeleteView.as_view(), name='property-delete'),

    # Unit URLS
    path('units/', UnitListCreateAPIView.as_view(), name='unit-list-create'),
    path('units/<int:pk>/', UnitRetrieveAPIView.as_view(), name='unit-retrieve'),
    path('units/update/<int:pk>/', UnitUpdateAPIView.as_view(), name='unit-update'),
    path('units/delete/<int:pk>/', UnitDestroyAPIView.as_view(), name='unit-delete'),


    # maintenance urls
    path('maintenance/', MaintenanceListCreateAPIView.as_view(),
         name='maintenance-list-create'),
    path('maintenance/<int:pk>/',
         MaintenanceRetrieveUpdateDestroyAPIView.as_view(), name='maintenance-detail'),

    # propertyrecurringbill
    path('other-recurring-bills/', PropertyOtherRecurringBillListCreateAPIView.as_view(),
         name='other-recurring-bill-list-create'),
    path('other-recurring-bills/<int:pk>/',
         PropertyOtherRecurringBillRetrieveUpdateDestroyAPIView.as_view(), name='other-recurring-bill-detail'),


    # unit recurring bills
    path('unit-other-recurring-bills/', UnitOtherRecurringBillListCreateAPIView.as_view(),
         name='unit-other-recurring-bill-list'),
    path('unit-other-recurring-bills/<int:pk>/',
         UnitOtherRecurringBillRetrieveUpdateDestroyAPIView.as_view(), name='unit-other-recurring-bill-detail'),


    # UTILITIES URLS
    path('utilities/', UtilitiesListCreateAPIView.as_view(), name='utilities-list'),
    path('utilities/<int:pk>/',
         UtilitiesRetrieveUpdateDestroyAPIView.as_view(), name='utilities-detail'),


    path('property-statements/', PropertyStatementListAPIView.as_view(),
         name='property-statements'),
    path('property-statements/temp/', PropertyStatementHTMLView.as_view(),
         name='property_statement_pdf_download'),
    path('property-statement-pdf/', PropertyStatementPDFView.as_view(),
         name='property_statement_pdf'),
]
