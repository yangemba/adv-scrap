import asyncio
import concurrent.futures
import requests
import time
import bs4


async def scrapp(link):

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get, f'{link}{i}'
            )
            for i in range(10)
        ]
        for response in await asyncio.gather(*futures):
            # print(response, str(start - time.time()))
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            with open(f"{len(link)}.txt", "a") as file:
                file.write(str(soup) + '\n')

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     start = time.time()
#     loop.run_until_complete(scrapp('https://premier.ua/zhilaia-nedvizhimost/prodazha-1-komn-kv-?page='))
#
#
#     print('\n\n\n')
#     print(str(time.time() - start))
