from search_package.searching.Search import search
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.addHandler(stream_handler)

class ABsearch(search):

    def prepare_for_search(self,Strings,pattern):
        try:
            self.Strings=Strings
            self.pattern=pattern
        except:
            logger.exception('something wrong happened in preparing for search')
    def begin_search(self):
        try:
            self.__z=super(ABsearch,self).search_string(self.Strings,self.pattern)
        except:
            logger.exception('something wrong happened to begin search')
    def end_search(self):
        try:
            return self.__z
            #for i in self.__z:
                #logger.INFO(i)
                #print(i)

        except:
            logger.exception('something wrong happened to end search')
    '''
            ABsearch class--
            three method :
            prepare_for_search(string,pattern)->Null
            begin_search()->Null
            endsearch()->print location of pattern in string

   '''
