import requests
import urllib
response = requests.get('https://api.jsonbin.io/b/59d0f30408be13271f7df29c').json()
access_token = response['access_token']

result = False
Base = 'https://api.instagram.com/v1/'

#User Profile
def u_profile():


#Searching a User
def u_search():
    query = raw_input("Please enter the name of user :")
    request_url = (Base + 'users/search?q=%s&access_token=%s') % (query,access_token)
    search_result = requests.get(request_url).json()
    print "Search Result is :"
    print search_result['data'][0]['id']
    return search_result['data'][0]['id']

#Fetching recent post information
def r_post():
    request_url = (Base + 'users/self/media/recent/?access_token=%s') % (access_token)
    print "your recent post's informations are :\n"
    info = requests.get(request_url).json()
    print info
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


def start_bot():
    success = 0
    print "Please enter your choice from the given tasks: \n 1. Get your account's information \n 2. Get recent post's information\n 3. Get another user's info \n 4. Check negative comments\n 5. Remove negative comments\n 6. Exit"
    choice = raw_input()
    if int(choice) > 0 and int(choice) < 7:
        # Tasks
        if choice == '1':
            self()
            return False
        elif choice == '2':
            r_post()
            return False
        elif choice == '3':
            search_result = u_search()
            u_profile(search_result)
            return False
        elif choice == '4':
            check()
            return False
        elif choice == '5':
            remove_comm()
            return False
        elif choice == '6':
            return True

    else:
        print "You have entered a wrong choice please try again !"
        return False

while result == False :
    # Start Bot
    result = start_bot()
