"""
URL configuration for photography project.

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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from authentication import views as authentication
from gallery import views as gallery # type: ignore
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),

    #AUTHENTICATIONS URLS
    path('sign_up/', authentication.sign_up, name='sign_up'),
    path('login/', authentication.user_login, name='login'),
    path('logout/', authentication.user_logout, name='logout'),
    path('changepass/', authentication.user_change_pass, name='changepass'),
    path('newpass/', authentication.user_new_pass, name='newpass'),

    #GALLERY URLS
    path('', gallery.home_page, name='home'),
    path('about/', gallery.about_page, name='about'),
    path('contect/', gallery.contect_page, name='contect'),
    path('dashboard/', gallery.dashboard_view, name='dashboard'),
    path('home/', gallery.home_page, name='home'),
    path('upload_img/', gallery.upload_img_view, name='upload_img'),
    path('view_img/', gallery.view_img_view, name='view_img'),
    path('all_pic/', gallery.all_picture_page, name='all_pic'),
    path('delete/<int:id>/', gallery.delete_img, name='delete_img'),
    path('<int:id>/', gallery.edit_data, name='edit_data'),

]

if settings.DEBUG: # type: ignore
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore

