from django.urls import path, include
from allauth.socialaccount.providers.discord.views import DiscordOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import (OAuth2LoginView, OAuth2CallbackView)
from allauth.account.views import LogoutView

urlpatterns = [
    path('accounts', include('allauth.urls')),
    path('accounts/discord/login/',OAuth2LoginView.adapter_view(DiscordOAuth2Adapter),name='discord_login'),
    path('accounts/discord/login/callback/',OAuth2CallbackView.adapter_view(DiscordOAuth2Adapter),name='discord_callback'),
    path('accounts/logout',LogoutView.as_view(),name='logout'),
]