#motor controller

while True:
    try:
        emp  = int(input("Enter Motor Speed: "))
        print(f"Speed set to: {emp}")
        break

    except ValueError:
        print("Error: Corrupted Signal. Maintaining current speed.")

def get_coordinate():

    while True:
        coordinate = int(input("What is the X coordinate? "))

        print(f"Coordinate X set to: {coordinate}")
        break
    
    while False:
    
        coordinate = (input("What is the X coordinate? "))
        print("Invalid coordinate")

    get_coordinate()