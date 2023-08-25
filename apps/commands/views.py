from .models import QiqiCommandsModel, QiqiCommandsCategoryModel
from django.shortcuts import render, redirect
from core.static_function import Checker
from allauth.socialaccount.providers.discord.provider import DiscordProvider
from django.views.generic.base import View
from .forms import CommandsForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy



# Вьюсы, которые будут рендерить странички

class CommandsCategoryView(View):
    def get(self, request, category_id):
        user = request.user
        discord_provider = DiscordProvider.id
        check_context = Checker.check_discord(user=user, discord_provider=discord_provider)
        check_context['commands'] = QiqiCommandsModel.objects.filter(command_category=category_id).order_by('-created_at')
        check_context['categories'] = QiqiCommandsCategoryModel.objects.all()

        if check_context:
            if user.is_staff:
                check_context['form'] = CommandsForm()
            return render(request, 'commands/commands.html', context=check_context)
        else:
            return redirect('discord_login')
    
    def post(self, request, *args, **kwargs):
        form = CommandsForm(request.POST)
        if form.is_valid():
            command = form.save()
            command.save()
            return HttpResponseRedirect(reverse_lazy('commands'))
        else:
            return HttpResponseRedirect(reverse_lazy('commands'))


class CommandsView(View):
    def get(self, request):
        user = request.user
        discord_provider = DiscordProvider.id
        check_context = Checker.check_discord(user=user, discord_provider=discord_provider)
        check_context['commands'] = QiqiCommandsModel.objects.order_by('-created_at')
        check_context['categories'] = QiqiCommandsCategoryModel.objects.all()

        category_id = request.GET.get('category_id')

        if category_id:
            return redirect('commands_category', category_id=category_id)
        
        if check_context:
            if user.is_staff:
                check_context['form'] = CommandsForm()
            return render(request, 'commands/commands.html', context=check_context)
        else:
            return redirect('discord_login')
    

    def post(self, request, *args, **kwargs):
        form = CommandsForm(request.POST)
        if form.is_valid():
            command = form.save()
            command.save()
            return HttpResponseRedirect(reverse_lazy('commands'))
        else:
            print(f'Не валидно {form.errors}')
            
            return HttpResponseRedirect(reverse_lazy('commands'))
    
