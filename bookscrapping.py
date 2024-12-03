import requests
from bs4 import BeautifulSoup
import csv
import time
with open('books_scrapping6.csv','w',newline='')as file: 
    writer=csv.writer(file)
    writer.writerow(['Title','Price','availability'])
    for i in range(1,51):
        url=f'https://books.toscrape.com/catalogue/page-{i}.html'
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        books=soup.find_all('article',class_='product_pod')
        for book in books:
             Title = book.h3.a['title']  # Extract book title  
             Price = book.find(class_='price_color').text  # Extract book price  
             availability = book.find(class_='instock availability').text.strip()  # Extract availability  
             if Title and Price and availability:
                 writer.writerow([Title,Price,availability])
                 print('*' * 40)
                 print(f'page number{i}')
                 print('*' * 40)
        
