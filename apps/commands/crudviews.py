from django.http import HttpResponseRedirect
from .forms import CommandsForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import View
from .models import QiqiCommandsModel
from django.urls import reverse_lazy
from django.shortcuts import redirect, render


"""
CRUD Views - представления в django, которые предоставляют возможность взаимодействия с моделью. CRUD - это аббревиатура методов взаимодействия с базами данных

C - Create (создание)
R - Read (чтение)
U - Update (обновление)
D - Delete (удаление)

"""




class CommandsDeleteView(DeleteView):
    model = QiqiCommandsModel
    success_url = reverse_lazy('commands')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class CommandsUpdateView(View):
    def post(self, request, command_id):
        form = CommandsForm(request.POST)
        if form.is_valid():
            command = QiqiCommandsModel.objects.get(id=command_id)
            for field_name, field_value in form.cleaned_data.items():
                setattr(command, field_name, field_value)
            command.save()
        return redirect('commands')

        
        
            
            

