from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',views.home,name="home"),
    

    path('',views.ElementView.as_view(),name="home"),
    path('element-detail/<int:pk>',views.ElementDetail.as_view(),name='element-detail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
]
