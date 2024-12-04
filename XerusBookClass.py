from GrabberClass import GitbookGrabber as Grabber

#PATH = "https://xerus.gitbook.io/msp/api-reference/"

class XerusBook( Grabber ):

    def __init__(self, PATH) -> None:
        self._PATH = PATH

    