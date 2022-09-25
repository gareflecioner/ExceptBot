import requests
from bs4 import BeautifulSoup
import sqlite3


url='https://superstep.ru/catalog/kedy-obuv-muzh/filter/code_brand-converse/'
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")

def insert_db(itemName,itemPrice):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO convers (name,price)
    VALUES(?,?)
    """ ,(itemName,itemPrice) )
    conn.commit()

items=soup.find_all("div",class_='product-item col-sm-4 col-xs-6')

for n,i in enumerate(items,start=1):
    itemName=i.find("p",class_="product-name").text.strip()
    itemPrice=i.find("span",class_="product-sale-price").text.strip()

    #вызываю функцию и определяю переменные
    insert_db(itemName,itemPrice)

    print(f"{n}: {itemName} за  {itemPrice}")

    #поменьше сайт нужно выбрать))))))
