from django.shortcuts import redirect, render
from django.views.generic.base import View

def handler404(request, exception):
    return redirect('404')

def handler403(request, exception):
    return redirect('404')


class Page404(View):
    def get(self, request):
        return render(request, 'errors/page404.html', status=404)