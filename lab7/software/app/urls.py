from django.urls import path
from . import views
# файл-маршрутизатор, который по url выбирает нужный метод в views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('version/create/', views.VersionCreate.as_view(template_name="app/version_form.html"), name='version-create'),
    path('software/create/', views.SoftwareCreate.as_view(template_name="app/software_form.html"), name='software-create'),
    path('version/<int:pk>', views.VersionDetailView.as_view(template_name="app/version_detail.html"), name='version-detail'),
    path('software/<int:pk>', views.SoftwareDetailView.as_view(template_name="app/software_detail.html"), name='software-detail'),
    path('version/<int:pk>/update/', views.VersionUpdate.as_view(template_name="app/version_form.html"), name='version-update'),
    path('software/<int:pk>/update/', views.SoftwareUpdate.as_view(template_name="app/software_form.html"), name='software-update'),
    path('version/<int:pk>/delete/', views.VersionDelete.as_view(template_name="app/version_confirm_delete.html"), name='version-delete'),
    path('software/<int:pk>/delete/', views.SoftwareDelete.as_view(template_name="app/software_confirm_delete.html"), name='software-delete'),
]