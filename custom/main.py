import asyncio
import concurrent.futures
import requests
import time
import bs4


async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get,f'http://www.example.com/{i}.html'
            )
            for i in range(100)
        ]
        for response in await asyncio.gather(*futures):
            print(response, str(start - time.time()))
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            with open("test.txt", "a") as file:
                file.write(str(soup) + '\n')


loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(main())


print('\n\n\n')
print(str(time.time() - start))
