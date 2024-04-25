from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("", index, name=""),
    path('get_software_lists/<int:subcategory_id>/', get_software_lists, name='get_software_lists'),
    path('software/<int:software_id>/', view_software_details, name='view_software'),
    path('all_details/',all_details,name="all_details"),
    path('edit_category/<int:category_id>/', edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),
    path('edit_subcategory/<int:subcategory_id>/', edit_subcategory, name='edit_subcategory'),
    path('delete_subcategory/<int:subcategory_id>/', delete_subcategory, name='delete_subcategory'),
    path('edit_softwarelist/<int:softwarelist_id>/', edit_softwarelist, name='edit_softwarelist'),
    path('delete_softwarelist/<int:softwarelist_id>/', delete_softwarelist, name='delete_softwarelist'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 