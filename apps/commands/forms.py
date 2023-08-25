from django.forms.models import ModelForm
from .models import QiqiCommandsModel


class CommandsForm(ModelForm):
    class Meta:
        model = QiqiCommandsModel
        fields = '__all__'
