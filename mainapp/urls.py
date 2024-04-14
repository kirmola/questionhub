from django.urls import path
from .views import (
    TrendByCountryDetailView,
    videofunc,
    regions,
)
from django_distill import distill_path

urlpatterns = [
    distill_path("trends-in-<slug:cc>/", TrendByCountryDetailView.as_view(), name="Trendbycountry_detail", distill_func=videofunc)
]

