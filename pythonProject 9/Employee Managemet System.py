#Employee management system using list

#Employee name
Employee_1 = input(["Emoloyee name 1:"])
print(Employee_1.center(50,'*'))
Employee_2 = input(["Emoloyee name 2:"])
print(Employee_2.center(50,'*'))
Employee_3 = input(["Employee name 3:"])
print(Employee_3.center(50,'*'))

#Employee id
Employee_id_1 = input(["Employee id 1:"])
print(Employee_id_1.center(50,'*'))
Employee_id_2 = input(["Employee id 2:"])
print(Employee_id_2.center(50,'*'))
Employee_id_3 = input(["Employee id 3:"])
print(Employee_id_3.center(50,'*'))

#Employee Mobile number
E_M_1 = input(["Enter Employee Number 1:"])
print(E_M_1.center(50,'='))
E_M_2 = input(["Enter Employee Number 2:"])
print(E_M_2.center(50,'='))
E_M_3 = input(["Enter Employee Number 3:"])
print(E_M_3.center(50,'='))

#Employee Address
E_A_1 = input(["Enter Employee Address 1:"])
print(E_M_1.center(50,'*'))
E_A_2 = input(["Enter Employee Address 2:"])
print(E_M_2.center(50,'*'))
E_A_3 = input(["Enter Employee Address 3:"])
print(E_M_3.center(50,'*'))

#Salary of Employee
Salary_1 = 20000
print(Salary_1)
Salary_2 = 15000
print(Salary_2)
Salary_3 = 30000
print(Salary_3)

#Employee 1 Incentive
TA_1 = 20000 * 2/100
DA_1 = 20000 * 5/100
HRA_1 = 20000 * 20/100
PF_1 = 20000 * 18/100

#Employee 2 Incentive
TA_2 = 15000 * 2/100
DA_2 = 15000 * 5/100
HRA_2 = 15000 * 20/100
PF_2 = 15000 * 18/100

#Employee 3 incentive
TA_3 = 30000 * 2/100
DA_3 = 30000 * 5/100
HRA_3 = 30000 * 20/100
PF_3 = 30000 * 18/100

#Total salary of Employee 1
Totalsalary_1 = Salary_1 + TA_1 + DA_1 + HRA_1 - PF_1

#Total salary of Employee 2
Totalsalary_2 = Salary_2 + TA_2 + DA_2 + HRA_2 - PF_2

#Total salary of Employee 3
Totalsalary_3 = Salary_3 + TA_3 + DA_3 + HRA_3 - PF_3


print(Totalsalary_1)
print(Totalsalary_2)
print(Totalsalary_3)








