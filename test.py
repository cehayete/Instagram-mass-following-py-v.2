from InstagramAPI import InstagramAPI

api = InstagramAPI('apaemfortest', '132424qwe')
api.login()

r = api.s.get(api.LastJson['challenge']['url'])
print(r.text)
