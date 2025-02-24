print("q1")
DEGREE = "\u00B0"

def dms(angle):
    degrees = int(angle)
    float_minutes = (angle - degrees) * 60
    minutes = int(float_minutes)
    seconds = int((float_minutes - minutes) * 60)
    
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)

    return(f"{degrees}{DEGREE}{minutes}'{seconds}\"")

print(dms(93.034773))

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
