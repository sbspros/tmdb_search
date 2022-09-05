from common.BaseClass import BaseClass
from models.Genre import Genre
from inheritances.UnpagedMedia import UnpagedMedia

class LatestTv(UnpagedMedia):

    def __init__(self,bc:BaseClass):
        super().__init__(bc)
        self._link=self._bc.ini_file.config['tv-links']['latest']
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
        rec=self.get_media()
        if rec['original_language']=='en' and rec['vote_average'] >7:
                genres=self._genre.lookup_list(rec['genre_ids'])
                print(self._format_str.format(original_name=rec['original_name'],vote_average=rec['vote_average'],overview=rec['overview'],genre_ids=genres))
        return self.get_media()


