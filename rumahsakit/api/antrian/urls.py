from django.urls import path
from . import views

urlpatterns = [
    path('now/<int:searchId>', views.GetAntrianNow.as_view()),
    path('add/<int:searchId>', views.AddAntrian.as_view()),
    path('reduce/<int:searchId>', views.ReduceAntrian.as_view()),
]