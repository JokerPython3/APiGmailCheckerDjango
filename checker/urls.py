from django.urls import path
from . import views
urlpatterns=[
    path('check/<str:email>',views.checker,name="checker"),
]