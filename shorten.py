import urllib, urllib2, config, json

def shorten(url):
    api_dest = "https://api-ssl.bitly.com/v3/shorten?"
    f = {'access_token' : config.BITLY_ACCESS_TOKEN, 'longUrl' : url, 'domain' : config.BITLY_DOMAIN}
    request = api_dest + urllib.urlencode(f)

    response = urllib2.urlopen(request)
    return get_url_from_bitly_response(response.read())

def http_encode(url):
    return urllib.quote_plus(url)

def get_url_from_bitly_response(html_response):
    data = json.loads(html_response)
    u_result = data['data']['url']
    return u_result.encode('utf-8')