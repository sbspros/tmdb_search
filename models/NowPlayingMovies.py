from common.BaseClass import BaseClass
from inheritances.PagedMedia import PagedMedia
from models.Genre import Genre
class NowPlayingMovies(PagedMedia):

    def __init__(self,bc:BaseClass):
        super().__init__(bc)
        self._link=self._bc.ini_file.config['movie-links']['nowPlaying']
        self._bc.log.error(self._link)
        self._genre=Genre(self._bc)
        self._genre.genre()
        self._format_str="""
{title} ({release_date}) 
\tVote Average {vote_average}
\tgenre {genre_ids}
\t{overview}      """

    def __str__(self):
        pass

    def media(self):
        for rec in self.get_media():
            if rec['original_language']=='en':
                genres=self._genre.lookup_list(rec['genre_ids'])
                print(self._format_str.format(title=rec['title'],vote_average=rec['vote_average'],overview=rec['overview'],genre_ids=genres,release_date=rec['release_date']))

