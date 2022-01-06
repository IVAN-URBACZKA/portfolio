from django.urls import path
from .views import ProjectPostHomeView

app_name = "projects"


urlpatterns = [
    path('', ProjectPostHomeView.as_view(), name="projects"),
]