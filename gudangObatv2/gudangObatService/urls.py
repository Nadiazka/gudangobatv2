from django.conf.urls import url, include
from gudangObatService import views
from django.views.generic import TemplateView

urlpatterns =[
 	url(r'^$', TemplateView.as_view(template_name='gudangObatService/home.html')),
	url(r'^Drugs/', views.DrugsView.as_view(), name='Drugs'),
	url(r'^Puskesmas/', views.PuskesmasView.as_view(), name='Puskesmas'),
	url(r'^DrugsQuantity/', views.DrugsQuantityView.as_view(), name='DrugsQuantity'),
]