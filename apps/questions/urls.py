from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="Home"),
    path('login/', views.login_view, name="Login"),
    path('registro/', views.registro, name="Registro"),
    path('logout/', views.logout_view, name="Logout"),
    path('questions/',views.upload_question, name="Questions"),
    path('answers/<int:question_id>/',views.upload_answer,name="Answers"),
    path('answers1/',views.show_answers, name="Answer1"),
]
#path('answers1/',views.show_answers, name="Answer1"), 