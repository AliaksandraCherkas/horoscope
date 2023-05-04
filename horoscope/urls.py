from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")
register_converter(converters.MyFloatConverter,"my_float")
#register_converter(converters.MyDateConverter,"my_date")

urlpatterns = [
    path("", views.index),
    path("types", views.get_info_about_type),
    path("types/<element>", views.get_info_about_element, name='element-name'),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_by_number),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_zodiac, name = 'horoscope-name'),
    
    
]