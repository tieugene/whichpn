from typing import Optional

from django import forms
from django.utils.translation import gettext as _

import core.models


def find_snrange(sn: int) -> Optional[core.models.SNRange]:
    if q := core.models.SNRange.objects.filter(ndc=sn // 10000000, beg__lte=sn % 10000000, end__gte=sn % 10000000):
        return q[0]


class PhoneForm(forms.Form):
    phone = forms.IntegerField(
        min_value=1000000000,
        max_value=9999999999,
        label=_("Phone"),
        help_text=_("+7 ##########")
    )
    snrange = forms.ModelChoiceField(
        queryset=core.models.SNRange.objects.all(),
        required=False,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super().clean()
        ph = cleaned_data.get('phone')
        if q := find_snrange(ph):
            cleaned_data['snrange'] = q
            return cleaned_data
        else:
            self.add_error(None, _("Not found"))
