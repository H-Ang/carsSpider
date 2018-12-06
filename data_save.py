def savdFile(datas):
    # 保存到文本文件
    with open('J:\DATAs\北京市二手车(汽车之家)\data.txt','a+',encoding='utf-8') as f:
        for data in datas:
            # try:
            #     name = data.name
            #     gonglishu = data.gonglishu
            #     brought_year = data.brought_year
            #     location = data.location
            #     img_url = data.img_url
            #     price = data.price
            #     writeCont = name+"/"+gonglishu+"/"+brought_year+"/"+location+"\n"+price+"图片地址:"+img_url
            #     f.write(writeCont+'\n\n')
            # except:
            #     print(writeCont)
            name = data.name
            gonglishu = data.gonglishu
            brought_year = data.brought_year
            location = data.location
            img_url = data.img_url
            price = data.price
            writeCont = name+"/"+gonglishu+"/"+brought_year+"/"+location+"\n"+price+"图片地址:"+img_url
            f.write(writeCont+'\n\n')
    print('保存完成。')


from openpyxl import Workbook
def saveExcel(datas):
    # 保存到Excel表中
    try:

        print('写入excel成功')
    except Exception:
        print('写入excel失败')



# 将数据保存到数据库中
from  sqlalchemy import Column,create_engine,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Car(Base):
    __tablename__ = "second_cars"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    carName = Column(String(100))
    gonglishu = Column(String(20))
    brought_year = Column(String(10))
    location = Column(String(10))
    image_url = Column(String(200))
    price = Column(String(10))

def saveMysql(datas):
    connect = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/second_cars",
                            encoding='utf-8',
                            echo=True)


    Base.metadata.create_all(connect)

    DBsession = sessionmaker(bind=connect)
    session = DBsession()

    for data in datas:

        car = Car(
            carName=data.name,
            gonglishu = data.gonglishu,
            brought_year = data.brought_year,
            price=data.price,
            location = data.location,
            image_url = data.img_url,
        )

        session.add(car)
        session.commit()
        session.close()