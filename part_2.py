rover_status = {
"Battery": 100,      #(Integer)

"Heater": "Off",     #(String)

"Camera": "Standby"     #(String)

}

print("The current status of the Battery is:", rover_status["Battery"])
print("The current status of the Heater is:", rover_status["Heater"])
print("The current status of the Camera is:", rover_status["Camera"])

print("Rover is now moving:")

rover_status["Battery"] = 85
print("The current status of the Battery is:", rover_status["Battery"])
rover_status["Heater"] = "On"
print("The current status of the Heater is:", rover_status["Heater"])

rover_status["Speed"] = 5
#print("The current status of the Speed is:", rover_status["Speed"])
print(rover_status)

mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False}, #D1
    {"Site": "Dune B", "Radiation": "High", "Water": True}    #D2
]

print(mission_log)