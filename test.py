import urllib2

url = "http://api.reimaginebanking.com/accounts/5bd46141322fa06b67793ea2/purchases?key=351388794358970b8ed7ec1790b2004a"
content = urllib2.urlopen(url).read()

print content
