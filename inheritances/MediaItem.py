from interfaces.Media import Media as MediaInterface
from app.inheritances.Media import Media as MediaBaseClass
from common.BaseClass import BaseClass
from exceptions.ApiExceptions import ApiRequestException,ApiOtherException

import requests

class MediaItem(MediaInterface,MediaBaseClass):

    def __init__(self,bc:BaseClass)->None:
        self._bc=bc
        super.__init__(self._bc)


    def get_media(self,link):
        ''' Returns a dictionary from a single API call
            Make a API call that returns all of its data
            at once
        '''
        try:
            return requests.get(self._link).json()
        except requests.exceptions.HTTPError:
            return []
