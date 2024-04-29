from django import forms

class FilmeSearchForm(forms.Form):
    rating = forms.IntegerField(label='Rating', required=False)
    diretor = forms.CharField(label='Nome do Diretor', required=False)
    nome_filme = forms.CharField(label='Nome do Filme', required=False)
    ano = forms.IntegerField(label='Ano', required=False)
