from django.urls import path

from . import views

# app_name = 'api'

urlpatterns = [
    path('apps/', views.AppListView.as_view(), name='apps'),
    path('apps/<int:pk>/', views.AppView.as_view(), name='app'),
    path('test/<str:api_key>/', views.AppInfoView.as_view(), name='app_info'),
    path('create-user/', views.CreateUserView.as_view(), name='create_user'),
    path('get-token/', views.GetUserTokenView.as_view(), name='get_user_token')
]
