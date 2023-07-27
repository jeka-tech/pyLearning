from bs4 import BeautifulSoup
import requests

url = 'https://rp5.ru/Погода_в_Самаре,_Самарская_область'

# GET / HTTP/1.1\r\nHost: 192.168.43.168:8000\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2527 Yowser/2.5 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: ru,en;q=0.9\r\n\r\n

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

temp = soup.find('div', id = 'forecastShort-content')

for match in temp.findAll('span', class_ = "t_1"):
        match.clear()

print(temp.text)