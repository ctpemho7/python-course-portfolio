from django.urls import path

from jobs.views import IndexDetailView

urlpatterns = [
    path("<int:pk>/", IndexDetailView.as_view(), name="job"),
]
