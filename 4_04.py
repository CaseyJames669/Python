#Objects and Methods: id and type functions

hrs = input("enter your hours: ")
print ("id is: ", id(hrs))
print ("type is: ", type(hrs))

#the id is an automatically assigned integer for hrs.
#type tells you what class hrs is defined as.
#so on this run the id was 49073152
#and the class is 'str'

strHrs = input("enter your hours: ")
print ("id of strHrs is: ", id(strHrs))
print ("type of strHrs is: ", type(strHrs))
print("==================")
hrs = eval(strHrs)
print ("id of hrs is: ", id(hrs))
print ("type of hrs is: ", type(hrs))

#with 40.8 strHrs you get an id of 49152440 which is a str type class
#and as hrs you get an id of 3067136 which is a float type class

#with 35 strHrs you get an id of 50056584 which is a str type class
#and as hrs you get an id of 506099824 which is a int type class
