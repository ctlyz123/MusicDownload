

class ThreadDownload( ):
    def __init__(self,builder,downloader,MusicName):
        self.builder = builder
        self.downloader = downloader
        self.MusicName = MusicName

    def run(self):
        # print("ThreadDownload %s"%(self.MusicName))
        Musicurl = self.builder.create(self.MusicName)
        print(self.MusicName.strip(),":",Musicurl)
        self.downloader.download(Musicurl,self.MusicName)