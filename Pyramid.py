from time import sleep

for i in range(1, 6):
    for j in range(6-i):
        print(" ", end="")
        
    for j in range(1,2*i):
        print("*", end="")
        sleep(0.1)
    print()