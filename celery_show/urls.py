from django.urls import path
from celery_show import views

urlpatterns = [
    # path('index/', views.index),
    path('contact/', views.ContactFormView.as_view(), name="contact_form"),
]
