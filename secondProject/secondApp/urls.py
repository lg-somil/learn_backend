from django.urls import path
from . import views
app_name = 'secondApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('accessRecords/', views.show_access_records, name='access_records'),
    path('fillCommentForm/', views.show_form, name='comment_form'),
    path('fillWebpageForm/', views.add_Webpage, name='add_webpage')
]