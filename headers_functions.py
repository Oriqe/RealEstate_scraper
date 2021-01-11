

def new_get_headers(url):

    headers = {
        'content-type': 'application/javascript; charset=utf-8',
        'accept-encoding': 'gzip',
        'accept-language': 'en-US,en;q=0.5',
        'upgrade-insecure-requests': '*',
        "referrer": url
    }

    return headers


def get_headers():

    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'cache-control': 'max-age=0',
        'accept-encoding': 'deflate, br, gzip',
        'accept-language': 'en-US,en;q=0.5',
        'upgrade-insecure-requests': '1',
    }

    return headers


def last_get_headers(referer):

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'content-type': 'application/json',
        'cache-control': 'max-age=0',
        'referer': referer,
        'accept-encoding': 'deflate, br, gzip',
        'accept-language': 'en-US,en;q=0.5',
        'upgrade-insecure-requests': '1',
        # 'user-agent': user_agent
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0"
    }

    return headers


optional = [
    '--winhttp-proxy-resolver',
    '--disable-fine-grained-time-zone-detection',
    '--autoplay-policy=user-gesture-required',
    '--disable-background-networking',
    '--disable-background-timer-throttling',
    '--disable-backgrounding-occluded-windows',
    '--disable-breakpad',
    '--disable-client-side-phishing-detection',
    '--disable-component-update',
    '--disable-default-apps',
    '--disable-dev-shm-usage',
    '--disable-domain-reliability',
    '--disable-extensions',
    '--disable-features=AudioServiceOutOfProcess',
    '--disable-hang-monitor',
    '--disable-ipc-flooding-protection',
    '--disable-notifications',
    '--disable-offer-store-unmasked-wallet-cards',
    '--disable-popup-blocking',
    '--disable-print-preview',
    '--disable-prompt-on-repost',
    '--disable-renderer-backgrounding',
    '--disable-setuid-sandbox',
    '--disable-speech-api',
    '--disable-sync',
    '--disk-cache-size=33554432',
    '--hide-scrollbars',
    '--ignore-gpu-blacklist',
    '--metrics-recording-only',
    '--mute-audio',
    '--no-default-browser-check',
    '--no-first-run',
    '--no-pings',
    '--no-sandbox',
    '--no-zygote',
    '--password-store=basic',
    '--use-mock-keychain',
    '--disable-gl-drawing-for-tests',
    '--blink-settings=imagesEnabled=false'
]
