from django import forms
from . import models

class LocalProjectForm(forms.Form):
    驻地 = forms.ModelMultipleChoiceField(queryset=models.local.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    项目 = forms.ModelMultipleChoiceField(queryset=models.project.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))

class UpdateFileForm(forms.Form):
    升级文件地址 = forms.CharField(label='升级文件',max_length=256,widget=forms.URLInput(attrs={'class': 'form-group'}))