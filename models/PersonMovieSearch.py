from common.BaseClass import BaseClass
from models.Genre import Genre
from inheritances.UnpagedMedia import UnpagedMedia

class PersonMovieSearch(UnpagedMedia):

    def __init__(self,bc:BaseClass,id):
        super().__init__(bc)
        self._link=self._bc.ini_file.config['person-links']['person-movies'].format(id=id)
        self._bc.log.error(self._link)
        self._genre=Genre(self._bc)
        self._genre.genre()
        self._format_str="""
        Title: {name}
        Charactor: {char_name}
        Overview:
        {overview}
     """


    def __str__(self):
        pass

    def media(self):
        rec=self.get_media()
        if rec['original_language']=='en' and rec['vote_average'] >7:
                genres=self._genre.lookup_list(rec['genre_ids'])
                print(self._format_str.format(title=rec['original_title'],char_name=rec['character'],overview=rec['overview']))
        return self.get_media()
