class Cars:
    number_of_wheels=4
    def __init__(self,color,car_model,max_speed):
        self.color=color
        self.car_model=car_model
        self.max_speed=max_speed
    
    def show_info(self):
        print(self.color, self.car_model, self.max_speed)
        
    def show_color(self):
        print(self.color)

car1=Cars("red","cedan",220)
car2=Cars("blue","crossover",250)

setattr(car1,"number_of_wheels",3)
print(car1.number_of_wheels)
print(car2.number_of_wheels)