from GrabberClass import GitbookGrabber as Grabber

#PATH = "https://xerus.gitbook.io/msp/api-reference/"

class XerusBook( Grabber ):

    def __init__(self, PATH) -> None:
        self._PATH = PATH

    
    def find_api( self, dest, source):
        '''
        Given a destination and a source, grabs the API call

        Requires dest, source
            - dest: ( ex "amfachievementwebservice")
            - source: ( ex "GetAchievementProgress")
        '''
        return None

    