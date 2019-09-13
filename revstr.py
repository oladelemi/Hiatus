import urllib2

link = "http://www.chiquitooenterprise.com/password"
# Missing a whole chunk of code here!

pwdString = urllib2.urlopen(link)
pwdString= pwdString.read()
print pwdString

def revstr(str) :
	""" recursive function to reverse a string """

	str_len = len(str)
	if str_len == 1 :
		return str

	new = str[str_len-1] + revstr(str[:str_len-1])
	return new

revString = revstr(pwdString)
answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = urllib2.urlopen(answer)
response = response.read()
print(response)
