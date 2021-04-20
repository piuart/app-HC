from django.contrib import admin
from django.urls import path, include
from core.homepage.views import IndexView


from core.login.views import *

from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import url
from django.contrib.auth import views as auth_views
from core.youtube import views as User

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/', include('core.chat.urls')),
    path('login/', include('core.login.url')),
    path('admin/', admin.site.urls),
    path('erp/', include('core.erp.urls')),
    path('reports/', include('core.reports.urls')),
    path('user/', include('core.user.urls')),

    #youtube
    path('youtube/', include('core.youtube.urls')),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)