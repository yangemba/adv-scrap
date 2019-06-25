import asyncio
import concurrent.futures
import requests
import time
import bs4

from request_sender import scrapp

massive = ['https://premier.ua/zhilaia-nedvizhimost/prodazha-1-komn-kv-?page=',
           'https://premier.ua/zhilaia-nedvizhimost/kvartiry-v-novostroykakh-?page=',
           'https://premier.ua/zhilaia-nedvizhimost/prodazha-2-komn-kv-?page=',
           'https://premier.ua/zhilaia-nedvizhimost/prodazha-3-komn-kv-?page=',
           'https://premier.ua/zhilaia-nedvizhimost/prodazha-4-komn-kv-?page=',
           'https://premier.ua/zhilaia-nedvizhimost/prodazha-gostinok-komnat?page=',
           'https://premier.ua/zhilaia-nedvizhimost/uchastki-v-kharkovskoy-oblasti?page=',
           'https://premier.ua/zhilaia-nedvizhimost/prodazha-domov-v-kharkove?page=',
           'https://premier.ua/zhilaia-nedvizhimost/prodazha-domov-v-prigorode?page=',
           'https://premier.ua/zhilaia-nedvizhimost/doma-v-kharkovskoy-oblasti?page=']


# async def main():
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
#
#         loop = asyncio.get_event_loop()
#         futures = [
#             loop.run_in_executor(executor, requests.get,f'https://premier.ua/zhilaia-nedvizhimost/prodazha-1-komn-kv-?page={i}'
#             )
#             for i in range(100)
#         ]
#         for response in await asyncio.gather(*futures):
#             print(response, str(start - time.time()))
#             soup = bs4.BeautifulSoup(response.text, "html.parser")
#             with open("test.txt", "a") as file:
#                 file.write(str(soup) + '\n')
#
#

start = time.time()
for elemnt in massive:
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(scrapp(f'{elemnt}'))

print(str(time.time() - start))
