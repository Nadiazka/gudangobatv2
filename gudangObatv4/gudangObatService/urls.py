from django.conf.urls import include
from gudangObatService import views
from django.views.generic import TemplateView
from django.urls import path

urlpatterns =[
 	path('', TemplateView.as_view(template_name='gudangObatService/home.html')),
	path('Drugs/', views.DrugsView.as_view(), name='Drugs'),
	path('Puskesmas/', views.PuskesmasView.as_view(), name='Puskesmas'),
	path('DrugsQuantity/', views.DrugsQuantityView.as_view(), name='DrugsQuantity'),
	path('Drugs/<pk>/', views.DrugsViewDetail.as_view(), name='DrugsDetail'),
	path('Puskesmas/<pk>/', views.PuskesmasViewDetail.as_view(), name='PuskesmasDetail'),
	path('DrugsQuantity/<int:pk>/', views.DrugsQuantityViewDetail.as_view(), name='DrugsQuantityDetail'),
]