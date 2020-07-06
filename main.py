#The number of lights should be configurable on the command line with a default value of 20.
#The set of lights will be made up of a repeating set of colours in a fixed order (e.g red, green, white)
#When you run the program, it should turn each light in the set on for 1 second and then turn it off.
#The output of the program should be formatted as follows: {HH:MM:SS} {light no / postion} {colour} Light {light state}
#12:00:01: 1 Red Light On 12:00:02: 1 Red Light Off 12:00:02: 2 Green Light On 12:00:03: 2 Green Light Off 12:00:03: 3 White Light On 12:00:04: 3 White Light Off etc. etc.
#The sequence should continue in a loop until the program is interrupted.
#Design the program so that it would be easy to modify the colours and the number of colours that make up the set of lights using object oriented techniques. (e.g. blue, red, yellow, white).
import sys
from lights import Lights
from time import gmtime, strftime
import time

# outputs state of light
def printLight(light,pos):
    print("{} {} {}".format(strftime("%H:%M:%S", gmtime()),pos,light))#

# The list of colours a light can take up
Colours = ["Red","Green","White","Blue","Yellow", "Purple", "Orange"]

if __name__ == "__main__":
    # error checks to see if the argument given was a number and not a string
    if len(sys.argv) > 1:
        if not sys.argv[1].isdigit():
            print("please enter a number or leave the argument blank")
            exit() 
    
    # initialise the light set
    LightSet = []

    # if argument wasn't passed, the list is of length 20 otherwise the argument
    maxSet = int(sys.argv[1]) if len(sys.argv) > 1 else 20

    # fills the list with the order of Colour list and turns them on for 1 second
    for i in range(0, maxSet):
        LightSet.append(Lights(Colours[i%7]))
        LightSet[i].toggleState()
        printLight(LightSet[i],i+1)
    
    time.sleep(1)

    # Goes through the list of lights and turns them off 
    for i in range(0,maxSet):
        LightSet[i].toggleState()
        printLight(LightSet[i],i+1)
    
    index = 0
    while True:
        try:
            # user can enter commands for the program while its running
            string = input("Enter command: ")
            
            # closes the program
            if string == "exit":
                break
            
            # runs throught the list of light switching them on and off
            elif string == "run":
                try: 
                    while True: 
                        LightSet[index].toggleState()
                        printLight(LightSet[index],index+1)
                        time.sleep(1)
                        LightSet[index].toggleState()
                        printLight(LightSet[index],index+1)
                        time.sleep(1)
                        index = 0 if index + 1 == maxSet else index + 1
                except KeyboardInterrupt:
                    pass
            
            # lets a user change the colour of a light, colour has to be in capitale.g set 1 Yellow
            elif string.startswith("set "):
                req = string[4:].strip()
                reqList = req.split() 
                if len(reqList) != 2 or not reqList[0].isdigit() or not isinstance(reqList[1], str) or reqList[1] not in Colours: 
                    print("please enter a correct format")
                    pass  
                else:
                    LightSet[int(reqList[0]) - 1]._colour = reqList[1]
                    print("The light number {} is now {}".format(int(reqList[0]), reqList[1]))
        except Exception as e:
            print(e)
