import os
import urllib
import requests

class Downloader():
    def __init__(self,save_path):
         self.save_path = save_path


    def download(self,url,MusicName):
        # self.requst.save(self.url,self.save_path)
        print(url)
        req = requests.get(url,stream=True)
        with open(os.path.join("Music",MusicName+".mp3"), "wb") as f:
            for chunk in req.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)