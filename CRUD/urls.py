from django.urls import include, path
from django.contrib import admin
from django.conf import settings # new
from django.conf.urls.static import static # new



api_urls = [

    path('', include('crudapp.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
