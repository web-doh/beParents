from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import requests
import collections


import sys
sys.path.append("/Users/iyeonji/Desktop/env/beParents")


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beParents.settings')
import django
django.setup()


from centers.models import Center




def center_info():
    
    real_final = []

    extra_list = []
    
    files = ['/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/신안군아동심리_전체(6).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/아산시아동심리_전체(54).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/안동시아동심리_전체(23).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/안산아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/안산아동심리_2(42).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/안성아동심리_전체(28).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/안양동안구아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/안양동안구아동심리_2(14).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/안양만안구아동심리_전체(48).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/양구군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/양산시아동심리_전체(28).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/양주아동심리_전체(53).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/양평군아동심리_전체(9).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/여수아동심리_전체(22).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/여주시아동심리_전체(19).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/연천군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/영광군아동심리_전체(1).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/영덕군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/영동군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/영암군아동심리_전체(21).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/영월군아동심리_전체(10).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/영주시아동심리_전체(8).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/영천시아동심리_전체(20).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/예산군아동심리_전체(11).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/예천군아동심리_전체(8).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/오산아동심리_전체(57).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/오은영아카데미.json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/옥천군아동심리_전체(4).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/완도군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/완산구아동심리_전체(32).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/완주군아동심리_전체(45).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/용인기흥구아동심리_1(50개).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/용인기흥구아동심리_2(44).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/용인수지구아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/용인수지구아동심리_2(28).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/용인처인구아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/용인처인구아동심리_2(21).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/울산남구아동심리_전체(49).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/울산동구아동심리_전체(10).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/울산북구아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/울산북구아동심리_2(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/울산울주군아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/울산울주군아동심리_2(44).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/울산중구아동심리_전체(39).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/울진군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/원주아동심리_전체(26).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/음성군아동심리_전체(11).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/의령군아동심리_전체(8).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/의왕아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/의왕아동심리_2(36).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/의정부시아동심리_전체(26).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/이천아동심리_전체(17).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/익산시아동심리_전체(20).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인제군아동심리_전체(3).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천강화군아동심리_전체(3).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천계양구아동심리_전체(28).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천남동구아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천남동구아동심리_2(22).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천동구아동심리_전체(24).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천미추홀구아동심리_전체(51).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천부평구아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천부평구아동심리_2(33).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천서구아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천서구아동심리_2(61).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천연수구아동심리_전체(37).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천옹진군아동심리_전체(7).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/인천중구아동심리_전체(44).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/임실군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/장성군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/장수군아동심리_전체(5).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/장흥군아동심리_전체(1).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/정선군아동심리_전체(3).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/정읍시아동심리_전체(11).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/제주서귀포시아동심리_전체(25).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/제주제주시아동심리_전체(31).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/제천시아동심리_전체(14).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/증평군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/진도군아동심리_전체(1).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/진안군아동심리_전체(7).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/진주시아동심리_전체(26).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/진천군아동심리_전체(7).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/창녕군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/창원시마산합포구아동심리_전체(21).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/창원시마산회원구아동심리_전체(34).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/창원시성산구아동심리_전체(53).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/창원시의창구아동심리_전체(58).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/창원시진해구아동심리_전체(23).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/천안아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/천안아동심리_2(35).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/철원군아동심리_전체(3).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/청도군아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/청도군아동심리_2(32).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/청송군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/청양군아동심리_전체(2).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/청주시상당구아동심리_전체(36).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/청주시서원구아동심리_전체(37).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/청주시청원구아동심리_전체(16).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/청주시흥덕구아동심리_전체(37).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/춘천아동심리_전체(19).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/충주시아동심리_전체(17).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/칠곡군아동심리_전체(59).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/태백:삼척시아동심리_전체(1).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/태안군아동심리_전체(5).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/통영시아동심리_전체(23.json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/파주시아동심리_전체(39).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/평택아동심리_전체(46).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/포천시아동심리_전체(22).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/포항남구아동심리_전체(31).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/포항북구아동심리_전체(30).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/하남아동심리_전체(65).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/하동군아동심리_전체(11).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/함안군아동심리_전체(37).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/함양군아동심리_전체(5).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/함평군아동심리_전체(7).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/합천군아동심리_전체(4).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/해남군아동심리_전체(8).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/홍성군아동심리_전체(6).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/홍천군아동심리_전체(19).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/화성 아동심리_2(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/화성아동심리_1(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/화성아동심리_3(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/화성아동심리_4(50).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/화성아동심리_5(30).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/화순군아동심리_전체().json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/화천군아동심리_전체(1).json',
        '/Users/iyeonji/Desktop/env/beParents/centers/static/centers/centers_data/횡성군아동심리_전체(23).json'

        ]

    for a in files:
        with open(a, 'rt') as json_file:
            content = json.load(json_file)

        #운영시간과 x,y좌표 

        for i in content['data']['places']['items']:
            n_id = i['id']
            runhours = i['businessHours']
            
            x = i['y']
            y = i['x']


        
            dic = {}
            dic['n_id'] = n_id
            dic['runhours'] = runhours
            dic['x'] = x
            dic['y'] = y


            
            
            extra_list.append(dic)



        center_id_list = []
        for x in content['data']['places']['items']:
            api_id = x['id']
            center_id_list.append(api_id)
        
        
        
        
        driver = webdriver.Chrome('/Users/iyeonji/Desktop/env/beParents/centers/chromedriver')
        base_url = 'https://map.naver.com/v5/entry/place/'


        #그외 기타 자료들
        for i in center_id_list:

            final = {}

            url = base_url + i
            driver.implicitly_wait(5)
            driver.get(url)

            
                
            iframes = driver.find_elements_by_css_selector('iframe')
            for iframe in iframes:
                iframe.get_attribute('id')
                
            driver.switch_to.frame('entryIframe')

            center_info = []

            try:
                c_name = driver.find_element_by_class_name('_3XamX').text
                center_info.append(c_name)
            except:
                pass

            try:    
                c_type = driver.find_element_by_class_name('_3ocDE').text
                center_info.append(c_type)
            except:
                pass
            
            try:
                phone = driver.find_element_by_class_name('_3ZA0S')
                phone_num = phone.text
                center_info.append(phone_num)
            except:
                phone_num = None
                center_info.append(phone_num)

            try:
                c_address = driver.find_element_by_class_name('_2yqUQ').text
                center_info.append(c_address)
            except:
                pass


            try:
                homepage = driver.find_element_by_xpath("//a[@class='_1RUzg']")
                homepage_list = homepage.text
            except:
                homepage_list = None



            hashtags = driver.find_elements_by_xpath("//span[@class='_1RUzg']")

            hashtag_list = []
            for hashtag in hashtags:
                data = hashtag.text
                hashtag_list.append(data)

            urls = driver.find_elements_by_xpath("//li[@class='_3xK_0']/a")

            url_list = []
            for url in urls:
                data2 = url.get_attribute("href")
                url_list.append(data2)

            contents = driver.find_elements_by_class_name('_3kKqj')

            content_list = []
            for content in contents:
                data3 = content.text
                content_list.append(data3)

            final['n_id'] = i    
            final['center_info'] = center_info
            final['homepage_list'] = homepage_list
            final['hashtag_list'] = hashtag_list
            final['url_list'] = url_list
            final['content_list'] = content_list
        
            real_final.append(final)

        
        end_list = []
        for aa in real_final:
            for bb in extra_list:
                if aa["n_id"] == bb["n_id"]:
                    cc = dict(aa, **bb)
                    end_list.append(cc)

        end = list({v['n_id']:v for v in end_list}.values())
    
    return end





if __name__== '__main__':
    center_list = center_info()


    
    for a in center_list:
        try:
            n_id = a['n_id']
            center_name = a['center_info'][0]
            center_type = a['center_info'][1]
            center_phone = a['center_info'][2]
            center_address = a['center_info'][3]
            homepage = a['homepage_list']
            runhours = a['runhours']
            hashtags = a['hashtag_list']
            content_urls = a['url_list']
            contents = a['content_list']
            x = a['x']
            y = a['y']

            
            Center(center_name=center_name, center_type=center_type, center_phone=center_phone, center_address=center_address, homepage = homepage, runhours = runhours, content_urls = content_urls, hashtags = hashtags, contents = contents, x = x, y = y, n_id=n_id).save()
        except:
            pass 



    






 
