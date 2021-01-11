
from random import randint, random
import requests_html
import asyncio
from requests_html import HTML
from headers_functions import optional


def get_headers(referer):  # referer is url shortened by zip-code
    referer = "/".join(referer.split("/")[:-2])
    headers = {

        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

        'cache-control': 'max-age=0',

        'referer': referer,

        'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
        'upgrade-insecure-requests': '1',
    }
    return headers


async def the_requesting_part(url, length):
    with requests_html.AsyncHTMLSession(browser_args=optional) as s:

        s.headers = get_headers(url)
        await asyncio.sleep((randint(1, length*10) * random() + (length * 10 * random()))*1.618)
        ans = await s.get(url)
        new_ans = HTML(html=ans.text)

        if "captcha" in new_ans.text:
            print(new_ans.text)
            raise ImportError

        return new_ans


async def the_requesting_part_quick(url):
    with requests_html.AsyncHTMLSession(browser_args=optional) as s:

        s.headers = get_headers(url)
        return await s.get(url)


async def main(*args, **kwargs):
    """Disclosed"""
    pass


async def initiator(url):
    all_addresses = await main(url)
    return all_addresses
