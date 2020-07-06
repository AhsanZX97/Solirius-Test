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

def printLight(light,pos):
    print("{} {} {}".format(strftime("%H:%M:%S", gmtime()),pos,light))#

if __name__ == "__main__":
    Colours = ["Red","Green","White"]
    LightSet = []
    maxSet = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    for i in range(0, maxSet):
        LightSet.append(Lights(Colours[i%3]))
        LightSet[i].toggleState()
        printLight(LightSet[i],i+1)
    time.sleep(1)
    for i in range(0,maxSet):
        LightSet[i].toggleState()
        printLight(LightSet[i],i+1)

    while True:
        try:
            string = input("Enter command: ")
            if string == "exit":
                break
            elif string == "run":
                try: 
                    while True: 
                        for i in range(0, maxSet):
                            LightSet[i].toggleState()
                            printLight(LightSet[i],i+1)
                            time.sleep(1)
                            LightSet[i].toggleState()
                            printLight(LightSet[i],i+1)
                            time.sleep(1)
                except KeyboardInterrupt:
                    pass
            elif string.startswith("set "):
                req = string[4:].strip()
                reqList = req.split()   
                if reqList[0].isdigit():
                    LightSet[int(reqList[0]) - 1]._colour = reqList[1]
                    print("The light number {} is now {}".format(int(reqList[0]), reqList[1]))
        except Exception as e:
            print(e)
