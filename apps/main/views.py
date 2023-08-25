from django.shortcuts import render,redirect
from django.views.generic.base import View
from allauth.socialaccount.providers.discord.provider import DiscordProvider
from core.static_function import Checker


class HomePage(View):
    def get(self, request):
        user = request.user
        discord_provider = DiscordProvider.id
        check_context = Checker.check_discord(user=user, discord_provider=discord_provider)

        if user.is_authenticated:
            if check_context:
                return render(request, 'main/main.html', context=check_context)
            else:
                return redirect('discord_login')
        else:
            return redirect('discord_login')


class AboutDevelopersPage(View):
    def get(self, request):
        user = request.user
        discord_provider = DiscordProvider.id
        check_context = Checker.check_discord(user=user, discord_provider=discord_provider)

        if check_context:
            return render(request, 'main/developers.html', context=check_context)
        else:
            return redirect('discord_login')

