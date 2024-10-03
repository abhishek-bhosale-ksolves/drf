import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request,*args, **kwargs):
    """
    DRF API View
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)

# @api_view(['GET'])
# def api_home(request,*args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id 
#         # data['title'] = model_data.title 
#         # data['content'] = model_data.content 
#         # data['price'] = model_data.price
#         data = model_to_dict(model_data)
#     # body = request.body
#     # data = {}
#     # try:
#     #     data = json.loads(body)
#     # except:
#     #     pass
#     # print(data)
#     # return JsonResponse(data)
#     return Response(data)
