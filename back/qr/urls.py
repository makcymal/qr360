from django.urls import path

from . import views

urlpatterns = [
    path('', views.QRList.as_view()),
    path('<int:qr_id>/', views.QRDetail.as_view()),
    path('demo/', views.DemoQRManage.as_view()),
    path('demo/<int:qr_id>/', views.DemoQRManageDetail.as_view()),
]
