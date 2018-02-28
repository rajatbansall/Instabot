import requests
response = requests.get('https://api.jsonbin.io/b/59d0f30408be13271f7df29c').json()
access_token = response['access_token']

Base = 'https://api.instagram.com/v1/'

def self():
    request_url = (Base + 'users/self/?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        print "Username : %s " % (user_info['data']['username'])
        print "Bio : %s " % (user_info['data']['bio'])
        print "Website : %s " % (user_info['data']['website'])
        print "Profile Picture : %s " % (user_info['data']['profile_picture'])
        print "Fullname : %s " % (user_info['data']['full_name'])
        print "Followed By : %s " % (user_info['data']['counts']['media'])
        print "Follows : %s " % (user_info['data']['counts']['follows'])
    else:
        #print 'Status code other than 200 received!'
        print "Wrong Information retrieved"


self()
