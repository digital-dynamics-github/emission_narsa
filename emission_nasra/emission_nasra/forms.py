# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label=_('username'), required=True)
    password = forms.CharField(label=_('Password'), required=True, widget=forms.PasswordInput(render_value=False))