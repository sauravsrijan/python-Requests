import requests

# list of endpoints to check.
ENDPOINTS = (
    '', 'ip', 'uuid', 'user-agent', 'headers', 'get', 'anything',
    'anything/:anything', 'encoding/utf8', 'gzip', 'deflate', 'brotli',
    '/stream/5', 'delay/2', 'status/200', 'html', 'robots.txt', 'deny',
    'cache', 'redirect/6', 'cookies', 'etag/:etag', 'cache/3', 'bytes/3',
    'stream-bytes/8', 'links/2', 'cookies/set?name=value', 'image/png',
    'image/jpeg', 'image/webp', 'image/svg', 'cookies/delete?name', 'xml')

OTHER_ENDPOINTS = ('post', 'patch', 'put', 'delete')
url = 'https://httpbin.org/'


def request_generator(opt, end):
    """Function to Check status code of request made."""
    api = url + end
    func = getattr(requests, opt)
    response = func(api)
    assert response.status_code == 200, "Failed for {}".format(api)
    print("success for {}".format(api))


# checking api endpoints.
def main():
	for second in ENDPOINTS:
		request_generator('get', second)
	for ep in OTHER_ENDPOINTS:
		request_generator(ep, ep)

if __name__ == "__main__":
	main()
'''FAILED_ENDPOINTS = [
    'redirect-to?url=foo', 'redirect-to?url=foo&status_code=307',
    'basic-auth/user/passwd', 'digest-auth/:qop/:user/:passwd/:algorithm',
    'digest-auth/:qop/:user/:passwd', 'range/1024?duration=s&chunk_size=code',
    'range/1024?duration=s&chunk_size=code',
    'drip?numbytes=n&duration=s&delay=s&code=code', 'image']
'''
