import http.client
import urllib.parse
import re
import json
import requests
import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("url")
url = {"content":["https://www.tiktok.com/@slow_mm/video/7002232802255162626","https://www.tiktok.com/@slow_mm/video/6998112477338750210","https://www.tiktok.com/@slow_mm/video/6997746370501168386","https://www.tiktok.com/@slow_mm/video/6995167056098348289","https://www.tiktok.com/@slow_mm/video/6991789193911438594","https://www.tiktok.com/@slow_mm/video/6989566637837995266","https://www.tiktok.com/@slow_mm/video/6987707632442264833","https://www.tiktok.com/@slow_mm/video/6985860791606054145","https://www.tiktok.com/@slow_mm/video/6985111240414727425","https://www.tiktok.com/@slow_mm/video/6985106960832040193","https://www.tiktok.com/@slow_mm/video/6982514541196365058","https://www.tiktok.com/@slow_mm/video/6982170284270882049","https://www.tiktok.com/@slow_mm/video/6981042151807257858","https://www.tiktok.com/@slow_mm/video/6979172282929286401","https://www.tiktok.com/@slow_mm/video/6978813770764209410","https://www.tiktok.com/@slow_mm/video/6978812422496783618","https://www.tiktok.com/@slow_mm/video/6977689702824414466","https://www.tiktok.com/@slow_mm/video/6977503701611138306","https://www.tiktok.com/@slow_mm/video/6976234043289521410","https://www.tiktok.com/@slow_mm/video/6976218754845773058","https://www.tiktok.com/@slow_mm/video/6976180146885774593","https://www.tiktok.com/@slow_mm/video/6976171514051742978","https://www.tiktok.com/@slow_mm/video/6975835200722996481","https://www.tiktok.com/@slow_mm/video/6975469045407681794","https://www.tiktok.com/@slow_mm/video/6975468087348874497","https://www.tiktok.com/@slow_mm/video/6975071662421167362","https://www.tiktok.com/@slow_mm/video/6974695117898763522","https://www.tiktok.com/@slow_mm/video/6972466102727085318","https://www.tiktok.com/@slow_mm/video/6972465537804684549","https://www.tiktok.com/@slow_mm/video/6972465331407310085","https://www.tiktok.com/@slow_mm/video/6972465102700170502","https://www.tiktok.com/@slow_mm/video/6972434687037885698","https://www.tiktok.com/@slow_mm/video/6972434560982207745","https://www.tiktok.com/@slow_mm/video/6972434409026784514"],"d":"2021-08-31T09:00:19.241Z"}

def getCookie():
    conn = http.client.HTTPSConnection("dltik.com")
    payload = ''
    conn.request("GET", "/?hl=vi", payload)
    res = conn.getresponse()
    if res.status == 200:
        cookie = res.headers['Set-Cookie']
        html = res.read().decode("utf-8")
        token = ''
        match = re.search(r"<input name=\"__RequestVerificationToken\"[^>]*value=\"([^ ]+)\"", html, re.MULTILINE)
        if match:
            token = match.group(1)
        return [cookie, token]
    return ''

def getDownloadUrl(url, cookie,i):
    conn = http.client.HTTPSConnection("dltik.com")
    cookies = cookie[0].split(';')[0].split('=')
    payload = 'm=getlink&url=' + urllib.parse.quote(url, safe='') + '&__RequestVerificationToken=' + urllib.parse.quote(cookie[1], safe='')
    headers = {
        'Cookie': cookies[0] + '=' + cookies[1] + ';',
        'content-type': 'application/x-www-form-urlencoded'
    }
    conn.request("POST", "/?hl=vi", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(json.dumps(json.loads(data.decode("utf-8")), indent=4, sort_keys=True))
    datajs =json.loads(data.decode("utf-8"))
    # print(datajs)
    # urls='https://v39-as.tiktokcdn.com/211e0df35b3b82b259aa785fa68fcc3b/612a0f83/video/tos/useast2a/tos-useast2a-pve-0037-aiso/af8bdb1c3d3c4df0b64dc6ba35285337/?a=1233&br=1602&bt=801&cd=0%7C0%7C0&ch=0&cr=0&cs=0&cv=1&dr=0&ds=6&er=&ft=98ZmAekh4kag3&l=20210828042700010245173118548D78DE&lr=all&mime_type=video_mp4&net=0&pl=0&qs=0&rc=M3U2NWU6ZmhrNzMzZjgzM0ApZmQ7aTQ2NTw0N2Q4PDU7aGctLWRxcjRvLWdgLS1kL2NzczNgXjFjNWBhYjYuNV8tMDA6Yw%3D%3D&vl=&vr='
    # r = requests.get(str(datajs["data"]["destinationUrl"]))
    r = requests.get(datajs["data"]["destinationUrl"])
    name = str(datajs["data"]["desc"])
    cleanString = re.sub('\W+', '', name)
    print(cleanString)
    with open('download/'+str(i) + cleanString +  '.mp4' , 'wb') as fd:
          fd.write(r.content)
if __name__ == '__main__':
    # args = parser.parse_args()
    i = 0
    cookie = getCookie()
    for url in url["content"]:
        getDownloadUrl(url, cookie,i)
        i=i+1


