from abc import abstractmethod

class preguntasDB:
    @abstractmethod
    def filtrarJSONPregunta(row):
        pass
    
    @abstractmethod
    def getQuery():
        pass