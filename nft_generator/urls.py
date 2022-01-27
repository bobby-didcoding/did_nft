
from django.urls import path
from . import views
 
app_name = "nft_generator"
 
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('nft-generator/', views.NFTGeneratorView.as_view(), name="nft-generator"),
    path('nfts/', views.NFTSView.as_view(), name="nfts"),
    path('nft/<slug:slug>/', views.NFTView.as_view(), name='nft'),
    ]
 
