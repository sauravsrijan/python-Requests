import requests

end_p = ['', 'ip', 'uuid', 'user-agent', 'headers', 'get', 'anything', 'anything/:anything', 
		 'encoding/utf8', 'gzip', 'deflate', 'brotli', '/stream/5', 'delay/2',
		 'status/200','html', 'robots.txt', 'deny', 'cache','redirect/6',
		 'cookies', 'etag/:etag', 'cache/3', 'bytes/3', 'stream-bytes/8', 'links/2',
		 'cookies/set?name=value','image/png', 'image/jpeg', 'image/webp', 'image/svg',
		 'cookies/delete?name','xml']
for second in end_p:
	res = requests.get('https://httpbin.org/'+second)
	assert res.status_code==200, "Status code not equal to 200 for endpoint %s" %(second)
	print ("success for the endpoint '%s'. Going for next one now. \n" %(second))

res = requests.post('https://httpbin.org/post')
assert res.status_code == 200, "Failed"
print ("successfully posted a request.")

res = requests.patch('https://httpbin.org/patch')
assert res.status_code == 200, "Failed"
print ("Patch Successfull.")

res = requests.put('https://httpbin.org/put')
assert res.status_code == 200, "Failed"
print ("successfull for endpoint 'put'.")

res = requests.delete('https://httpbin.org/delete')
assert res.status_code == 200, "Failed"
print ("Delete request successfull.")

failed_endP=['redirect-to?url=foo','redirect-to?url=foo&status_code=307', 'basic-auth/user/passwd',
		'digest-auth/:qop/:user/:passwd/:algorithm', 'digest-auth/:qop/:user/:passwd','range/1024?duration=s&chunk_size=code',
		'range/1024?duration=s&chunk_size=code', 'drip?numbytes=n&duration=s&delay=s&code=code', 'image', ]