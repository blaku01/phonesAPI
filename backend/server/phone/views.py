from django.shortcuts import get_object_or_404
from phone.serializers import PhoneListSerializer, PhoneDetailSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from phone.models import Phone
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator
from phone.filters import TrigramSimilaritySearchFilter


class PhoneViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing phones.
    """

    queryset = Phone.objects.all()
    serializers = {
        'list':    PhoneListSerializer,
        'detail':  PhoneDetailSerializer,
    }
    filter_backends = (TrigramSimilaritySearchFilter,)
    filter_fields = ('model_name', 'brand_name')

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializers.get("list")
        else:
            return self.serializers.get("detail")

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
