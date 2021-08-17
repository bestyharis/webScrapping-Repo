from bs4 import BeautifulSoup
import requests 
from csv import writer


url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&Locality=C-V-Raman-Nagar&cityName=Bangalore&BudgetMin=5-Lacs&BudgetMax=10-Lacs'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
soup.prettify()
lists = soup.find_all('div',class_ = 'm-srp-card__area')
with open('housing.csv','w',encoding='utf8',newline='n') as f:
    thewriter=writer(f)
    header=['Title','society','BHK','SQFT Area','Price']
    writer.writerow(header)

    for list in lists:
        price = lists.price('div',class_="m-srp-card__price").text().replace("\n","")
        sqftarea = lists.find('span',class_='semi-bold').text().replace("\n","")
        title = lists.find('span',class_="m-srp-card__title").text().replace("\n","")
        society = lists.find('a',class_='m-srp-card__link').text().replace("\n","")
        bhk = lists.find('span',class_='m-srp-card__title__bhk').text().replace("\n","")
        info =[title,society,bhk,sqftarea,price]
        writer.writerow(info)
