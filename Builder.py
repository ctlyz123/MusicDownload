import requests
import re
import json
from urllib.parse import quote
from Utils import loadconfig


class Builder():
    def __init__(self,configpath):
        self.urlconfig = loadconfig(configpath)["Url"]
    def create(self,music_name):
# ---------------------------------------fetch music code-------------------------------------------------------
#         print(music_name)
        search_url = "%s/?q=%s"%(self.urlconfig["Main_url"],quote(music_name))
        # print(search_url)
        content = requests.get(search_url).content
        Music_code = re.findall("vi\/(.*)\/maxresdefault\.jpg",str(content))[0]

# ---------------------------------------fetch middle token-------------------------------------------------------
# demo /download?v=b5Zay_Hd_7Q&t=f31098a3863c2da153da11f40d29a85f&r=https%3A%2F%2Fmp3pro.xyz%2Fb5Zay_Hd_7Q&b=320
        mid_url = "%s/%s"%(self.urlconfig["Mid_url"],Music_code)
        content = requests.get(mid_url).content
        m_token = re.findall('token":"(.*)","verify"',str(content))[0]
        # print(m_token)


# ---------------------------------------fetch final token-------------------------------------------------------
        data = {
            "purpose": "audio",
            "token": m_token,
        }
        req = requests.post("https://mp3pro.xyz/ajax",data=data)
        # print(req.content)
        res_json = json.loads(bytes.decode(req.content))
        code_token = res_json["audio"]
# ---------------------------------------fetch music link-------------------------------------------------------

        data = {
        "purpose":"download",
        "token":code_token,
        "f":0,
        "d":0,
        "b":320,
        "c":1,
        "r":"https://mp3pro.xyz/{}".format(code_token.split(":")[0])
        }
        req = requests.post("https://mp3pro.xyz/ajax", data=data)
        res_json = json.loads(bytes.decode(req.content))
        # print(res_json)
        return res_json['mp3url']

if __name__ == '__main__':
    builder = Builder("Config/config.json")
    print(builder.create("Yummy"))