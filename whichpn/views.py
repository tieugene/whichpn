from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages
import forms


class FindPhone(FormView):
    form_class = forms.PhoneForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """form.cleaned_data['org']:Org item"""
        data = form.cleaned_data
        messages.add_message(
            self.request,
            messages.INFO,
            f"+7{data['phone']}: {data['snrange'].opsos} ({data['snrange'].region})"
        )
        return super().form_valid(form)
