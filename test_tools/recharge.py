#会员中心消费明细造数据,订单经验值充值接口
#只需修改"card_no"，"mobile"，"device_id"字段
import requests
from test_tools import get_token
import random
def recharge():
    times = int(input('请输入需要造多少条数据：'))
    order_no = random.randint(100,10000)#订单号初始值每次随机取
    while times > 0:
        url = "http://membergrade-api.vip.elong.com:8080/order/exp/recharge"
        return_value = get_token.getToken()
        token = return_value[0]
        business_type_id = return_value[1]
        print(token,business_type_id)
        dic = {'Hotel': 'hotel_op_obtain_exp',
               'IHotel': 'ihotel_op_obtain_exp',
               'Flight': 'flight_op_obtain_exp',
               'IFlight': 'iflight_op_obtain_exp',
               'Train': 'train_op_obtain_exp',
               'Bus': 'bus_op_obtain_exp'}  # business_type_id值对应的exp_op_id值
        payload = '''{
                "token":"%s",
                "card_no":"240000000318781072",
                "proxy":"AP0011893",
                "business_type_id":"%s",
                "order_no":"%s",
                "order_money":"%d",
                "order_date":"2018-06-11 10:00:00",
                "order_modify_time":"1528682400",
                "exp_op_id":"%s",
                "illustration":"test",
                "request_ip":"192.168.3.13",
                "client_ip":"192.168.3.13",
                "mobile":"18511859096",
                "device_id":"08D26EC4-E82A-4B24-B09B-FC9CD055D217"
            }'''% (token,business_type_id,order_no,1,dic[business_type_id])

        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-ca4529533799che",
            'Postman-Token': "c167c942-7421-b78f-b1b3-903b4b708738"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        order_no += 1
        times -= 1
        print(response.text)
        #print(order_no)

if __name__ == '__main__':
    recharge()