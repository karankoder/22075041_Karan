from django.contrib import admin
from django.urls import path,include
from url_shortener_app import views

urlpatterns = [
    path('', views.url_shortener_view,name="homepage"),
    path('<slug:short_url>', views.url_redirect_view),
    path('display_urls/', views.display_urls),
]