import search
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.addHandler(stream_handler)
class ABsearch(search):
    '''
    ABsearch class--
           three method :
              prepare_for_search(string,pattern)->Null
              begin_search()->Null
              endsearch()->print location of pattern in string

    '''
    def prepare_for_search(String,pattern):
        try:
            self.String=String
            self.pattern=pattern
        except:
            logger.exception('something wrong happened in preparing for search'))
    def begin_search():
        try:
            self.__z=super(ABsearch,self).search_string(self.String,self.pattern)
        except:
            logger.exception('something wrong happened to begin search'))
    def end_search():
        try:
            for i in self.__z:
                logger.INFO(i)
        except:
            logger.exception('something wrong happened to end search'))
