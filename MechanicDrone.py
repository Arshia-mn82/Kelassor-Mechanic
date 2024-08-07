class MechanicDrone(Mechanic):
    def init(self):
        super().__init__()
        self.__base_price = 240000
        self.__speed = 50

    def get_base(self):
        return self.__base_price
    
    def get_speed(self):
        return self.__speed 
    
    def calculate_total_price(self , service_time):
        return self.get_base()
      