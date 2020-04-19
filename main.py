from Downloader import Downloader
from Builder import Builder
from Utils import loadconfig
from Controller import Controller





if __name__ == '__main__':
# -----------------load config--------------------
    configpath = "Config/config.json"
    configs = loadconfig(configpath)
    dir_config = configs["Dir"]
    file_config = configs["File"]
# -----------------create classes--------------
    builder = Builder(configpath)
    downloader = Downloader(dir_config["Save_Path"])
    controller = Controller(file_config["MusicList"])
# ------------------------------------------
    controller = controller.init(downloader,builder)
    controller.AutoDownload()