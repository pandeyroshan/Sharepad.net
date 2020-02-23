from django.contrib import admin
from django.urls import path
from core import views as core_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.index,name='index'),
    path('my_room/<slug:room_id>',core_views.open_room,name='open_room'),
    path('add_file/<int:id>/',core_views.add_file,name='add_file'),
    path('delete_room/<int:id>/',core_views.delete_room,name='delete_room')
]
