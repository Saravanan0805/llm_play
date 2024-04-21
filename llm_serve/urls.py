from django.urls import path
from llm_serve import views

urlpatterns = [
    path("onboard", views.OnboardAPI.as_view()),
]
