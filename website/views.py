from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views import generic, View
from .models import Booking


def home(request, template_name="index.html"):
    return TemplateResponse(
        request, template_name, {'background': "background-lg"}
    )

def about(request, template_name="about.html"):
    return TemplateResponse(
        request, template_name, {'background': "background-plain"}
    )
