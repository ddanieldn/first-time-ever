x=3 #input
fx=0
gx=0
hx=0

if x<10:
    fx +=x**2-5*x
elif 10<=x<50:
    fx += (3*x+11)**0.5
elif x>=50:
    fx += (x**2-25)**(1/3)
print("f(x)= ", fx)

if fx<5:
    gx += abs(2*fx-17)
elif 15<fx<30:
    gx +=abs((1/13)*fx-43)
elif fx>=30:
    gx +=((fx)**0.5)-(10/33)*fx
print("g(x)= ", gx)

if gx<10:
    hx +=1.7246*gx
elif 20<=gx<35:
    hx +=1.3355/((gx/2.1425)+(1.1311*gx))
elif gx>=35:
    hx +=(7.142/(0.5412*gx))**0.5
print("h(x)= ", hx)

if hx<(fx/gx):
    cond =(fx/gx)+hx
elif hx>=(fx/gx):
    cond =((fx-1)*hx)/gx

ref = 2 + 2 + 2 + 1 + 6 + 1 + 0 + 1 + 3 + 8 # student id

if cond == ref:
    print(True," ",cond," is equal to the ref ", ref)
elif cond != ref:
    print(False," ",cond," is not equal to the ref ", ref)
    print("Sansern ")