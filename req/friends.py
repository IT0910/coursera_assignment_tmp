import requests
import operator
import datetime
from collections import Counter

ACCESS_TOKEN = '87eddcf687eddcf687eddcf6a587860faf887ed87eddcf6dad86715468077f029dc8047'
def calc_age(uid):
    params = {"v":5.71,"access_token": ACCESS_TOKEN, "user_ids":uid, "fields":"id"}

    r = requests.get("https://api.vk.com/method/users.get", params= params)
    user = r.json()
    params = {"v": 5.71, "access_token": ACCESS_TOKEN, "user_id": user['response'][0].get('id'), "fields": "bdate"}

    # params = {"v": 5.71, "access_token": ACCESS_TOKEN, "user_id": int(12520148, "fields": "bdate"}
    fr =  requests.get("https://api.vk.com/method/friends.get", params = params)
    friends = fr.json()['response'].get("items",[])
    year = datetime.datetime.now().year

    friends = [year - datetime.datetime.strptime(i.get('bdate'), '%d.%m.%Y').year for i in friends if i.get('bdate') and i.get('bdate').count('.')>1]
    friend_list = sorted(dict(Counter(friends)).items(),key = operator.itemgetter(0))
    friend_list = sorted(friend_list, key=operator.itemgetter(1), reverse= True)
    return friend_list
if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)