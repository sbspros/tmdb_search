from common.BaseClass import BaseClass

class Media():

    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._link=None
        self._results=[]
        self._status=None
        self._apk_key=self._bc.ini_file.config['api']['key']


        @property
        def link(self):return self._link

        @link.setter
        def link(self,link): self._link = link

        @property
        def results(self):return self._results

        @property
        def status(self):return self._status

        @property
        def api_key(self): return self._apk_key