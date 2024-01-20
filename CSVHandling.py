import csv

def writeData(fname, data):
    with open(fname, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerows(data)

def appendData(fname, data):
    with open(fname, 'a', newline='') as file:
        csvAppend = csv.writer(file)
        csvAppend.writerows(data)

def deleteData(fname, rowIndex):
    with open(fname, 'r') as file:
        csvReader = csv.reader(file)
        data = list(csvReader)
    if rowIndex < len(data):
        del data[rowIndex]
    with open(fname, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerows(data)

def searchByName(fname, nameToSearch):
    found = False
    with open(fname, 'r') as file:
        csvReader = csv.reader(file)
        data = list(csvReader)
        for i in data:
            if i[0].strip().lower() == nameToSearch.lower():
                found = True
                break
        return found

def searchByCity(fname, cityToSearch):
    found = False
    with open(fname, 'r') as file:
        csvReader = csv.reader(file)
        data = list(csvReader)
        for i in data:
            if i[1].strip().lower() == cityToSearch.lower():
                found = True
                break
        return found

def searchByOccupation(fname, occupationToSearch):
    found = False
    with open(fname, 'r') as file:
        csvReader = csv.reader(file)
        data = list(csvReader)
        for i in data:
            if i[2].strip().lower() == occupationToSearch.lower():
                found = True
                break
        return found

def readData(fname):
    with open(fname, 'r',) as file:
        csvReader = csv.reader(file)
        for rows in csvReader:
            print(rows)

def menu():
    i = 0
    fname = input("Enter The File Name: ")
    while True:
        choice = input( "1. To Create a File\n"
                        "2. To Read a File\n"
                        "3. To Delete From a File\n"
                        "4. To Append a File\n"
                        "5. To Search By Name\n"
                        "6. To Search By City\n"
                        "7. To Search By Occupation\n"
                        "8. To Exit\n")
        choice = int(choice)
        if choice == 1:
            while True:
                inputlist = []
                userInput = input("Input Data Separated by Commas(Type 'done' to exit): ")
                if userInput.lower() == 'done':
                    break
                else:
                    finalInput = userInput.split(',')
                    inputlist.append(finalInput)
            writeData(fname, inputlist)
        elif choice == 2:
            readData(fname)
        elif choice == 3:
            rowIndex = input("Enter The Row Number to Delete: ")
            rowIndex = int(rowIndex)
            deleteData(fname, rowIndex - 1)
        elif choice == 4:
            while True:
                inputlist = []
                userInput = input("Input Data Separated by Commas(Type 'done' to exit): ")
                if userInput.lower() == 'done':
                    break
                else:
                    finalInput = userInput.split(',')
                    inputlist.append(finalInput)
                appendData(fname, inputlist)
        elif choice == 5:
            nameToSearch = input("Enter the Name to Search: ")
            found = searchByName(fname, nameToSearch)
            if found:
                print(nameToSearch, "Found!!!")
            else:
                print(nameToSearch, "Not Found!!!")
        elif choice == 6:
            cityToSearch = input("Enter the City to Search: ")
            found = searchByCity(fname, cityToSearch)
            if found:
                print(cityToSearch, "Found!!!")
            else:
                print(cityToSearch, "Not Found!!!")
        elif choice == 7:
            occupationToSearch = input("Enter the Occupation to Search: ")
            found = searchByOccupation(fname, occupationToSearch)
            if found:
                print(occupationToSearch, "Found!!!")
            else:
                print(occupationToSearch, "Not Found!!!")
        else:
            break



"""def main():
    data = [
        ['Name', 'Age', 'Occupation'],
        ['Maximus Decimus Meridius', 40, 'General'],
        ['Julius Caesar', 55, 'Consul'],
        ['Napoleon Bonaparte', 45, 'Emperor']
    ]
    data1 = [
        ['Robert J. Oppenheimer', 56, 'Physicist']
    ]
    fname = "Great Men.csv"
    writeData(fname, data)
    appendData(fname, data1)
    print("Data Written")
    print("Recived Data:")
    readData(fname)
    deleteData(fname, 1)
    print("After Deletion:")
    readData(fname)
"""

def main():
    menu()

main()