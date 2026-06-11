#class.property=value this will help to chaneg the avlue with using property whcih is basically the object
class vehicle:
    wheels=5
    color="green"


print(vehicle.wheels)     
vehicle.wheels=int(input("tell me if you want to change number of wheels:--"))
v=vehicle.wheels
if v>5:
    print("wheels increased to",vehicle.wheels)
else:
    print("wheels deccreased to",vehicle.wheels)    
vehicle.color=input("which color you want>>>>")
vehicle.color=f"color changed to {vehicle.color}"
print(vehicle.color)

#modifications with respect to class name willl refelect both class as well as object dictionaries
#modifications with respect to object name willl refelect only the particular dictionaries


