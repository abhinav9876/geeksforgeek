import logging
__all__=['ABsearch']
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.addHandler(stream_handler)
try:
    from search_package.searching.absearch import ABsearch

except:
    logger.exception('something wrong happened in searching package')
