class MovieAlreadyavailableError(Exception):
    def __init__(self,message):
        self.message=message
class MovieNotAvailableerror(Exception):
    def __init__(self,message):
        self.message=message
class TicketsNotAvailableError(Exception):
    def __init__(self,message):
        self.message=message 
    