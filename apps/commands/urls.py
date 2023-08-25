from django.urls import path,include
from . import views
from . import crudviews


urlpatterns = [
    #COMMANDS
    path('commands/', views.CommandsView.as_view(), name='commands'),
    path('commands/category/<int:category_id>/', views.CommandsCategoryView.as_view(), name='commands_category'),

    #CRUD
    # path('commands/create/', crudviews.CommandsCreatView.as_view(), name='commandsCreate'), ДЕРЬМО ЕБАНОЕ, ХУЙНЯ ВОНЮЧАЯ, РОТ ЕЁ ТРАХАЛ, ВСЕХ МАТЕРЕЙ ЕБАЛ!
    path('commands/update/<int:command_id>/', crudviews.CommandsUpdateView.as_view(), name='commands_update'),
    path('commands/delete/<int:pk>/', crudviews.CommandsDeleteView.as_view(), name='commandsDelete'),
    # path('commands/update/<int:pk>/', crudviews.CommandsUpdateView.as_view(), name='commandsUpdate'),

]

