from django import forms
from .models import ProdLeche,Alimento,ExistenciaTambo,ExistenciaRecria

class ProdLecheForm(forms.ModelForm):
    class Meta:
        model = ProdLeche
        fields = '__all__'

class FechasForm(forms.Form):
    inicio = forms.DateField()
    final = forms.DateField()

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = '__all__'

class ExistenciaTamboForm(forms.ModelForm):
    class Meta:
        model = ExistenciaTambo
        fields = '__all__'

class ExistenciaRecriaForm(forms.ModelForm):
    class Meta:
        model = ExistenciaRecria
        fields = '__all__'
