b = input("enter b: ")
try:
    b = int(b)
    result = 10 / b 
except ZeroDivisionError:
    print("cant divide") 
except ValueError:
    print("Can't divided by a character")
except Exception as e: 
    print(f"An error occurred: {e}")  
