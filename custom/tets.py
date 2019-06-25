import bs4
import requests
import asyncio
import concurrent.futures


with open("settings.txt", 'r') as file:
    file.seek(0)
    text = file.read().replace(' ', '')
    LIST_TO_PARSE = text.split(',')


def get_lin_list(url):
    list_names2 = []
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # self.name_area = self.soup.find(id="CategoryHeader120")
    # self.name = self.soup.find(id='headerItema')
    list = [f"https://premier.ua/{x.attrs['href']}" for x in soup.select('.catlist a')]
    # list_names = [f"{x.attrs['title']}" for x in soup.select('.catlist a')]

    # for x in list_names:
    #     k = x.replace(',', ' ')
    #     list_names2.append(k)
    dict_linksname = list[1:]
    return dict_linksname


'''    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

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
                file.write(str(soup) + '\n') '''

all_parse_list = []


# for link in LIST_TO_PARSE:
#     temp = get_lin_list(link)
#     all_parse_list += temp

print(len(all_parse_list))
