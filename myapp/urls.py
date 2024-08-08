from django.urls import path
from .views import *

urlpatterns = [
   path('list_student/', student_list),

   path('create/', create_list),

   path('update/<int:id>/', update_student),

]