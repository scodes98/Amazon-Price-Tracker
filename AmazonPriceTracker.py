
#  -- AMAZON PRICE TRACKER --
#  https://github.com/scodes98

import requests
from bs4 import BeautifulSoup
import re
import time
import smtplib

url = input("Enter product URL: ")
headers = {
    "User-Agent": "--Your user agent--"}  # Enter your respective user agent
desired_price = float(input("Enter your desired budget price: "))


def trackPrice():
    price = float(getPrice())
    if price > desired_price:
        print("Item price out of budget! :(")
    else:
        print("Item price is now in your desired budget! :)")
        sendMail()


def getPrice():
    global title
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = ''.join((re.findall(r'\d+\.*\d*', price)))
    return converted_price


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Make sure you enable "Allow less secure apps" in your respective google account
    # OR Enable Two-Factor Authentication, and generate a new app password for Gmail

    # Enter your respective email and password
    server.login('--email@gmail.com--', '--password--')

    subject = 'PRICE FELL DOWN!'
    body = title+" is now in your desired budget!\nCheck link: "+url
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '--sender@gmail.com--',
        '--receiver@gmail.com--',
        msg
    )

    print('Email has been sent!')
    server.quit()


if __name__ == "__main__":
    while True:
        trackPrice()
        time.sleep(60)  # Run script after every 60 seconds

#  -- AMAZON PRICE TRACKER --
#  https://github.com/scodes98
