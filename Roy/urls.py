from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chekigari.urls')),
    path('myapp/', include("my_app.urls"))
]
