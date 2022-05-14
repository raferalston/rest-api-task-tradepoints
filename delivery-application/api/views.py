from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'workers': reverse('worker-list', request=request, format=format),
        'tradepoints': reverse('tradepoint-list', request=request, format=format),
        'visits': reverse('visit-list', request=request, format=format),
        'worker-tradepoints': reverse('worker-tradepoints-list', request=request, format=format),
    })
