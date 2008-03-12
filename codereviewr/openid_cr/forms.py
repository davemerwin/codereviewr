from django import newforms as forms
from django.utils.translation import ugettext as _
from django.conf import settings

# needed for some linux distributions like debian
try:
    from openid.yadis import xri
except:
    from yadis import xri

import re

class OpenidSigninForm(forms.Form):
    openid_url = forms.CharField(max_length=255, widget=forms.widgets.TextInput(attrs={'class': 'required openid'}))
    next = forms.CharField(max_length=255,widget=forms.HiddenInput(), required=False)

    def clean_openid_url(self):
        if 'openid_url' in self.cleaned_data:
            openid_url = self.cleaned_data['openid_url']
            if xri.identifierScheme(openid_url) == 'XRI' and getattr(
                settings, 'OPENID_DISALLOW_INAMES', False
                ):
                raise forms.ValidationError(_('i-names are not supported'))
            return self.cleaned_data['openid_url']

    def clean_next(self):
        if 'next' in self.cleaned_data and self.cleaned_data['next'] != "":
            next_url_re = re.compile('^/[-\w/]+$')
            if not next_url_re.match(self.cleaned_data['next']):
                raise forms.ValidationError(_('next url "%s" is invalid' % self.cleaned_data['next']))
            return self.cleaned_data['next']


