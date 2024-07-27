def capitalize(**my_dict):
    for key,value in my_dict.items():
        if isinstance (value, str):
            my_dict[key] = value.capitalize()
    return my_dict
    
my_dict = capitalize(name = "alaN", aGe = 33, pLaCe = "kOcHi" )
print(my_dict)

# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]


# creating objects of car class
audi = Car(200, 'red')
bmw = Car(250, 'black')
mb = Car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)