from django.urls import path
from . import views


urlpatterns = [
    path('',views.modelform),
    path('editt/<int:id>/',views.form_edit,name='form_edit'),
    path('form_change',views.form_change),
    path('form',views.form,name='form_register'),
    path('new_register',views.new_register),

]
