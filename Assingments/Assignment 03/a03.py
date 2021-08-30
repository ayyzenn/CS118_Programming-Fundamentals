### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget, bashir_budget):
    if type(ali_budget) == str or type(bashir_budget) == str:
        return "Not Possible"
    elif ali_budget<0 or bashir_budget<0:
        return "Not Possible"
    else:
        m = 0
        a= ali_budget
        b= bashir_budget
        if a > b:
            m = b
        else:
            m = a
    for i in range(1, m+1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i 
    return hcf        

def Totalchocolate(ali_budget, bashir_budget):
    if type(ali_budget) == str or type(bashir_budget) == str:
        return "Not Possible"
    elif ali_budget<=0 or bashir_budget<=0:
        return "Not Possible"
    else:
        a= chocolatePrice(ali_budget,bashir_budget)
        x=ali_budget//a
        y=bashir_budget//a
        return x,y
print(Totalchocolate(12,56))

#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
def calculateProfit(ali_budget, bashir_budget):
    if type(ali_budget) == str or type(bashir_budget) == str:
        return "Not Possible"
    elif ali_budget>0 and bashir_budget>0:
        i=0
        t=0
        o=0
        Ali_profit=0
        Bashir_profit=0
        t= chocolatePrice(ali_budget,bashir_budget)
        i=ali_budget//t
        o=bashir_budget//t
        Ali_profit= t*2* (i)
        Bashir_profit=t*(1.5)*(o)
        totalpro = Ali_profit - ali_budget 
        totalpro2 = Bashir_profit - bashir_budget
    else:
        return"Not Possible"
    return int(totalpro) , int(totalpro2)
calculateProfit(1,12)






#### End OF MARKER


