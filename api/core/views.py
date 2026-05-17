from rest_framework import generics
from .models import *
from .serializers import *


class UserList(generics.ListAPIView):
    queryset = WebUser.objects.all()
    serializer_class = WebUserSerializer


class AddressList(generics.ListAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer


class AddressTypeList(generics.ListAPIView):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer


class PhoneList(generics.ListAPIView):
    queryset = UserPhone.objects.all()
    serializer_class = UserPhoneSerializer


class PhoneTypeList(generics.ListAPIView):
    queryset = PhoneType.objects.all()
    serializer_class = PhoneTypeSerializer


class UserInfoList(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class PageList(generics.ListAPIView):
    queryset = PageData.objects.all()
    serializer_class = PageDataSerializer