#!/usr/bin/env python
import sys

def getPurchaseChange(change_needed):
    oneBills = 0
    fiveBills = 0
    tenBills = 0
    twentyBills = 0
    while change_needed >= 20:
        change_needed = change_needed - 20
        twentyBills += 1
    while change_needed >= 10 and change_needed < 20:
        change_needed = change_needed - 10
        tenBills += 1
    while change_needed >= 5 and change_needed < 10:
        change_needed = change_needed - 5
        fiveBills += 1
    while change_needed >= 1 and change_needed < 5:
        change_needed = change_needed - 1
        oneBills += 1
    return oneBills, fiveBills, tenBills, twentyBills

def init(array, lineSplit, lines):
    for element in lineSplit:
        try:
            new_int = int(element)
            if new_int < 0:
                print "Return code = 1: Bad arguments"
                return "Return code = 1: Bad arguments"
        except ValueError:
            pass
    if len(lineSplit) < 4:
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"
    if  len(lineSplit) < 7 and len(lineSplit) > 4:
        while len(lineSplit) < 7:
            lineSplit.append(0)
    if len(lineSplit) > 7:
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"
    if lineSplit[2] != "=":
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"
    try:
        int(lineSplit[1])
    except ValueError:
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"
    for i in range (3,7):
        try:
            int(lineSplit[i])
        except ValueError:
            print "Return code = 1: Bad arguments"
            return "Return code = 1: Bad arguments"
    file = open("dataRecord.txt", "w")
    # initilize register to 0 (new shift)
    ones = 0
    fives = 0
    tens = 0
    twenties = 0
    sales = 0
    file.write("0\n")  # ones
    file.write("0\n")  # fives
    file.write("0\n")  # tens
    file.write("0\n")  # twenties
    file.write("0\n")  # sales
    file = open("dataRecord.txt", "r")
    register_total = lineSplit[1]  # Get register input
    ones += int(lineSplit[3])  # Get amount of ones
    fives += int(lineSplit[4])  # Get amount of fives
    tens += int(lineSplit[5])  # Get amount of tens
    twenties += int(lineSplit[6])  # Get amounts of twenties
    file = open("dataRecord.txt", "w")
    file.write(str(ones))  # ones
    file.write("\n")
    file.write(str(fives))  # fives
    file.write("\n")
    file.write(str(tens))  # tens
    file.write("\n")
    file.write(str(twenties))  # twenties
    file.write("\n")
    file.write(str(sales))  # sales

    # Get ones, fives, tens, twenties, and sales data from .txt file
    file = open("dataRecord.txt", "r")
    for line in open('dataRecord.txt'):
        array.append(line)
        array[-1] = array[-1].strip()
    ones = array[0]
    fives = array[1]
    tens = array[2]
    twenties = array[3]
    sales = array[4]
    print ones, fives, tens, twenties
    print "Return code = 0: SUCCESS"

def purchase(array, lineSplit, lines):

    if len(lineSplit) < 4:
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"
    if  len(lineSplit) < 7 and len(lineSplit) > 4:
        while len(lineSplit) < 7:
            lineSplit.append(0)
    if len(lineSplit) > 7:
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"
    if lineSplit[2] != "=":
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"
    try:
        int(lineSplit[1])
    except ValueError:
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"
    for i in range (3,7):
        try:
            int(lineSplit[i])
        except ValueError:
            print "Return code = 1: Bad arguments"
            return "Return code = 1: Bad arguments"
    file = open("dataRecord.txt", "r")
    for line in open('dataRecord.txt'):
        array.append(line)
        array[-1] = array[-1].strip()
    ones = array[0]
    ones_int = int(ones)
    fives = array[1]
    fives_int = int(fives)
    tens = array[2]
    tens_int = int(tens)
    twenties = array[3]
    twenties_int = int(twenties)
    sales = array[4]
    sales_int = int(sales)

    purchase_total = int(lineSplit[1])  # Get purchase total
    input_ones = int(lineSplit[3])  # Get number of ones
    input_fives = int(lineSplit[4])  # Get number of fives
    input_tens = int(lineSplit[5])  # Get number of tens
    input_twenties = int(lineSplit[6])  # Get number of twenties
    billTotal = (
            input_ones * 1 + input_fives * 5 + input_tens * 10 + input_twenties * 20)  # Get total amount customer gave
    if purchase_total > billTotal:
        print "Return code = 2: Amounts don't jibe"
        return 0
    change = billTotal - purchase_total  # find change we need to give back
    changeInBills = getPurchaseChange(change)  # Determine which bills to give
    for billType in range(0, len(changeInBills)):  # print bill type
        print changeInBills[billType],
    print ""  # end same line print
    input_sales = purchase_total
    new_sales = input_sales + int(sales)
    file = open("dataRecord.txt", "w")
    file.write(str((ones_int + input_ones) - int(changeInBills[0])))  # ones
    file.write("\n")
    file.write(str((fives_int + input_fives) - changeInBills[1]))  # fives
    file.write("\n")
    file.write(str((tens_int + input_tens) - changeInBills[2]))  # tens
    file.write("\n")
    file.write(str((twenties_int + input_twenties) - changeInBills[3]))  # twenties
    file.write("\n")
    file.write(str(new_sales))  # ones
    print "Return code = 0: SUCCESS"

def change(array, lineSplit, lines):
    file = open("dataRecord.txt", "r")
    for line in open('dataRecord.txt'):
        array.append(line)
        array[-1] = array[-1].strip()
    ones = array[0]
    ones_int = int(ones)
    fives = array[1]
    fives_int = int(fives)
    tens = array[2]
    tens_int = int(tens)
    twenties = array[3]
    twenties_int = int(twenties)
    sales = array[4]
    sales_int = int(sales)

    if len(lines) != 24:
        leftOfEquals = []
        rightOfEquals = []
        i = 0
        for item in lineSplit[1:]:
            if item == "=":
                equalsSign = lineSplit[i + 1]
                index = i + 1
            i += 1
        try:
            for left_int in range(1, index):
                leftOfEquals.append(lineSplit[left_int])
            for right_int in range(index + 1, len(lineSplit)):
                rightOfEquals.append(lineSplit[right_int])
        except UnboundLocalError:
            print "Return code = 1: Bad arguments"
            return "Return code = 1: Bad arguments"
        while len(leftOfEquals) < 4:
            leftOfEquals.append(0)
        while len(rightOfEquals) < 4:
            rightOfEquals.append(0)
    else:
        leftOfEquals = []
        rightOfEquals = []
        i = 0
        for item in lineSplit[1:]:
            if item == "=":
                equalsSign = lineSplit[i + 1]
                index = i + 1
            i += 1
        for left_int in range(1, index):
            leftOfEquals.append(lineSplit[left_int])
        for right_int in range(index + 1, len(lineSplit)):
            rightOfEquals.append(lineSplit[right_int])
        while len(leftOfEquals) < 4:
            leftOfEquals.append(0)
        while len(rightOfEquals) < 4:
            rightOfEquals.append(0)
    try:
        changeForAmount = int(leftOfEquals[0]) * 1 + int(leftOfEquals[1]) * 5 + int(leftOfEquals[2]) * 10 + int(
            leftOfEquals[3]) * 20
        requestedChangeAmount = int(rightOfEquals[0]) * 1 + int(rightOfEquals[1]) * 5 + int(
            rightOfEquals[2]) * 10 + int(rightOfEquals[3]) * 20
    except ValueError:
        print "Return code = 1: Bad arguments"
        return "Return code = 1: Bad arguments"

    file = open("dataRecord.txt", "w")
    onesToWrite = (ones_int + int(leftOfEquals[0])) - int(rightOfEquals[0])
    fivesToWrite = (fives_int + int(leftOfEquals[1])) - int(rightOfEquals[1])
    tensToWrite = (tens_int + int(leftOfEquals[2])) - int(rightOfEquals[2])
    twentiesToWrite = (twenties_int + int(leftOfEquals[3])) - int(rightOfEquals[3])
    if onesToWrite < 0 or fivesToWrite < 0 or tensToWrite < 0 or twentiesToWrite < 0:
        print "Return code = 3: Drawer has insufficient money or denominations to make proper change"
        return "Return code = 3: Drawer has insufficient money or denominations to make proper change"

    file.write(str(onesToWrite))  # ones
    file.write("\n")
    file.write(str(fivesToWrite))  # fives
    file.write("\n")
    file.write(str(tensToWrite))  # tens
    file.write("\n")
    file.write(str(twentiesToWrite))  # twenties
    file.write("\n")
    file.write(str(sales_int))  # ones

    if changeForAmount == requestedChangeAmount:
        for item in rightOfEquals:
            print item,
        print ""
        print "Return code = 0: SUCCESS"
    else:
        print "Return code = 2: Amounts don't jibe"
        return "Return code = 2: Amounts don't jibe"



def report(array, lineSplit, lines):
    try:
        file = open("dataRecord.txt", "r")
    except IOError:
        print "Return code = 4: Unable to read/write data file"
    for line in open('dataRecord.txt'):
        array.append(line)
        array[-1] = array[-1].strip()
    ones = array[0]
    ones_int = int(ones)
    fives = array[1]
    fives_int = int(fives)
    tens = array[2]
    tens_int = int(tens)
    twenties = array[3]
    twenties_int = int(twenties)
    sales = array[4]
    sales_int = int(sales)

    print sales_int, " : ", (
            ones_int * 1 + fives_int * 5 + tens_int * 10 + twenties_int * 20), " = ", ones_int, " ", fives_int, " ", tens_int, " ", twenties_int
    print "Return code = 0: SUCCESS"

def main():
    try:
        file = open("dataRecord.txt", "r")
    except IOError:
        print "Return code = 4: Unable to read/write data file"
    try:
        with open(sys.argv[1], "r") as fileinput:
            pass
    except IOError:
        print "Return code = 4: Unable to read/write data file"
        return "Return code = 4: Unable to read/write data file"
    with open(sys.argv[1], "r") as fileinput:
        # for expression in f:
        for expression in fileinput:
            lines = expression.strip()
            lineSplit = lines.split()
            array = []
            try:
                if lineSplit[0] == "init":
                    init(array, lineSplit, lines)
                if lineSplit[0] == "purchase":
                    purchase(array, lineSplit, lines)
                if lineSplit[0] == "change":
                    change(array, lineSplit, lines)
                if lineSplit[0] == "report":
                    report(array, lineSplit, lines)

                if (lineSplit[0] != "init") and (lineSplit[0] != "purchase") and (lineSplit[0] != "change") and (lineSplit[0] != "report"):
                    if expression[0] == "#":
                        print expression
                        continue
                    print "Return code = 1: Bad arguments"
            except IndexError:
                print "Return code = 1: Bad arguments"
if __name__ == '__main__':
    main()
