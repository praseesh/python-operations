def capitalize(**my_dict):
    for key,value in my_dict.items():
        if isinstance (value, str):
            my_dict[key] = value.capitalize()
    return my_dict
    
my_dict = capitalize(name = "alaN", aGe = 33, pLaCe = "kOcHi" )
print(my_dict)