from Utils import readfile
from Utils import logging
from ThreadDownload import ThreadDownload
from concurrent.futures import ThreadPoolExecutor

class Controller():
    def     __init__(self,list_filename):
        self.list_filename = list_filename

    def init(self,downloader,builder):
        logging.info("[+] Download Initialing")
        self.downloader = downloader
        self.builder = builder
        return self

    def AutoDownload(self):
        MusicsName = readfile(self.list_filename)
        logging.info("[+] Begin Download")
        threads = []
        threadPool = ThreadPoolExecutor(max_workers=10)

        for MusicName in MusicsName:
            thread = ThreadDownload(self.builder,self.downloader,MusicName.strip())
            threadPool.submit(thread.run)

        threadPool.shutdown(wait=True)

        logging.info("[+] Download Successful")
