print("                          WELCOME TO PYTHON LEARNING "    )                  

name=str(input("what is ur name: "))
div=int(input("what is ur class: "))


print("*"*80)
num1=int(input("n1"))
num2=int(input("n2"))
num3=int(input("n3"))
sum=num1+num2+num3
print("the no. are:",num1, num2, num3)
print("sum=",sum)

print("*"*80)


sp=float(input("sp: "))
gst_rate=float(input("gst_rate: "))
cgst=sp*((gst_rate/2)/100)
sgst=cgst
print("  "*10, "bill for ur product" )
print("selling price = ",sp)
print("cgst = ",cgst)
print("sgst = ",sgst)
print("total= sp+cgst+sgst = ",sp+sgst+cgst)
