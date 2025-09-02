from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("museums/", views.MuseumListAPIView.as_view()),
]


router = DefaultRouter()
router.register("admin-access", views.MuseumAdminViewSet)
# router.register("city", views.MuseumByCityList, basename='city')
urlpatterns += router.urls