#q7_generate_payroll.py
#generates payroll based on information given

#input variables

name = str(input("Enter name: "))
hours_worked = int(input("Enter number of hours worked weekly: "))
rate = float(input("Enter hourly pay rate: "))
CPF_rate = int(input("Enter CPF contribution rate(%): "))

#process variables
gross_pay = hours_worked * rate
CPF = (CPF_rate / 100) * gross_pay
net_pay = gross_pay - CPF

#display results
print("Payroll statement for",name)
print("Number of hours worked weekly:",hours_worked)
print("Hourly pay rate:{0:.2f}".format(rate))
print("Gross pay: ${0:.2f}".format(gross_pay))
print("CPF contribution at {0}%:${1:.2f}".format(CPF_rate,CPF))
print()
print("Net Pay: ${0:.2f}".format(net_pay))
