# write python program that read weather condition and 
# temprature degree from the user and decide the fol`lowing:
# if the weather condition is "Raining" check if the degree>45 
#    then print "Wear lightweight raincoat" 
#    otherwise print "Wear fleece and raincoat".
# if the weather condition is "Snowing" check if the degree>20 
#    then print "Wear softshell jacket" 
#    otherwise print "Wear down jacket".

condition = str(input("Enter weather condition:"))
degree = int(input("Enter temprature:"))

if condition =="Raining":
    if degree > 45:
        print("Wear lightWeight raincoat")
    else:
        print("Wear fleece and raincoat")

if condition =="Snowing":
    if degree > 20:
        print("Wear softshell jacket")
    else:
        print("Wear down jacket")