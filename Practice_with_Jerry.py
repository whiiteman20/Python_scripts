# Employee A: 15.62 miles
# Employee B: 41.85 miles
# Employee C: 32.67 miles
# solution accepts three integer inputs representing the number of times an employee travels to the job site
# solution outputs "Distance: " followed by the total value to two decimal places

# Emp_A = 15.62
# Emp_B = 41.85
# Emp_C = 32.67
#
# first_int = int(input())
# second_int = int(input())
# third_int = int(input())
#
# total_miles_traveled = (Emp_A * first_int) + (Emp_B * second_int) + (Emp_C * third_int)
#
# print("Distance: {:.2f} miles".format(total_miles_traveled))
###################################################################################################################
# there are 16 ounces in a pound and 2000 pounds in a ton
# solution accepts an integer value representing any number of ounces
# solution outputs the converted tons, pounds, and ounces represented by the input value of ounces
# user_int = int(input())
#
# tons = user_int // 32000
# user_int = user_int % 32000
# pounds = user_int // 16
# user_int = user_int % 16
# ounces = user_int
#
# print("Tons: {}\nPounds: {}\nOunces: {}".format(tons, pounds, ounces))
##################################################################################################################
# various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
#
# use built-in function type()
# get name by using the built-in attribute __name__
# solution accepts integer input representing list element index
# solution outputs data type of list element based on input index value
#
# index = int(input())
#
# for item in various_data_types:
#    if item == various_data_types[index]:
#        print("Element {}: {}".format(index, type(item).__name__))
################################################################################################################
# solution accepts three integer values representing base and height measurements of a trapezoid
# first and second integers represent base 1 and base 2; third integer represents height
# solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h
#
# b1 = int(input())
# b2 = int(input())
# h = int(input())
#
# A = ((b1 + b2) / 2) * h
#
# print("Trapezoid area: {:.1f} square meters".format(A))
###############################################################################################################
# solution accepts five integer inputs
# solution outputs three sums of input values; convert before calculating sum
# first output: sum of five inputs maintained as integer values
# second output: sum of five inputs converted to float values
# third output: sum of five inputs converted to string values (concatenate)

# int_1 = int(input())
# nt_2 = int(input())
# nt_3 = int(input())
# int_4 = int(input())
# int_5 = int(input())
#
# int_added = int_1 + int_2 + int_3 + int_4 + int_5
# float_convert = float(int_1) + float(int_2) + float(int_3) + float(int_4) + float(int_5)
# str_convert = str(int_1) + str(int_2) + str(int_3) + str(int_4) + str(int_5)
#
# print("Integer: {}\nFloat: {:.1f}\nString: {}".format(int_added, float_convert, str_convert))
########################################################################################################
# hint: modulo (%) and floored division (//) may be used
# solution accepts a 9-digit integer representing an unformatted student identification number (i.e.,"5417543010")
# solution outputs formatted student identification number as a string (i.e.,"541-75-3010")
#
# user_int = int(input())
#
# str_convert = str(user_int)
#
# print(str_convert[0:3] + '-' + str_convert[3:5] + '-' + str_convert[5:9])
########################################################################################################
# predef_list = [4, -27, 15, 33, -10]
#
# solution accepts an integer input
# solution outputs Boolean value indicating if integer input is greater
# than the maximum value when compared to predef_list
#
# user_num = int(input())
#
# if user_num > max(predef_list):
#    print("Greater Than Max?", True)
# else:
#    print("Greater Than Max?", False)
###################################################################################################
# frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
#
# use try block with exception "Error" when index value is not found in list
# solution accepts an integer input
# solution outputs the corresponding string value for the integer input
#
# index = int(input())
#
# try:
#    for framework in frameworks:
#        if framework == frameworks[index]:
#            print(framework)
# except IndexError:
#    print("Error")
################################################################################################
# temperature >= 212, water state is "Boiling"
# temperature (115, 211], water state is "Hot"
# temperature [80, 115], water state is "Warm" --done
# temperature [33, 80), water state is "Cold" --done
# temperature < 33, water state is "Frozen" --done
# temperature = 212, safety comment "Caution: Hot!"
# temperature < 33, safety comment "Watch out for ice!" --done
# solution accepts integer input representing a water temperature
# solution outputs the water state and potential safety comment based on temperature
#
# temperature = int(input())
#
# if temperature < 33:
#    print("Frozen")
#    print("What out for ice!")
# elif temperature >= 33 and temperature < 80:
#    print("Cold")
# elif temperature >= 80 and temperature < 115:
#    print("Warm")
# elif temperature >= 115 and temperature < 211:
#    print("Hot")
# elif temperature >= 212:
#    print("Boiling")
#    if temperature == 212:
#        print("Caution: Hot!")
######################################################################################################
# stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92,
#          'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}
#
# solution accepts an integer input representing the number of stock selections
# solution accepts string inputs equivalent to the integer input identifying the stock selections
# solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places
#
# stocks_amount = int(input())
#
# stocks_we_want = []
#
# while len(stocks_we_want) < stocks_amount:
#    stock = input("What stock would you like?\n")
#    if stock in stocks.keys():
#        stocks_we_want.append(stocks.get(stock))
#
# print(stocks_we_want)
#
# print(f"Total price: ${sum(stocks_we_want):.2f}")
############################################################################################################
# purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}
#
# cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
# solution accepts a string input representing an item (dictionary key)
# solution accepts an integer input representing the number of items to be purchased
# solution outputs the item and total cost of purchase
#
# item_we_want = input()
# amount_of_item = int(input())
#
# if item_we_want in purchase:
#    if amount_of_item < 10:
#        print(f"{item_we_want} ${(amount_of_item * purchase.get(item_we_want)):.2f}")
#    elif amount_of_item >= 10 and amount_of_item <= 20:
#        discount = (amount_of_item * purchase.get(item_we_want) * 0.05)
#        print(f"{item_we_want} ${((amount_of_item * purchase.get(item_we_want)) - discount):.2f}")
#    elif amount_of_item > 20:
#        discount = (amount_of_item * purchase.get(item_we_want) * 0.10)
#        print(f"{item_we_want} ${((amount_of_item * purchase.get(item_we_want)) - discount):.2f}")
#############################################################################################################
#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence
#
#with open("WordTextFile1.txt", 'r') as file:
#    read_file = file.readlines()
#    for word in read_file:
#        print(word.replace('\n', ''))
#    new_str = ''.join(read_file)
#    print(new_str.replace('\n', ' '))
#############################################################################################################
#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file (i.e., "input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements
#import csv
#
#file = input()
#
#with open(file, 'r') as file:
#    contents = list(csv.reader(file, delimiter=','))
#
#for row in contents:
#    content_dict = {}
#    for item in range(len(row)):
#        if item % 2 == 0:
#            content_dict[row[item].strip()] = row[item + 1].strip()
#    print(content_dict)
###########################################################################################################
#
#rand_dict = {}
#rand_list = [10, "me", 20, "please"]
#
#for item in range(0, len(rand_list), 2):
#    key = rand_list[item]
#    value = rand_list[item + 1].strip()
#    rand_dict[key] = value
#
#print(rand_dict)
#
# 1 pound into 5 gallons
# how to put 1 pounds into 2 gallons
print(2/5)
print(1*0.4)