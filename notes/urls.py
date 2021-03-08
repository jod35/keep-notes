from django.urls import path
from . import views

app_name='notes'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('delete/<int:id>/',views.NoteDeleteView.as_view(),name='delete_note'),
    path('update/<int:id>/',views.NoteUpdateView.as_view(),name='update_note'),
]