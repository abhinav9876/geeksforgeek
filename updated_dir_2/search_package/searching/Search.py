from search_package.searching.singleton import *
from abc import ABCMeta,abstractmethod
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.addHandler(stream_handler)



#@singleton
class search(metaclass=ABCMeta):
    #@abstractmethod
    def search_string(self,String,pattern):
        try:
            ll=[]
            concate=pattern+'$'+String
            z=self.__z_arr(concate)
            for i in range(len(z)):
                if z[i]==len(pattern):
                    ll.append(str("pattern found at index ")+str(i-len(pattern)-1))

        except:
                        logger.exception('something wrong happened in searching position of pattern in string')
        else:
            return ll
    #@abstractmethod
    def __z_arr(self,ss):
        try:
            l=0
            r=0
            k=0
            n=len(ss)
            z=[0]
            for i in range(1,n):
                if l<i:
                    l=r=i
                    while(r<n and ss[r-l]==ss[r]):
                        r+=1
                    z.append(r-l)
                    r-=1
                else:
                    k=i-l
                    if z[k]<r-i+1:
                        z.append(z[k])
                    else:
                        l=i
                        while r<n and ss[r-l]==ss[r]:
                            r+=1
                        z.append(r-l)
                        r-=1

        except:
            logger.exception('something wrong happened in crearting z array')
        else:
            return z
