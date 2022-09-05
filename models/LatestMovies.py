
from common.BaseClass import BaseClass
from inheritances.UnpagedMedia import UnpagedMedia
from models.Genre import Genre

class LatestMovies(UnpagedMedia):

    def __init__(self,bc:BaseClass):
        super().__init__(bc)
        self._link=self._bc.ini_file.config['movie-links']['latest']
        self._bc.log.error(self._link)
        self._genre=Genre(self._bc)
        self._genre.genre()
        self._format_str="""
Name {title} ({release_date}) 
\tVote Average {vote_average}
\tgenre {genres}
\t{overview}      """

    def __str__(self):
        pass

    def media(self):
        rec=self.get_media()
        if rec['original_language']=='en' and rec['vote_average'] >7:
            genres=self._genre.lookup_list(rec['genre_ids'])
            print(self._format_str.format(original_name=rec['original_name'],vote_average=rec['vote_average'],overview=rec['overview'],genres=genres))

    def test_404(self):
        return{
  "status_message": "The resource you requested could not be found.",
  "status_code": 34
}

    def test_api_key(self):
        return {
  "status_message": "Invalid API key: You must be granted a valid key.",
  "success": False,
  "status_code": 7
}