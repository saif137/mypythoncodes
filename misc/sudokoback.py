import Tkinter
import random

k=[8,3,2,6,7,1,4,9,5]

class algo:
    def __init__(self,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0):
##        ra=random.sample(k,9)
##        self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i=(ra[0],
##                    ra[1],ra[2],ra[3],ra[4],ra[5],ra[6],ra[7],ra[8])
##        for i in range(9):
##            print(ra[i])
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
        self.h=h
        self.i=i
##    def ran(self):
##        for i in range(9):
##            print(ra[i])
    def Sumh(self): #checks the horizontal sum
        x=self.a+self.b+self.c+self.d+self.e+self.f+self.g+self.h+self.i
        if x==45:
            return(True)
        else:
            return(False)

class vert:
    def Sumv(self): #checks the verticle sums
        if ((c1.a+c2.a+c3.a+c4.a+c5.a+c6.a+c7.a+c8.a+c9.a)==45 and
            (c1.b+c2.b+c3.b+c4.b+c5.b+c6.b+c7.b+c8.b+c9.b)==45 and
            (c1.c+c2.c+c3.c+c4.c+c5.c+c6.c+c7.c+c8.c+c9.c)==45 and
            (c1.d+c2.d+c3.d+c4.d+c5.d+c6.d+c7.d+c8.d+c9.d)==45 and
            (c1.e+c2.e+c3.e+c4.e+c5.e+c6.e+c7.e+c8.e+c9.e)==45 and
            (c1.f+c2.f+c3.f+c4.f+c5.f+c6.f+c7.f+c8.f+c9.f)==45 and
            (c1.g+c2.g+c3.g+c4.g+c5.g+c6.g+c7.g+c8.g+c9.g)==45 and
            (c1.h+c2.h+c3.h+c4.h+c5.h+c6.h+c7.h+c8.h+c9.h)==45 and
            (c1.i+c2.i+c3.i+c4.i+c5.i+c6.i+c7.i+c8.i+c9.i)==45):
            return(True)
        else:
            return(False)
    def Sumb(self): #checks the sum of 3x3 boxes
        if ((c1.a+c2.a+c3.a+c1.b+c2.b+c3.b+c1.c+c2.c+c3.c)==45 and
            (c1.d+c2.d+c3.d+c1.e+c2.e+c3.e+c1.f+c2.f+c3.f)==45 and
            (c1.g+c2.g+c3.g+c1.h+c2.h+c3.h+c1.i+c2.i+c3.i)==45 and
            (c4.a+c5.a+c6.a+c4.b+c5.b+c6.b+c4.c+c5.c+c6.c)==45 and
            (c4.d+c5.d+c6.d+c4.e+c5.e+c6.e+c4.f+c5.f+c6.f)==45 and
            (c4.g+c5.g+c6.g+c4.h+c5.h+c6.h+c4.i+c5.i+c6.i)==45 and
            (c7.a+c8.a+c9.a+c7.b+c8.b+c9.b+c7.c+c8.c+c9.c)==45 and
            (c7.d+c8.d+c9.d+c7.e+c8.e+c9.e+c7.f+c8.f+c9.f)==45 and
            (c7.g+c8.g+c9.g+c7.h+c8.h+c9.h+c7.i+c8.i+c9.i)==45):
            return(True)
        else:
            return(False)

##class box:
##    def Sumb(self): #checks the sum of 3x3 boxes
##        if ((c1.a+c2.a+c3.a+c1.b+c2.b+c3.b+c1.c+c2.c+c3.c)==45 and
##            (c1.d+c2.d+c3.d+c1.e+c2.e+c3.e+c1.f+c2.f+c3.f)==45 and
##            (c1.g+c2.g+c3.g+c1.h+c2.h+c3.h+c1.i+c2.i+c3.i)==45 and
##            (c4.a+c5.a+c6.a+c4.b+c5.b+c6.b+c4.c+c5.c+c6.c)==45 and
##            (c4.d+c5.d+c6.d+c4.e+c5.e+c6.e+c4.f+c5.f+c6.f)==45 and
##            (c4.g+c5.g+c6.g+c4.h+c5.h+c6.h+c4.i+c5.i+c6.i)==45 and
##            (c7.a+c8.a+c9.a+c7.b+c8.b+c9.b+c7.c+c8.c+c9.c)==45 and
##            (c7.d+c8.d+c9.d+c7.e+c8.e+c9.e+c7.f+c8.f+c9.f)==45 and
##            (c7.g+c8.g+c9.g+c7.h+c8.h+c9.h+c7.i+c8.i+c9.i)==45):
##            return(True)
##        else:
##            return(False)

c1=algo(8,2,7,1,5,4,3,9,6)
c2=algo(9,6,5,3,2,7,1,4,8)
c3=algo(3,4,1,6,8,9,7,5,2)
c4=algo(5,9,3,4,6,8,2,7,1)
c5=algo(4,7,2,5,1,3,6,8,9)
c6=algo(6,1,8,9,7,2,4,3,5)
c7=algo(7,8,6,2,3,5,9,1,4)
c8=algo(1,5,4,7,9,6,8,2,3)
c9=algo(2,3,9,8,4,1,5,6,7)

sud=vert()
##sudb=box()
print(c9.Sumh())
print(sud.Sumv())
print(sud.Sumb())


k=[8,3,2,6,7,1,4,9,5]
j=[]

root = Tkinter.Tk(  )

for r in range(9):
   for c in range(1):
       i=random.sample(k,9) #creates non repeated horizontals
       Tkinter.Label(root, text='%s   '%i#(r+1,c+1),
           ,borderwidth=1 ).grid(row=r,column=c)
root.mainloop(  )



