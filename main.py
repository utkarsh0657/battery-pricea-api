import requests
from bs4 import BeautifulSoup
from flask import Flask,jsonify

app=Flask(__name__)

#Creating A Function for web scrapping
def scrape_price():

    url = "https://www.metal.com/Lithium-ion-Battery/202303240001"
    url_read = requests.get(url)
    soup = BeautifulSoup(url_read.content, 'html.parser')
    find_price = soup.find('span', {'class': 'strong___1JlBD priceDown___2TbRQ'})
    if find_price:
        price = find_price.text.strip()
        return price
    else:
        return None


## Create API for the this application
@app.route('/price', methods=['GET'])
def price():
    price = scrape_price()
    if price is not None:
        return jsonify({'Price': price})
    else:
        return jsonify({'error': "Url not working"})
    
if __name__ == '__main__':
    app.run()
