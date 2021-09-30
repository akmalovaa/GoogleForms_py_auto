import requests
import mimesis
from mimesis import Person
from mimesis import locales
import random

GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSdBfczTD5A5IRcQEyBM2Id9cbRigaalPiDCaQhA_c4NawN0pA'

urlResponse = GoogleURL+'/formResponse'
urlReferer = GoogleURL+'/viewform'

pers = Person(locales.RU)
GenderList = ['MALE', 'FEMALE']
if random.choice(GenderList) == 'MALE':
    GenRandom = mimesis.enums.Gender.MALE
    Gender = 'Муж'
else:
    GenRandom = mimesis.enums.Gender.FEMALE
    Gender = 'Жен'

name = pers.full_name(GenRandom)
email = pers.email(domains=['mail.ru','yandex.ru','list.ru','gmail.com','bk.ru'])
phone = pers.telephone(mask='+7(9##)#######')

check_list = ['RSTP', 'IPSEC', 'DHCP', 'DNS', 'MSTP']

form_data = {'entry.1745782649': name,
            'entry.1180824424':Gender,
            'entry.2064015836': {random.choice(check_list),random.choice(check_list)},
            'entry.1671460138':'Mikrotik',
            'emailAddress':email,
            'entry.1065332859':phone
             }
user_agent = {'Referer':urlReferer,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
r = requests.post(urlResponse, data=form_data, headers=user_agent)
