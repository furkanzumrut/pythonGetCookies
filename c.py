import cookielib
import urllib2

cookies = cookielib.LWPCookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
    ]
opener = urllib2.build_opener(*handlers)

def get_digits(str1):
    c = ""
    for i in str1:
        if i.isdigit():
            c += i
    return c  

def fetch(uri):
    req = urllib2.Request(uri)
    return opener.open(req)

def dump():
    for cookie in cookies:
        print cookie.name, cookie.value


uri = 'http://www.facebook.com/'
res = fetch(uri)
opener.close()
#dump()
for cookie in cookies:
	print len(get_digits(cookie.value))
	print cookie.value
