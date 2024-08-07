class MechanicDirect(Mechanic):
    def __init__(self):
        super.__init__()
        self.__base_price = 100000
        self.__price_per_hour = 100000
        self.__speed = 60
    
    def get_base_price(self):
        return self.__base_price
    
    def get_price_per_hour(self):
        return self.__price_per_hour
    
    def get_speed(self):
        return self.__speed
    
    def calculate_total_price(self, service_time):
        return self.get_base_price + self.get_price_per_hour * service_time
