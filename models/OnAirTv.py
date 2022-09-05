from common.BaseClass import BaseClass
from inheritances.PagedMedia import PagedMedia
from models.Genre import Genre
import datetime
import time

class OnAirTv(PagedMedia):

    def __init__(self,bc:BaseClass):
        super().__init__(bc)
        self._link=self._bc.ini_file.config['tv-links']['onAir']
        self._bc.log.error(self._link)
        self._genre=Genre(self._bc)
        self._genre.genre()        
        self._format_str="""
{original_name}  
\tVote Average {vote_average}
\tgenre {genre_ids}
\t{overview}      """

    def __str__(self):
        pass

    def media(self):
        data=self.get_media()
        for rec in data:
            if rec['original_language']=='en' and rec['vote_average'] >7:
                genres=self._genre.lookup_list(rec['genre_ids'])
                print(self._format_str.format(original_name=rec['original_name'],vote_average=rec['vote_average'],overview=rec['overview'],genre_ids=genres))
        return self.get_media()


