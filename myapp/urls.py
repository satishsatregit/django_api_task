from django.urls import path
from .views import GenericgetAPIView,GenericpostAPIView,GenericputAPIView,GenericdeleteAPIView

urlpatterns = [
    path('api/all_api/', GenericgetAPIView.as_view(), name='get_api'),
    path('api/all_api/', GenericpostAPIView.as_view(), name='post_api'),
    path('api/all_api/<str:table_name>/<int:id>/', GenericputAPIView.as_view(), name='put_api'),
    path('api/all_api/<str:table_name>/<int:id>/', GenericdeleteAPIView.as_view(), name='delete_api'),
]
