n=float(input("Enter price of product"))
if n>=200 and n<500:
  a=n-(n*0.1)
elif n>=500 and n<1000:
  a=n-(n*0.3)
elif n>=1000:
  a=n-(n*0.5)
else:
  a=n
  print("You are not eligible for a discount")
print("Total amount you have to pay is ",a)
