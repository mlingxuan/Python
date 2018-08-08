#会员中心造数据，先生成充值token
#只需修改"card_no"
import requests
import json
import random
'''
business_type_id说明：
Hotel(表示国内酒店)
IHotel （表示国际酒店）
Flight （表示国内机票）
IFlight（表示国际机票）
Train（表示火车票）
Bus（表示汽车票）
Sign（表示签到）

'''
def getToken():
    business_type_id_list = ['Hotel','IHotel','Flight','IFlight','Train','Bus']
    business_type_id_value = random.sample(business_type_id_list,1)   #随机取一个业务线的值
    url = "http://membergrade-api.vip.elong.com:8080/token/getToken"
    payload = '''{"card_no":"240000000318781072","business_type_id":"%s"}''' % (business_type_id_value[0])
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "276db546-1fab-68a1-5724-e0d5ecad5930"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    dic = json.loads(response.text)
    token = dic['token']
    value = [token,business_type_id_value[0]]
    print(value)
    return value

if __name__ == '__main__':
    getToken()

