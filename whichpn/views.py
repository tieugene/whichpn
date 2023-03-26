from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

import core.models
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


def endpoint(request):
    if request.method == 'GET':
        # print(request.GET)
        if 'no' not in request.GET:
            return HttpResponseBadRequest()
        no = request.GET['no']
        if not (isinstance(no, str) and no.isnumeric() and len(no) == 11 and no.startswith('7')):
            return HttpResponseBadRequest()
        no = int(no[1:])
        if not (q := forms.find_snrange(no)):
            return HttpResponseBadRequest()
        print(q)
        return HttpResponse()  # OK
    else:
        return HttpResponseNotAllowed('GET')
