import configparser
import json
import requests
import subprocess


config = configparser.ConfigParser() 
config.read("config.ini")

APiKey5Sim = config['Token']['Key5Sim']

def send_get(url, param=None, headers=None):
    x = requests.get(url, json=param, headers=headers)
    #print(x.text)
    try:
        return json.loads(x.text)
    except:
        return x.text

rd = {
  "id": 11631253,
  "created_at": "2018-10-13T08:13:38.809469028Z",
  "phone": "+79000381454",
  "product": "vkontakte",
  "price": 21,
  "status": "RECEIVED",
  "expires": "2018-10-13T08:28:38.809469028Z",
  "sms": [
      {
        "id":3027531,
        "created_at":"2018-10-13T08:20:38.809469028Z",
        "date":"2018-10-13T08:19:38Z",
        "sender":"VKcom",
        "text":"VK: 09363 - use this code to reclaim your suspended profile.",
        "code":"09363"
      }
  ],
  "forwarding": 'false',
  "forwarding_number": "",
  "country":"russia"
}


def api(num, action, city=None, oper=None, apps=None, id=None):
    
    if num in [1, '1']:
        token = APiKey5Sim
        headers = {
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json',
        }
        if action == 'balance':
            return send_get('https://5sim.net/v1/user/profile', None, headers)
        elif action == 'all':
            country = 'any'
            operator = 'any'
            return send_get('https://5sim.net/v1/guest/products/' + country + '/' + operator, None, headers)

        elif action == 'buy':
            return send_get('https://5sim.net/v1/user/buy/activation/'+ city + '/' + oper + '/' + apps, None, headers)
        
        elif action == 'code':
            return send_get('https://5sim.net/v1/user/check/' + str(id), None, headers)
        
        else:
            return False
    return False


def send_shell(*argv):
    subprocess.Popen(argv)
'''u = send_get('https://5sim.net/v1/user/check/367086045', None, headers)

sms = u['sms']
for i in sms:
    print(i['text'], i['code'])'''