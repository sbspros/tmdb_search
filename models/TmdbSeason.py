from TableClass import TableClass
from TmdbApi import TmdbApi

class TmdbSeason(TableClass):

    def __init__(self,id,title):
        super().__init__()
        self._id = id
        self._title = title
        self.log.info(' --- create Tmdb Show Season Object')
        self._isLoad = False

    def __str__(self):
        return "Show:{title} Season:{season} Total Episode:{maxEpisode} ".format(title=self._title,\
        season=self._seasonNum,maxEpisode=self.maxEpisode)

    def __del__(self):
        try:
            self.log.info(" -- Exiting Tmdb Show Season")
        except:
            pass

    @property
    def apiKey(self): return self.iniFile.config['api']['key']

    @property
    def baseSeasonUrl(self): return self.iniFile.config['api']['tvSeason']

    @property
    def maxEpisode(self):
        self.log.info(" ---- Inside maxEpisode")
        maxEsp = 0
        for episode in self._episodes:
            if episode['episode_number'] > maxEsp:
                maxEsp =  episode['episode_number']
        if  maxEsp == 0:
            raise SeasonNoFoundException()
        return maxEsp

    
    def loadSeason(self,seasonNum):
        self.log.info(" ---- Inside loadSeason")
        self._seasonNum = seasonNum
        model = TmdbApi()
        try:
            self._episodes = model.getItem(self.baseSeasonUrl.format(showId=str(self._id),\
                season=str(seasonNum),key=self.apiKey))['episodes']
            self._isLoad = True
        except:
            self._episodes = []


    def printEpisodes(self):
        self.log.info(" ---- Inside printEpisode")
        for episode in self._episodes:
            print("Are Date:{date} Season:{season} Episode:{episode} {name}".format(date=episode['air_date'],\
            season=self._seasonNum,episode=episode['episode_number'],name=episode['name']))

class SeasonNoFoundException(Exception):
    def __init__(self):
        super().__init__('Season no Found')

if __name__ == '__main__':
    ts = TmdbSeason(63726,"Alone")
    ts.loadSeason(6)
    ts.printEpisodes()
    print(ts)