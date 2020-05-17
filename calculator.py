# a small calc that calculates the basic mathematical functions
# designated functions have been assigned to perform specific tasks
# line 4 and 5 applies to almost all the functions used in this program
# here since the values could potentially be float. Hence, we format the
# output using place holders and assigning the precision i.e {:.2f}


def add(add_list):
    # this function takes in a list as argument and using the sum function
    # we add the elements in the list to get the total.
    # reason we used list because a user might have a groceries list that
    # they would want to calculate
    # here since the values could potentially be float. Hence, we format the
    # output using place holders and assigning the precision i.e {:.2f}
    print("Sum is {:.2f}".format(sum(add_list)))
    add_list.clear()


def subtract(a1, b1):
    # here we just have 2 arguments and we calculate the difference between them
    print("Difference is {:.2f}".format(a1-b1))


def multiply(mr1, mr2):

    print("{} times {} is {}".format(mr1, mr2, mr1 * mr2))


def divide(dv1, dr2):

    print("Division is {}".format(dv1//dr2))


def bmi(w1, h1):
    # the values here 29.9, 24.9, 18.5 are BMI standards set by the WHO

    h_square = h1 * h1
    b_m_i = w1 / h_square  # this can also be written as b_m_i = w1 / h1 * h1
    # print("BMI is {:.2f}".format(b_m_i))
    if 25 < b_m_i <= 29.9:
        print("BMI is {:.2f}. You are overweight.".format(b_m_i))
    elif 18.5 <= b_m_i <= 24.9:
        print("BMI is {:.2f}. You are under safe weight zone.".format(b_m_i))
    else:
        print("BMI is {:.2f}. You are underweight.".format(b_m_i))


def square_pow(p1):
    # here the power func takes 2 arguments, number and the power to raise to
    # since it is a square function we assign 2 manually, which is the 2nd argument of pow func
    print("Square of {} is {:.2f}".format(p1, pow(p1, 2)))


print("Select option below. ")
print("""\t\t1.Add
        2.Subtract
        3.Multiply
        4.Divide
        5.Square
        6.BMI(Body Mass Index)""")

while True:
    option = input()
    if option == "1":
        lst1 = []
        n = int(input("How many numbers you want to add? "))
        print("Please enter the numbers you want to add: ")
        for i in range(0, n):
            ele = float(input())
            lst1.append(ele)
        add(lst1)
        print("Select option to continue or type exit to exit.")

    elif option == "2":
        print("Enter the numbers you want to subtract: ")
        a = float(input())
        b = float(input())
        subtract(a, b)
        print("Select option to continue or type exit to exit.")

    elif option == "3":
        print("Enter the numbers to multiply")
        m1 = float(input())
        m2 = float(input())
        multiply(m1, m2)
        print("Select option to continue or type exit to exit.")

    elif option == "4":
        print("Dividend: ")
        dv = float(input())
        print("Divisor: ")
        dr = float(input())
        divide(dv, dr)
        print("Select option to continue or type exit to exit.")

    elif option == "5":
        print("Enter number to calculate square. ")
        p = float(input())
        square_pow(p)
        print("Select option to continue or type exit to exit.")

    elif option == "6":
        print("Enter Weight in kg: ")
        w = float(input())
        print("Enter height in cm: ")
        h = float(input())
        bmi(w, h / 100)   # here the height gets converted into metres(m) before passing it to the func.
        print("Select option to continue or type exit to exit.")

    if option == "EXIT".lower():
        break



