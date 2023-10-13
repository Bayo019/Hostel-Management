from django.contrib import admin
from django.urls import path

from portal.views import index_view, staff_dshbd_view, studnt_dshbd_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='hostel_portal'),
    path('staff_dashboard/', staff_dshbd_view, name='staff_page'),
    path('student_dashboard/', studnt_dshbd_view, name='student_page'),
    
]
