from rest_framework import serializers
from .models import Message, Parcel

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('sender','recepient','shippingPoint','destination','indexShipping','indexDestination','messageType','weight')

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ('sender','recepient','shippingPoint','destination','indexShipping','indexDestination','number','messageType','weight')