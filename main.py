import requests
import urllib
response = requests.get('https://api.jsonbin.io/b/59d0f30408be13271f7df29c').json()
access_token = response['access_token']

result = False
Base = 'https://api.instagram.com/v1/'

def comment(uid):
    media_id = get_media_id(uid)
    comment = raw_input("What comment you want to post?")
    payload = {"access_token": access_token, "text": comment}
    url = (Base + 'media/%s/comments') % (media_id)
    r = requests.post(url, payload).json()
    print r
    if r['meta']['code'] == 200:
        print "Comment Successfull."
    else:
        print 'Couldn\'t Comment please try again!'


def get_media_id(uid):
    media_choice = raw_input("Please input media ID:")
    media = int(media_choice) - 1
    request_url = (Base +'users/%s/media/recent/?access_token=%s') % (uid,access_token)
    info = requests.get(request_url).json()
    if info['meta']['code'] == 200:
        return info['data'][media]['id']
    else:
        print 'Couldn\'t get media id'

#Liking a post
def like(uid):
    media_id = get_media_id(uid)
    payload = {'access_token': access_token}
    url = Base + 'media/%s/likes' % (media_id)
    r = requests.post(url, payload).json()
    print r
    if r['meta']['code'] == 200:
        print "Post Liked Successfully."
    else :
        print 'Couldn\'t like please try again!'

#Downloading User media
def download(id,url):
    name = id + ".jpg"
    urllib.urlretrieve(url,name)
    print 'Your image has been downloaded successfully'

#Fetching Info of a user's public post
def u_post(uid):
    media_id = raw_input("Please input media ID:")
    media = int(media_id) + 1
    request_url = (Base + 'users/%s/media/recent/?access_token=%s') % (uid,access_token)
    print "your recent post's informations are :\n"
    info = requests.get(request_url).json()
    if info['meta']['code'] == 200:
        if len(info['data']) > 0:
            print "Caption : %s " % (info['data'][media]['caption'])
            print "Post Type : %s " % (info['data'][media]['type'])
            print "Tags : %s" % (info['data'][media]['tags'])
            print "Location : %s " % (info['data'][media]['location'])
            print "Number of Comments : %s " % (info['data'][media]['comments']['count'])
            print "Time: %s " % (info['data'][media]['created_time'])
            print "Link : %s " % (info['data'][media]['link'])
            print "Id: %s " % (info['data'][media]['id'])
            print "Number of likes : %s " % (info['data'][media]['likes']['count'])
            download(info['data'][media]['id'],info['data'][media]['images']['standard_resolution']['url'])
        else :
            print "Post doesn't exist"
    else:
        print "Error Occured"

#Getting Any self post's Info
def get_post():
    media_id = raw_input("Please input media ID:")
    request_url = (Base + 'users/self/media/recent/?access_token=%s') % (access_token)
    info = requests.get(request_url).json()
    media = int(media_id)
    if info['meta']['code'] == 200:
        print "Caption : %s " % (info['data'][media]['caption'])
        print "Post Type : %s " % (info['data'][media]['type'])
        print "Tags : %s " % (info['data'][media]['tags'])
        print "Location : %s " % (info['data'][media]['location'])
        print "Number of Comments : %s " % (info['data'][media]['comments']['count'])
        print "Time: %s " % (info['data'][media]['created_time'])
        print "Link : %s " % (info['data'][media]['link'])
        print "Id: %s " % (info['data'][media]['id'])
        print "Number of likes : %s " % (info['data'][media]['likes']['count'])
    else:
        # print 'Status code other than 200 received!'
        print "Wrong Information retrieved"


#User Profile
def u_profile(uname):
        print "Username : %s " % (uname['username'])
        print "Bio : %s " % (uname['bio'])
        print "Website : %s " % (uname['website'])
        print "Profile Picture : %s " % (uname['profile_picture'])
        print "Fullname : %s " % (uname['full_name'])
        print "ID : %s " % (uname['id'])

#Searching a User
def u_search():
    query = raw_input("Please enter the name of user :")
    request_url = (Base + 'users/search?q=%s&access_token=%s') % (query,access_token)
    search_result = requests.get(request_url).json()
    if search_result['meta']['code'] == 200:
        print "Id of the user is :"
        print search_result['data'][0]['id']
        return search_result['data'][0]
    else:
        print "Operation Failed !"
        return 0

#Fetching recent post information(self)
def r_post():
    request_url = (Base + 'users/self/media/recent/?access_token=%s') % (access_token)
    print "your recent post's informations are :\n"
    info = requests.get(request_url).json()
    if info['meta']['code'] == 200:
        print "Caption : %s " % (info['data'][0]['caption'])
        print "Post Type : %s " % (info['data'][0]['type'])
        print "Tags : %s " % (info['data'][0]['tags'])
        print "Location : %s " % (info['data'][0]['location'])
        print "Number of Comments : %s " % (info['data'][0]['comments']['count'])
        print "Time: %s " % (info['data'][0]['created_time'])
        print "Link : %s " % (info['data'][0]['link'])
        print "Id: %s " % (info['data'][0]['id'])
        print "Number of likes : %s " % (info['data'][0]['likes']['count'])
    else:
        # print 'Status code other than 200 received!'
        print "Wrong Information retrieved"


def self():
    request_url = (Base + 'users/self/?access_token=%s') % (access_token)
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


def start_bot():
    success = 0
    print "Please enter your choice from the given tasks: \n 1. Get your account's information \n 2. Get your recent post's information\n 3. Get any other user's info \n 4. Get any of your post's information \n 5. Get a user's post and download \n 6. Like a user's post\n 7. Commenmt on a post\n 8. Exit"
    choice = raw_input()
    if int(choice) > 0 and int(choice) < 10:
        # Tasks
        if choice == '1':
            self()
            return False
        elif choice == '2':
            r_post()
            return False
        elif choice == '3':
            search_result = u_search()
            if search_result == 0 :
                return False
            else :
                u_profile(search_result)
                return False
        elif choice == '4':
            get_post()
            return False
        elif choice == '5':
            search = u_search()
            if search == 0 :
                return False
            else :
                uid = search['id']
                u_post(uid)
                return False
            return False
        elif choice == '6':
            search = u_search()
            if search == 0:
                return False
            else:
                uid = search['id']
                like(uid)
                return False
            return False
        elif choice == '7':
            search = u_search()
            if search == 0:
                return False
            else:
                uid = search['id']
                comment(uid)
                return False
            return False
        elif choice == '8':
            return True

    else:
        print "You have entered a wrong choice please try again !"
        return False

while result == False :
    # Start Bot
    result = start_bot()
