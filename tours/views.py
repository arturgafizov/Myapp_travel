from django.shortcuts import render

from django.views import View

from django.http import HttpResponseNotFound, HttpResponseServerError

from tours.data import tours

from tours.data import departures

from tours.data import dic

from tours.data import dic2

from tours.data import dic_all
# Create your views here.

title = "Stepik Travel"
subtitle = "Для тех, кого отвлекают дома"
description = "Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование,' \
' дизайн, разработку игр и управление продуктами"


def custom_handler404(request, exception=None):
    return HttpResponseNotFound('Ой, кажется запроссили не существующию страницу!')


def custom_handler500(request):
    return HttpResponseServerError('Server error')


class DepartureView(View):
    def get(self, request, departure):
        context = {'departure_main': departure,
                   'tour': tours,
                   'departure': departures,
                   'dic_sec': dic2,
                   'all_depart': dic_all[departure]
                   }
        return render(
            request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, id: int):

        context = {'departure': departures, 'tour': tours[id], 'depart': departures[tours[id]['departure']]}
        return render(
            request, 'tours/tour.html', context=context)


class BaseView(View):
    def get(self, request, *args, **kwargs):
        context = {'departure': departures, 'ls': dic, 'tour': tours}
        return render(request, 'base.html', context=context)
