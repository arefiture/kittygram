from django.urls import path

from cats.views import cat_detail, cat_list

urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:pk>/', cat_detail),
]
