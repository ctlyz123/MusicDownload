import abc

class BaseRequester(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def req(self,url):
        pass

    @abc.abstractmethod
    def save(self,url,save_path):
        pass