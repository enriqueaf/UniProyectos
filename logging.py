'''
Utils
'''  
class LogError(Exception):
    pass

class logging:
    LOG_LEVELS={'INFO':0,'DEBUG':1}
    _LOG_LEVEL=0
    def __init__(self,module):
        self.module = module
    @staticmethod
    def set_log_level(level):
        try:
            logging._LOG_LEVEL = logging.LOG_LEVELS[level]
            return True
        except:
            raise LogError('Level no suported')
    @staticmethod
    def get_log_level():
        return Login._LOG_LEVEL
    def wrt(self,msg,level='INFO'):
        if logging._LOG_LEVEL >= logging.LOG_LEVELS[level]: 
                print '[',self.module,']',msg
if __name__ == '__main__':
    pass
