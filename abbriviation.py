#for python
import math,sys
sys.set_int_max_str_digits(10**9)
def add_abb():
    global a,b,c,d,e
    d = ["","K","M","B","T","Qd","Qn","Sx","Sp","Oc","No"]
    a = ["","U","D","T","Qd","Qn","Sx","Sp","Oc","No"]
    b = ["","De","Vg","Tg","Qg","Qq","Sg","St","Og","Ng"]
    c = ["","Ce","Dc","Tc","Qe","Qu","Se","Su","Oc","Ne"]
    e = ["","Mi","Mc","Na","Pi","Fem","At","Zep","Yo"]
    

def abb(n: int):
    add_abb()
    Num = ""
    if n%10**(3*9) > 10**(3*9)/1000-1:
        Num= Num+a[math.floor(n/10**12)%10]
        Num= Num+b[math.floor(n/10**23)%10]
        Num= Num+c[math.floor(n/10**24)%10]
        Num= Num+e[7]
    if n%10**(3*8) > 10**(3*8)/1000-1:
        Num= Num+a[math.floor(n/10**19)%10]
        Num= Num+b[math.floor(n/10**20)%10]
        Num= Num+c[math.floor(n/10**21)%10]
        Num= Num+e[6]
    if n%10**(3*7) > 10**(3*7)/1000-1:
        Num= Num+a[math.floor(n/10**16)%10]
        Num= Num+b[math.floor(n/10**17)%10]
        Num= Num+c[math.floor(n/10**18)%10]
        Num= Num+e[5]
    if n%10**(3*6) > 10**(3*6)/1000-1:
        Num= Num+a[math.floor(n/10**13)%10]
        Num= Num+b[math.floor(n/10**14)%10]
        Num= Num+c[math.floor(n/10**15)%10]
        Num= Num+e[4]
    if n%10**(3*5) > 10**(3*5)/1000-1:
        Num= Num+a[math.floor(n/10**10)%10]
        Num= Num+b[math.floor(n/10**11)%10]
        Num= Num+c[math.floor(n/10**12)%10]
        Num= Num+e[3]
    if n%10**(3*4) > 10**(3*4)/1000-1:
        Num=Num+a[math.floor(n/10**17)%10]
        Num= Num+b[math.floor(n/10**8)%10]
        Num= Num+c[math.floor(n/10**9)%10]
        Num= Num+e[2]
    if n%10**(3*3) > 10**(3*3)/1000-1:
        Num=Num+a[math.floor(n/10**4)%10]
        Num= Num+b[math.floor(n/10**5)%10]
        Num= Num+c[math.floor(n/10**6)%10]
        Num= Num+e[1]
    if n%10**(3*2) > 10**(3*2)/1000-1:
        Num= Num+a[math.floor(n/1)%10]
        Num= Num+b[math.floor(n/10)%10]
        Num= Num+c[math.floor(n/100)%10]
    else:
        Num= Num+d[math.floor(n/1)%10]
    return Num


def NumToAbb(n: int ,prec: int):
    prec = int(prec)
    Number = int(n)
    ToString = str(Number)
    GetLength = len(ToString)
    Finished = math.floor((GetLength-1)/3)
    a = 0
    b = ToString[a]
    if Number > 999:
        if prec < GetLength:
            for i in range(prec):
                a += 1
                if a == GetLength%3:
                    b = b+"."
                if GetLength%3 == 0:
                    b = b+ToString[a]
                    a += 1
                    b = b+ToString[a]
                    b = b+"."
                    GetLength = 0.1
                b = b+ToString[a]
            return str(f'{b} '+abb(Finished))
        else:
            for i in range(GetLength-1):
                a += 1
                if a == GetLength%3:
                    b = b+"."
                if GetLength%3 == 0:
                    b = b+ToString[a]
                    a += 1
                    b = b+ToString[a]
                    b = b+"."
                    GetLength = 0.1
                b = b+ToString[a]
            return str(f'{b} '+abb(Finished))
    else:
        return Number
if __name__ == '__main__': 
    print("---------\n"+NumToAbb(input("Number Here: "),input("Precision Here: ")))

# ------Example ------
# print(Num(37713341,4))
# print(abb(312))
# ------Example ------
