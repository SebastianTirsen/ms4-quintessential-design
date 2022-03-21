from django.http import HttpResponse


class StripeWH_Handler:
    def__init__(self, request):
        self.request = request

    def_handle_event(self, event):
    return HttpResponse(
        content=f'Webhook recieved: {event["type"]}',
        status=200)
