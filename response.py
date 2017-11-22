from urllib2 import Request, urlopen

headers = {
  'Authorization': 'Basic Um9iZXJ0UGF1bHNvbjoxMjM0NTY3OA==',
  'X-Api-Token': 'TheSecretTokenWeSentInEmail'
}
request = Request('http://www.rainsoul-hu.com/1')

response_body = urlopen(request).read()
print response_body