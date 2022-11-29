from abc import ABC, abstractmethod
from connector import APIConnector, TwitterAPI, FacebookAPI

class APIFactory(ABC):
    """ API Factory"""

    @abstractmethod
    def create_api(self) -> APIConnector:
        """Create API"""
        pass

class TwitterAPIFactory(APIFactory):
    """ Twitter API Factory"""
    
    def create_api(self) -> APIConnector:
        return TwitterAPI()


class FacebookAPIFactory(APIFactory):
    """ Facebook API Factory"""

    def create_api(self) -> APIConnector:
        return FacebookAPI()