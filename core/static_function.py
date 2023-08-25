from django.shortcuts import redirect


class Checker:
    def check_discord(user, discord_provider):
        if user.is_authenticated:
            discord_account = user.socialaccount_set.filter(provider=discord_provider).first()
            context = {}
            if discord_account:
                extra_data = discord_account.extra_data
                if extra_data["avatar"] is not None:
                    avatar_url = f'https://cdn.discordapp.com/avatars/{extra_data["id"]}/{extra_data["avatar"]}.png'
                else:
                    avatar_url = 'https://www.iguides.ru/upload/iblock/613/6132674b0998de6e986e0ff2fa50d663.jpg'
                context = {
                    'discord_account':discord_account,
                    'member':extra_data,
                    'avatar':avatar_url
                }
                
            else:
                context = {
                    'user':user
                }
            return context
        else:
            return redirect('discord_login')