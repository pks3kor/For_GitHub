#~ tmp = {<key>:<val>}
def sum(x,y):
    return x+y
tmp = {"A":123,"B":456,"C":789}
tmp2 = {123:"A",("A","B"):[1,2,3]}
tmp3 = {sum(1,2):"A",sum(2,1):"B"}
#~ print tmp2[("A","B")]
tmp4 = {"A":1,"B":{"A":2,"B":[5,6,7]},
    "C":(1,2,3)}
print tmp4["B"]["B"][::-1]
    
