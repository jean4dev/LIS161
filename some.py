#cs1
hrs = input("Enter Hours:")
h = float(hrs)
rate =input("Enter Rate:")
r = float(rate)
if h > 40:
	p = (((h-40)*(r*1.5))+(40*r))
else:
    p = (h*r)
print(p)



#cs2
try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate =input("Enter Rate:")
    r = float(rate)
    if h > 40:
	       p = (((h-40)*(r*1.5))+(40*r))
    else:
           p = (h*r)
    print(p)
except:
    print("Error, please enter numeric input")





#cs3
try:
    score = input("Enter Score: ")
    s = float(score)

    if s >= 0.9 and s <= 1.0:
	    print("A")
    elif s >= 0.8 and s < 0.9:
        print("B")
    elif s >= 0.7 and s < 0.8:
        print("C")
    elif s >= 0.6 and s < 0.7:
        print("D")
    elif s < 0.6 and s > 0.0:
        print("F")
    else:
        print("Range!")
except:
    print("Bad Number")




#f1
h = float(input("Enter hours: "))
r = float(input("Enter rate: "))
def computepay():
    if h > 40:
    	p = (((h-40)*(r*1.5))+(40*r))
    else:
        p = (h*r)
    print(p)

computepay()





#f2
s = float(input("Enter Score: "))

def computegrade():
    try:
        if s >= 0.9 and s <= 1.0:
	          print("A")
        elif s >= 0.8 and s < 0.9:
              print("B")
        elif s >= 0.7 and s < 0.8:
              print("C")
        elif s >= 0.6 and s < 0.7:
              print("D")
        elif s < 0.6 and s > 0.0:
              print("F")
        else:
              print("Range!")
    except:
        print("Bad Number")

computegrade()



#i1
new =""
total = 0
count =0
avg = float()

while True:
    if new == "done":
        break
    else:
        try:
            new = input()
            count += 1
            total= new + total
        except:
            print("bad")
