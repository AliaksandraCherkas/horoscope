from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types = {
    'fire':['aries',  'leo',  'sagittarius'],
    'earth':[ 'taurus',  'virgo',  'capricorn' ],
    'air': [ 'gemini',  'libra',   'aquarius'],
    'water': [ 'cancer',  'scorpio',  'pisces' ]

}

def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'you entered four digits - {sign_zodiac}')

def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'you entered float digit - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    rez = ""
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign])
        rez += f'<h2><li><a href="{redirect_path}">{sign.title()}</a></li></h2>'
    redirect_types = reverse('horoscope-name', args=['types'])
    response = f'<ol>{rez}</ol><br><h2><a href="{redirect_types}">Elements</a></h2>'
    return HttpResponse(response)



def get_info_about_zodiac(request, sign_zodiac:str):
   
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h1>{description}</h1>')
    
    else:
        return HttpResponseNotFound(f'неизвестный знак зодиака  - {sign_zodiac}')



def get_info_about_zodiac_by_number(request, sign_zodiac:int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'неизвестный номер  зодиака  - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
    #return HttpResponseRedirect('https://docs.djangoproject.com/en/4.2/search/?q=path+converter')

def get_info_about_type(request):
    types_list = list(types)
    rez = ""
    for type in types_list:
        redirect_element = reverse('element-name',args = [type])
        rez += f'<h2><li><a href="{redirect_element}">{type.title()}</a></li><?h2>' 
    response = f'<ol>{rez}</ol>'
    return HttpResponse(response)

def get_info_about_element(request, element):
    #types_list = list(types)
    if element in types:
        rez = ''
        for i in types[element]:
            redirect_i = reverse('horoscope-name', args = [i])
            rez+=f'<h2><li><a href="{redirect_i}">{i.title()}</a></li></h2>'
        response  = f'<ol>{rez}</ol>'

        return HttpResponse(response)
        # return HttpResponse(types[element])
    else:
      return HttpResponseNotFound(f'неизвестная  стихия  - {element}')  


