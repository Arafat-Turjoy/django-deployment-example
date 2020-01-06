from django.urls import path
from . import views

app_name = 'basicapp'
urlpatterns=[
    path('relative',views.relative_url,name='relative'),
    path('other',views.others,name='other'),
]
