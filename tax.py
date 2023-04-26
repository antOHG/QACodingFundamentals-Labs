
# Lab 6 - tax calculations


# Personal allowance:	£11,850	 
# 0 to 34,500 			taxed at 20%		
# 34,501 to 150,000 	taxed at 40%		
# Over 150,000 			taxed at 45%		
  

def getIncomeTax(salary):

    # Calculate user_input
    if salary < 11850:
        return 0
    elif 11850 <= salary <= 34500: 
        return (salary - 11850) * 0.2
    elif 34501 <= salary <= 150000: 
        return 4530 + ((salary - 34500) * 0.4)
    else:
        return 50730 + ((salary - 150000) * 0.45) 

salary = 100000
tax_amount = getIncomeTax(salary)
print("Tax amount for salary £{} is £{}".format(salary.tax_amount))

getIncomeTax(salary)



