import requests
import time

# Global variables
Api_key ='2d3228bc-c890-4a65-9ee3-3f23f5e965c9'
bot_key ='2062955732:AAHuc-XPOMqO04L_Dyq6zqOIvKvWATpBkiI'
chat_id ='1405192730'
limit = 50000
time_interval = 5

def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    """ parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
        } """
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': Api_key,
        }
    respone=requests.get(url=url,headers=headers).json()
    BTC_value=respone['data'][0]['quote']['USD']['price']
    return BTC_value
print(get_price())

price=get_price()

def send_update(chat_id,msg):
    url=f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    

send_update(chat_id,f"the botcoin value is {price}")
 #### i have a problem in the function below but it works 
def mainFun():
    while True:
        price = get_price()
        if price > limit:
            send_update(chat_id,f"The Bitcoin price now is :{price} ")
        time.sleep(time_interval)   
mainFun()

