from django.urls import path
from . import views
app_name = 'secondApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('accessRecords/', views.show_access_records, name='access_records'),
    path('fillCommentForm/', views.show_form, name='comment_form'),
    path('fillWebpageForm/', views.add_Webpage, name='add_webpage'),
    path('temp_inherit/', views.temp_inherit, name='temp_inherit'),
]