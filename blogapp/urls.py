from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'store'

urlpatterns = [
     #API to a post comment
    path('',views.index, name='index'),
    path('<slug:slug>',views.single_post,name='single_post'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('news/',views.news, name='news'),
    path('contact/', views.contact, name='contact'),
]

                                                     