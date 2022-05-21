from rest_framework import serializers
from phone.models import Phone
from phone.utils import get_image


class PhoneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'
        read_only_fields = ('image_url',)

    def create(self, validated_data):
        phone = Phone.objects.create(image_url=get_image(
            validated_data['model_name']), **validated_data)
        return phone


class PhoneListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'brand_name', 'model_name', 'url', "image_url"]
