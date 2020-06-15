from bs4 import BeautifulSoup
import requests

url = "https://www.dolarhoy.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


col6 = soup.find_all("div", class_="col-6")
precioDeCompra = col6[0].find_all("span")
precioDeVenta = col6[1].find_all("span")
print("$$$$$$$$$$ Dolar Oficial $$$$$$$$$$$$")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("Precio de compra: "+precioDeCompra[0].text)
print("-----------------------------------------")
print("Precio de venta: "+precioDeVenta[0].text)
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")