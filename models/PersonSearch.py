from common.BaseClass import BaseClass
from inheritances.PagedMedia import PagedMedia
from models.Genre import Genre
import datetime
import time

class PersonSearch(PagedMedia):

    def __init__(self,bc:BaseClass.person):
        super().__init__(bc)
        self._link=self._bc.ini_file.config['tv-links']['person_search'].format(person=person)
        self._bc.log.error(self._link)
        self._genre=Genre(self._bc)
        self._genre.genre()
        self._format_str="""
        name: {name}
        id:{id}
        popularity: {popularity}
      """

    def __str__(self):
        pass

    def media(self):
        data=self.get_media()
        for rec in data:
            genres=self._genre.lookup_list(rec['genre_ids'])
            print(self._format_str.format(name=rec['name'],popularity=rec['popularity'],id=rec['id']))
        return self.get_media()
