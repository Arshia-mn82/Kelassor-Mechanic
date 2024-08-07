
class Mechanic:  
    def __init__(self, name, X, Y, id, service, map) -> None:  
        self.__name = name                      
        self.__X = X                            
        self.__Y = Y                            
        self.__id = id                         
        self.__service = None
        self.__map =  map

    def get_id(self):  
        return self.__id  

    def get_name(self):  
        return self.__name  

    def get_service(self): 
        return self.__service

    def set_service(self, service):
        self.__service = service  


    def calculate_total_price(self, service_time):
        pass
