from django.contrib import messages
from django.http import HttpResponseNotAllowed, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

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
    def __err(status: int, detail: str) -> JsonResponse:
        return JsonResponse(
            {'error': {'status': status, 'detail': detail}},
            status=status
        )
    if request.method != 'GET':
        return HttpResponseNotAllowed('GET')
    if not (no := request.GET.get('no')):
        return __err(422, "'no' not found")
    if not (no.isnumeric() and len(no) == 11 and no.startswith('7')):
        return __err(422, "'no' must be 11-digit number starting with '7'")
    if not (q := forms.find_snrange(int(no[1:]))):
        return __err(422, "OpSoS not found for the number")
    return JsonResponse(
        {'data': {'sn': int(no), 'opsos': q.opsos.name, 'region': q.region}},
        json_dumps_params={'ensure_ascii': False}
    )
