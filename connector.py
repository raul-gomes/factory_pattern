from abc import ABC, abstractmethod

class APIConnector(ABC):
    """ Basic representation of the API Connector"""

    @abstractmethod
    def connect(self) -> None:
        """Connect to API"""
        pass

class TwitterAPI(APIConnector):
    """ Twitter API """
    
    def connect(self, querie:str) -> str:
        print(f"Twitter API: {querie}")


class FacebookAPI(APIConnector):
    """ Facebook API """

    def connect(self, querie:str) -> str:
        print(f"Facebook API: {querie}")