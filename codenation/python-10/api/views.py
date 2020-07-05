

from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter

@api_view(["POST"])
def lambda_function(request):

    data = request.data.get('question')
    data =list(Counter(data).elements())
    solution = sorted(data, key=data.count, reverse=True)
    return Response({'solution': solution}) 

