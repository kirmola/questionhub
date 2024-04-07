from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Question
from django.views.generic import DetailView


class QuestionDetailView(DetailView):
    model = Question
    template_name = "mainapp/index.html"
    slug_url_kwarg = "question_slug"
    slug_field = "question_slug"

    def get_queryset(self):
        current_question_slug = self.kwargs.get("question_slug")
        return super().get_queryset().filter(question_slug=current_question_slug)