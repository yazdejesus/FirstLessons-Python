import urllib
import urllib.request

try:
	pweb = 'http://www.pudim.com.br'
	web = urllib.request.urlopen(pweb)
except urllib.error.URLError:
	print('Website inacessível')
else:
	print('Site acessível')
	#print(web.read())
