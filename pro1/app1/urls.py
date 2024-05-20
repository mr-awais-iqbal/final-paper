
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.page1 , name = 'datepage'),
    path('page/<int:id>' ,views.page2 , name = "page"),
    path('formmate/' , views.forming , name = 'forming'),
    path('adddata/', views.adddata , name = "adddata"),
    path('delete/<int:id>' , views.delete , name = "delete"),
    path('update/<int:id>', views.update , name='update')
]
