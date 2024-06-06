from django.urls import path
from . import views

urlpatterns = [
    path('api/companies', views.CompanyList.as_view(), name='company_list'),
    path('api/companies/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
    path('api/locations', views.LocationList.as_view(), name='location_list'),
    path('api/locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
]
