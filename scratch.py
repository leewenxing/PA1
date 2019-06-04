import csv
class CalUtils:
    def __init__(calAvgHeight , names , heights , totalstudentheight , totalstudentcount):
        calAvgHeight.names=str(names)
        calAvgHeight.heights=float(heights)
        calAvgHeight.totalstudentheight=float(heights)
        calAvgHeight.totalstudentcount=float(totalstudentcount)
namesandweight = {"wenxing":1.89, "leon":1.76, "reuben":1.8999, "debin":1.79}
print(namesandweight)
totalstudentheight=sum(namesandweight.values())
print("the total height of the student is {}".format(totalstudentheight))
totalstudentnames=len(namesandweight.keys())
calAvgHeight=(totalstudentheight/totalstudentnames)
print("the average height of the student not in 2 decimal is {}".format(calAvgHeight))
twodecimal=(round(calAvgHeight, 2))
print("student average height is {} in two decimal point for {} students".format(twodecimal,totalstudentnames))
adduserandhisweight=input("do u want to enter student name ? yes or no:")
while adduserandhisweight == "yes":
    names=input("enter new student name:")
    try:
        heights=float(input("enter student height(in meters):"))

    except:
        print("not numeric ")
        exit()

    adduserandhisweight=input("do u want to add another user and his height? yes or no:")
    namesandweight[names]= heights
print(namesandweight)
totalstudentheight=sum(namesandweight.values())
print("the updated sum of total student height is {}".format(totalstudentheight))
totalstudentcount=len(namesandweight.keys())
calAvgHeight=(totalstudentheight/totalstudentcount)
print("student average height of the student not in two decimal place is {}".format(calAvgHeight))
twodecimal=(round(calAvgHeight, 2))
print("student average height is {} in two decimal point for {} students".format(twodecimal,totalstudentcount))

fileoperator = csv.writer(open("listOfStudentHeight.txt ", "w"))
for key, val in namesandweight.items():
    print((f"\n{key}    {val}"))
    with open("listOfStudentHeight.txt" , "a") as file:
        file.write(f"\n{key}    {val}")
