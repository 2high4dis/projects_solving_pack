import requests
from bs4 import BeautifulSoup as bs
import os

os.system('cls || clear')

signs = {'Овен': 'aries', 'Телец': 'taurus', 'Близнецы': 'gemini', 'Рак': 'cancer', 'Лев': 'lion', 'Дева': 'virgo',
         'Весы': 'libra', 'Скорпион': 'scorpio', 'Стрелец': 'sagittarius', 'Козерог': 'capricorn', 'Водолей': 'aquarius', 'Рыбы': 'pisces'}

URL_TEMPLATE = 'https://orakul.com/horoscope/astrologic/more/%s/today.html'

sign = input('Введите свой знак зодиака: ').capitalize()

url = URL_TEMPLATE % signs[sign]

request = requests.get(url)

soup = bs(request.text, 'html.parser')
horoscope = str(soup.find('div', class_='horoBlock').find(
    'p')).replace('<p class="">', '').replace('</p>', '').lstrip()

print()
print(horoscope)
