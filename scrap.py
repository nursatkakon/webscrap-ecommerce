import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card'

#Opening up connection & grabing the page content
uClient = ureq(my_url)
pageHtml = uClient.read()
uClient.close()

#HTML parsing
pageSoup = soup(pageHtml, "html.parser")
#print(pageSoup.p)

#grab each products in CSV files
containers = pageSoup.findAll("div", {"class": "item-container"})
'''
print (len(containers))
print (containers[0])
contain = containers[0]
container = containers[0]
print (container.div.div.a.img["title"])

contain = containers[0]
container = containers[0]
title_container = container.findAll("a", {"class": "item-title"})
print (title_container)

contain = containers[0]
container = containers[0]
title_container = container.findAll("li", {"class": "price-ship"})
print (title_container)
'''

filename = "product.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:

    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
f.close()


    




