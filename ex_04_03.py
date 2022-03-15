##################################################
# ex_04_o3  Functions in Python - beginner's class

################## function computepay - returns pay based on passed rate and number of hours
def computepay(h, r):
    ######### Pay for the first 40 hours
    BasePay = 40 * r

    ############ Additional Hours
    if (h > 40):
        AddedPay = (h - 40) * r * 1.5
    else:
        AddedPay = 0
        
    GrossPay = BasePay + AddedPay

    return GrossPay

#################  Main function runs below
hrs = input("Enter Hours:")
fHours = float(hrs)


rate = input("Enter Pay:")
fRate = float(rate)

p = computepay(fHours, fRate)

print("Pay", p)

