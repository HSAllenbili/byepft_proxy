import requests
import random
from requests_toolbelt.multipart.encoder import MultipartEncoder
from tools.version import proxy_version, miniapp_ver, miniapp_ver_str


def headers_1(length, token, tenant, ua):
    headers = {"Host": "pft.ujs.edu.cn",
               "Connection": "keep-alive",
               "Content-Length": length,
               "tenant": tenant,
               "miniappversion": miniapp_ver_str,
               "content-type": "application/json;charset=utf-8",
               "token": token,
               "Accept-Encoding": "gzip,compress,br,deflate",
               "User-Agent": ua,
               "Referer": "https://servicewechat.com/wx482e15722a952deb/" + miniapp_ver + "/page-frame.html"}
    return headers


def headers_2(token, tenant, ua):
    headers = {"Host": "pft.ujs.edu.cn",
               "Connection": "keep-alive",
               "tenant": tenant,
               "miniappversion": miniapp_ver_str,
               "content-type": "application/json",
               "token": token,
               "Accept-Encoding": "gzip,compress,br,deflate",
               "User-Agent": ua,
               "Referer": "https://servicewechat.com/wx482e15722a952deb/" + miniapp_ver + "/page-frame.html"}
    return headers


def headers_3(length, token, tenant, ua, boundary):
    headers = {"Host": "pft.ujs.edu.cn",
               "Connection": "keep-alive",
               "Content-Length": length,
               "token": token,
               "tenant": tenant,
               "miniappversion": miniapp_ver_str,
               "Accept-Encoding": "gzip,compress,br,deflate",
               "User-Agent": ua,
               "Content-Type": "multipart/form-data; boundary=" + boundary,
               "Referer": "https://servicewechat.com/wx482e15722a952deb/" + miniapp_ver + "/page-frame.html"}
    return headers


def headers_4(length, token, tenant, ua):
    headers = {"Host": "pft.ujs.edu.cn",
               "Connection": "keep-alive",
               "Content-Length": length,
               "tenant": tenant,
               "miniappversion": miniapp_ver_str,
               "content-type": "application/json;charset=utf-8",
               "token": token,
               "Accept-Encoding": "gzip,compress,br,deflate",
               "User-Agent": ua,
               "Referer": "https://servicewechat.com/wx482e15722a952deb/" + miniapp_ver + "/page-frame.html"}
    return headers


def get(url, headers):
    session = requests.Session()
    session.headers.clear()
    session.headers.update(headers)
    res = session.get(url=url)
    return res


def post(url, headers, data):
    session = requests.Session()
    session.headers.clear()
    session.headers.update(headers)
    res = session.post(url=url, data=data)
    return res


def get_version():
    ver_json = {"status": 0, "miniapp_ver": miniapp_ver, "miniapp_ver_str": miniapp_ver_str,
                "proxy_version": str(proxy_version)}
    return ver_json


def list_rule(token, tenant, ua):
    res = get("https://pft.ujs.edu.cn/api/miniapp/exercise/listRule", headers_2(token, tenant, ua))
    return res.json()


def start_img(token, tenant, ua, img):
    file_name = "tmp_" + "".join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 32)) + ".jpg"
    boundary = "WABoundary+" + "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 16)) + "WA"
    data = MultipartEncoder(fields={'file': (file_name, img, 'image/jpeg')}, boundary=boundary)
    res = post("https://pft.ujs.edu.cn/api/miniapp/exercise/uploadRecordImage",
               headers_3(str(data.len), token, tenant, ua, boundary), data)
    return res.json()


def start_record(token, tenant, ua, data):
    res = post("https://pft.ujs.edu.cn/api/exercise/exerciseRecord/saveStartRecord",
               headers_4(str(len(data)), token, tenant, ua), data)
    return res.json()


def end_img(token, tenant, ua, img):
    file_name = "tmp_" + "".join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 32)) + ".jpg"
    boundary = "WABoundary+" + "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 16)) + "WA"
    data = MultipartEncoder(fields={'file': (file_name, img, 'image/jpeg')}, boundary=boundary)
    res = post("https://pft.ujs.edu.cn/api/miniapp/exercise/uploadRecordImage2",
               headers_3(str(data.len), token, tenant, ua, boundary), data)
    return res.json()


def end_record(token, tenant, ua, data):
    res = post("https://pft.ujs.edu.cn/api/exercise/exerciseRecord/saveRecord",
               headers_4(str(len(data)), token, tenant, ua), data)
    return res.json()


def my_record(token, tenant, ua):
    data = "{}"
    res = post("https://pft.ujs.edu.cn/api/miniapp/exercise/getTotalRecord",
               headers_1(str(len(data)), token, tenant, ua), data)
    return res.json()


def record_detail(token, tenant, ua, data):
    res = post("https://pft.ujs.edu.cn/api/miniapp/exercise/miniApprecordInfo",
               headers_1(str(len(data)), token, tenant, ua), data)
    return res.json()


def get_info(token, tenant, ua):
    res = get("https://pft.ujs.edu.cn/api/miniapp/studentMini/getStudentInfo", headers_2(token, tenant, ua))
    return res.json()
