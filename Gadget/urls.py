"""
URL configuration for Gadget project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from new_gadget import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.show.as_view(), name="show_all"),
    path('', views.show.as_view(), name="show_all"),
    path('create/', views.create.as_view(), name = "create"),
    path('edit/<int:pk>', views.Edit.as_view(), name="edit"),
    path('delete/<int:pk>', views.Delete.as_view(), name="delete")
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
