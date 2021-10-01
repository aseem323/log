from django.urls import path
from .import views

urlpatterns = [
    path('test',views.testfn,name='test'),

]