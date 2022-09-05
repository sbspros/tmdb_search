from common.BaseClass import BaseClass
from exceptions.MediaTypeMissing import MediaTypeMissing
from models.TopRateTv import TopRateTv
from models.UpComingMovies import UpComingMovies
import argparse
import traceback


__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"
""" A ulitity to find and update plex media"""

if __name__ == '__main__':
    bc=BaseClass('config.ini')
    
    parser = argparse.ArgumentParser(description = 'A ulitity to find and update plex media')

    parser.add_argument('-t', 
        '--media_type',
        type=str, 
        help='media type {tv,movies}')    
    

    arg = parser.parse_args()
    try:
        if arg.media_type == None:
            raise MediaTypeMissing

        if arg.media_type == 'tv':
            media_search=TopRateTv(bc)   
            media_search.media()
        else:
            media_search=UpComingMovies(bc)   
            media_search.media()
       
    #     if show_search == []:
    #         bc.log.error("\tShow {show} for season {season} not found".format(show=arg.show,season=arg.season)) 
    #         raise ShowTitleMissing
        
    #     search_str=media_finder.show_to_search(show_search)

    #     ## search_str has last episode and we want the next one
    #     search_str['episode']=search_str['episode']+1
    #     links=media_finder.query(search_str,'query')
        
    #     if arg.link_style=='link':
    #         display_torrents.display_links(links)
    #     else:
    #         display_torrents.display_mag_link(links)

    # except  (MediaFinderFailed,PlexConnectionFailed,PlexSearcShowhFailed):
    #     ## Error logged by calling program
    #     exit()
    except:
        bc.log.error("\t"+":"+traceback.format_exc()) 
        exit()
