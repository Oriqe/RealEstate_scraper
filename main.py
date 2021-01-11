from random import randint, random, shuffle
import json
import requests_html
from requests.exceptions import ChunkedEncodingError
import asyncio
from datetime import datetime
from pgadmin_functions import get_new_search_number, dict_arrange, insert_zillow
from request_functions import the_requesting_part, new_the_requesting_part, the_last_requesting_part
import all_address


async def request_info_gatherer(*args, **kwargs):
    """Disclosed"""
    return args


async def mainfunc(url, client_version, query_id, for_sale_query_id, rent_query_id, zpid, length, search_number):
    await asyncio.sleep((randint(length-3, length+5) * random()))
    try:

        answer = await the_last_requesting_part(zpid=zpid, clientversion=client_version, queryid=query_id, referer=url, operation="OffMarketDoubleScrollFullRenderQuery")
    except ChunkedEncodingError as e:
        print(e)
        print(url)
        return

    if '"countyId":null' in answer.text:
        print("AN EMPTY ONE", url)
        return

    try:
        new_answer = json.loads(answer.text)
    except json.decoder.JSONDecodeError as e:
        print(e)
        print(answer.text)
        return

    try:
        new_answer = new_answer["data"]["property"]

        house_details = dict_arrange(new_answer, search_number)
        print(house_details)
    except Exception as e:
        print(url)
        print(new_answer)
        print(e)
        return

    return house_details


async def initiator(urls):
    shuffle(urls)
    url = urls[0]

    queryid, rent_query_id, for_sale_query_id, clientv = await request_info_gatherer(url)

    last_index = 0
    index = 0
    start = datetime.now()
    search_number = get_new_search_number()

    while index < len(urls):
        last_index = index
        increment = randint(5, 15)
        if increment+index > len(urls):
            increment = len(urls) - index
        index += increment
        house_details = await asyncio.gather(*[mainfunc(i, client_version=clientv, query_id=queryid, for_sale_query_id=for_sale_query_id, rent_query_id=rent_query_id, zpid=i.split("/")[-2][:-5], length=increment, search_number=search_number) for i in urls[last_index:index]])

        insert_zillow(house_details)

    print("finished")

    end = datetime.now()
    ans = end - start
    print("total time: ", ans)


state = input("Enter state's shortened name: ")
county = input("Enter county name: ")
zip = input("Enter a 5 digit zip code: ")

all_address_url = f"https://www.zillow.com/browse/homes/{state}/{county}-county/{zip}/"

urls = asyncio.get_event_loop().run_until_complete(
    all_address.initiator(all_address_url))

asyncio.get_event_loop().run_until_complete(initiator(urls=urls))
