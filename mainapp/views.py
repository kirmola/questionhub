from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Video
from django.views.generic import DetailView
from .models import country_codes


class TrendByCountryDetailView(DetailView):
    model = Video
    template_name = "mainapp/ytrends_tbc.html"
    slug_url_kwarg = "cc"
    slug_field = "trending_cc"

    def get_queryset(self):
        country_in_url = self.kwargs.get("cc")
        return super().get_queryset().filter(trending_cc=country_in_url)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["countries"] = country_codes
        return context
    

def home(request):

    return render(request, "mainapp/homepage.html", {
        "countries": country_codes
    })




def videofunc():
    for eachquestion in Video.objects.all():
        yield {
            "question_slug": eachquestion.question_slug
        }


def regions():
    pass