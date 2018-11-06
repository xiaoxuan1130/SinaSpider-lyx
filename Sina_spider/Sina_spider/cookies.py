# conding:utf-8
import requests
from lxml import etree
s = requests.session()
import json

def get_it_execution():
    result = {}
    loginurl = "https://account.chsi.com.cn/passport/login"
    r = s.get(loginurl, verify=False)
    dom = etree.HTML(r.content.decode("utf-8"))

    try:
        result["lt"] = dom.xpath('//input[@name="lt"]')[0].get("value")
        result["execution"] = dom.xpath('//input[@name="execution"]')[0].get("value")
        print(result)
    except:
        print("----------")
    return result

def login(result, user, psw):
    loginurl = "https://account.chsi.com.cn/passport/login"
    body = {
        "username": user,
        "password": psw,
        "rememberMe": "true",
        "lt": result["lt"],
        "execution": result["execution"],
        "_eventId": "submit"
    }
    r4 = s.post(loginurl, data=body, verify=False)
    return s.cookies.get_dict()

def iotLogin(user,psw):
    loginurl="http://www.iotcn.org.cn/wp-admin/admin-ajax.php"
    body = {
        "action": "ajaxlogin",
        "username": user,
        "password": psw,
        "email":'',
        "password2":'',
        "security":'af7c8e82c6'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }
    r4 = s.post(loginurl,headers=headers,data=body, verify=False)
    return s.cookies.get_dict()

def getCookies(myinfo):
    for elem in myinfo:
        account = elem['no']
        password = elem['psw']
        ##result = get_it_execution()
        cookie = iotLogin(account, password)
        return cookie


myinfo = [
    {'no': '1024046894@qq.com', 'psw': ''}
]

cookies=getCookies(myinfo)
