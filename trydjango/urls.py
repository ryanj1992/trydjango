"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from pages.views import home_view, contact_view, about_view
from products.views import product_detail_view, product_create_view
from flights.views import search_flights_view, flights_results_view, add_flight
from hotels.views import search_hotels_view
from trips.views import TripsDashboard, add_trip, add_image_url, TripDetailView
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('about/', about_view),
    path('admin/', admin.site.urls),
    # Login and Profile
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # Flights
    path('flights/', search_flights_view, name='flights'),
    path('result_flights/', flights_results_view, name='result_flights'),
    path('add_flight/', add_flight, name='add_flight'),
    # Hotels
    path('hotels/<str:location>', search_hotels_view, name='hotels'),
    # Trips
    path('trips/', login_required(user_views.FlightListView.as_view()), name='trips'),
    path('dashboard/', login_required(TripsDashboard.as_view()), name='dashboard'),
    path('add_trip/', add_trip, name='add_trip'),
    path('add_image_url/', add_image_url, name='add_image_url'),
    path('trip/<int:pk>/', login_required(TripDetailView.as_view()), name='trip-detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
