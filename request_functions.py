from headers_functions import get_headers, new_get_headers, last_get_headers, optional
import requests_html


async def the_requesting_part(url):
    with requests_html.AsyncHTMLSession(browser_args=optional) as s:

        s.headers = get_headers()

        return await s.get(url)


async def new_the_requesting_part(url):
    with requests_html.AsyncHTMLSession(browser_args=optional) as s:
        s.headers = new_get_headers(url)

        return await s.get(url)


async def the_last_requesting_part(*args, **kwargs):
    """Disclosed"""
    pass
