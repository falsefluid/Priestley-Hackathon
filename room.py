#room.py
import csv
def room():
    filename="MainSheet.csv"
    fields=[]
    rows=[]
    rooms=["LC.1","LC.2","LC.3","LC.4","LC.5","P1.1","P1.2","P1.3","P1.4","P1.5"]
    temprooms = rooms
    LightsOn=True
    with open(filename,"r") as mainfile:
        csvreader=csv.reader(mainfile)
        fields=next(csvreader)
        for row in csvreader:
            rows.append(row)

    for row in rows[:100]:
        a=row[11]
        b=row[1]
        c=row[2]
        if a =="None":
            print(" ")
        elif a in rooms:
            print("==================")
            print(a,"In use by", b, c)
            LightsOn=True
            temprooms.remove(a)
    for x in range(len(temprooms)):
        print("==================")
        print(temprooms[x],"Not in use, turning lights off")
        LightsOn=False


