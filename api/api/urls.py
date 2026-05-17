from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', UserList.as_view()),
    path('addresses/', AddressList.as_view()),
    path('address-types/', AddressTypeList.as_view()),
    path('phones/', PhoneList.as_view()),
    path('phone-types/', PhoneTypeList.as_view()),
    path('user-infos/', UserInfoList.as_view()),
    path('pages/', PageList.as_view()),
]