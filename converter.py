import requests
from bs4 import BeautifulSoup
try:
    source = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    source.raise_for_status()
    soup = BeautifulSoup(source.text,"html.parser")
    soup1 = str(soup)
    a = soup1.split("\"rates\":")
    b = a[1]
    c = b.strip("{}").split(",")
    dictionary1= {}
    for x in c:
        front= x[1:4]
        back= x[6:]
        dictionary1[front]= float(back)

    print("Enter the amount to convert:",end="")
    amount1 = int(input())
    for x in list(dictionary1.keys()):
         print(x,dictionary1[x])    
    print("Convert From:",end="")
    first = str(input()).upper()
    print("Convert To:",end="")   
    second= str(input()).upper()     

    if first != 'USD':
            amount2 = amount1 / dictionary1[first]
        # limiting the precision to 4 decimal places
    amount2 = round(amount1 * dictionary1[second], 4)
    print(amount2)

except Exception as e:
    print(e)    
