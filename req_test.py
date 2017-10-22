import requests

# list of endpoints to check.
get_end_p = [
    '', 'ip', 'uuid', 'user-agent', 'headers', 'get', 'anything',
    'anything/:anything', 'encoding/utf8', 'gzip', 'deflate', 'brotli',
    '/stream/5', 'delay/2', 'status/200', 'html', 'robots.txt', 'deny',
    'cache', 'redirect/6', 'cookies', 'etag/:etag', 'cache/3', 'bytes/3',
    'stream-bytes/8', 'links/2', 'cookies/set?name=value', 'image/png',
    'image/jpeg', 'image/webp', 'image/svg', 'cookies/delete?name', 'xml']

other_endP = ['post', 'patch', 'put', 'delete']
url = 'https://httpbin.org/'


def req_gen(opt, end):
    """Function to Check status code of request made."""
    if opt is "get":
        res = requests.get(url+end)
    elif opt is "post":
        res = requests.post(url+end)
    elif opt is "patch":
        res = requests.patch(url+end)
    elif opt is "put":
        res = requests.put(url+end)
    elif opt is "delete":
        res = requests.delete(url+end)
    assert res.status_code == 200, "Failed for {}".format(url+end)
    print("success for {}".format(url+end))


# checking api endpoints.
for second in get_end_p:
    req_gen('get', second)
for eP in other_endP:
    req_gen(eP, eP)

failed_endP = [
    'redirect-to?url=foo', 'redirect-to?url=foo&status_code=307',
    'basic-auth/user/passwd', 'digest-auth/:qop/:user/:passwd/:algorithm',
    'digest-auth/:qop/:user/:passwd', 'range/1024?duration=s&chunk_size=code',
    'range/1024?duration=s&chunk_size=code',
    'drip?numbytes=n&duration=s&delay=s&code=code', 'image']
