import requests
r = requests.get('https://github.com', auth=('user','pass'))

code = r.status_code
print(code)

header = r.headers
print(header)

encode = e.encoding
print(encode)

text = r.text
print(text)

json = r.json()
print(json)
