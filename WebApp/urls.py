from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='Home'),
    path('search/', views.Search, name='Search'),
    path('search/submit/', views.Submit, name='Submit'),
    path('urls/', views.Urls, name='Urls'),
    path('process/', views.Process, name='Process'),
    path('details/', views.Detail, name='Details'),
    path('category/', views.categories, name='category'),
    path('category/add_category/', views.add_category, name='add category'),
    path('category/update_category/<cid>', views.update_category, name='update categoty'),
    path('category/delete_category/<cid>', views.delete_category, name='delete categoty'),
    path('phone_list/whatsapp/', views.whatsApp, name='whatsapp'),
    path('phone_number/', views.checkphonenumber, name='phone number'),
    path('phone_list/', views.phone_list, name='Phone List'),
    path('filter-whatsapp/', views.filter_whatsapp, name='filter-whatsapp'),
    path('state/', views.states, name='state'),
    path('state/add_state/', views.add_state, name='add state'),
    path('state/update_state/<sid>/', views.update_state, name='update state'),
    path('state/delete_state/<sid>/', views.delete_state, name='delete state'),
    path('city/', views.cities, name='city'),
    path('city/add_city/', views.add_city, name='add city'),
    path('city/update_city/<cid>/', views.update_city, name='update city'),
    path('city/delete_city/<cid>/', views.delete_city, name='delete city'),
    path('WebApp/', views.webapps, name='WebApp'),
    path('country/', views.countries, name='country'),
    path('country/add_country/', views.add_country, name='add'),
    path('country/update_country/<cid>/', views.update_country, name='update country'),
    path('country/delete_country/<cid>/', views.delete_country, name='delete country'),
    path('image_upload/', views.imageUpload, name='image_upload'),
    path('display_upload/', views.display_images, name='display_image'),
    path('success', views.success, name='success'),
    path('about/', views.about, name='About'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)