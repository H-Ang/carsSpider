# 汽车之家爬虫，北京二手车
import requests
from lxml import etree
from data_save import *
import time

class Car_second():
    name = ''
    gonglishu = ''
    brought_year = ''
    location = ''
    img_url = ''
    price = ''

def getInfors(url,i):
    print("Page %d is saving." % i)
    headers = {
        "Cache-Control":"no-cache",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Referer":"https://www.che168.com/beijing/list/",
    }

    response = requests.get(url=url,headers=headers)

    html = response.text

    ob_xml = etree.HTML(html)

    infos = ob_xml.xpath('//*[@id="viewlist_ul"]//li[not(contains(@class,"adv-img"))]/a')

    secondCars = []
    for info in infos:
        if info.xpath('.//img/@src2') == []:
            img = info.xpath('.//img/@src')[0]
        else:
            img = info.xpath('.//img/@src2')[0]

        name = info.xpath('.//h4/text()')[0]

        price = info.xpath('.//span[@class="price"]/text()')[0] + info.xpath('.//em/text()')[0]

        myl = info.xpath('.//p/text()')[0].split('／')
        gonglishu = myl[0]
        brought_year = myl[1]
        location = myl[2]

        secondCar = Car_second()
        secondCar.name = name
        secondCar.img_url = img
        secondCar.brought_year = brought_year
        secondCar.location = location
        secondCar.gonglishu = gonglishu
        secondCar.price = price

        secondCars.append(secondCar)

    return secondCars

if __name__ == '__main__':
    url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp{}exx0/'
    for i in range(1,101):
        car_infors = getInfors(url.format(i),i)
        time.sleep(0.95)
        #savdFile(car_infors)
        saveMysql(car_infors)