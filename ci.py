import math
principle=int(input("enter principle amount:"))
rate=float(input("enter rate of interest(in%'):"))
time=int(input("enter no of years:"))

ci=principle*(1+rate/100)**time-principle
print("compound interest for provided input is: ",f"{ci:.5f}")
