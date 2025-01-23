from django.urls import path

from .views import HomePageView, AboutPageView, ProductPageView, upload_file

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("product/", ProductPageView.as_view(), name="product"),
    path("upload/", upload_file, name="upload_file"),
]
