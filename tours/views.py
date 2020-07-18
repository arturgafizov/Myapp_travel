from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
from tours.apart_tours import tours
from tours.apart_departure import departures
# Create your views here.

title = "Stepik Travel"
subtitle = "Для тех, кого отвлекают дома"
description = "Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование,' \
' дизайн, разработку игр и управление продуктами"


class MainView(View):
    def get(self, request):
        return render(
            request, 'tours/index.html'
        )


def custom_handler404(request, exception=None):
    return HttpResponseNotFound('Ой, кажется запроссили не существующию страницу!')


def custom_handler500(request):
    return HttpResponseServerError('Server error')


class DepartureView(View):
    def get(self, request, place_departure: str):
        context = {'departure': departures[place_departure]}
        return render(
            request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, id: int):
        context = {'tour': tours[id]}

        return render(
            request, 'tours/tour.html', context=context)
