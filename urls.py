from django.urls import path, include
from myapp import views
urlpatterns = [
   path('',views.index), #path 없이 들어오면 views.index 실행
   path('create/',views.create),
   path('read/<id>/',views.read)
]
