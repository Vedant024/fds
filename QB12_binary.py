def sort(arr):
    for _ in range(len(arr)):
        swp = 0
        j = 0
        while j < len(arr) - 1:
            if arr[j][0] > arr[j+1][0]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swp = 1
            j += 1
        if swp == 0:
            break

def addFriend(arr, name, number):
    arr.append([name, number])
    sort(arr)
    print("Friend added successfully")


def searchFriend(arr, x):
    print("How do you want to search your friend?")
    print("1. Binary Search (Non Recursive)")
    print("2. Binary Search (Recursive)")
    print("3. Fibonacci Search")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        index = binarySearch_nonRecursive(arr, x)
    elif choice == 2:
        index = binarySearch_Recursive(arr, x, 0, len(arr)-1)
    elif choice == 3:
        index = FibonacciSearch(arr, x)
    else:
        print("Invalid choice")
        return
    if index < 0:
        print("Friend not found")
        print("Do you want to add friend? (y/n)")
        ch = input()
        if ch == 'y':
            number = input("Enter mobile number: ")
            addFriend(arr, x, number)
    else:
        print("Friend found")
        print("Name: ", arr[index][0])
        print("Mobile number: ", arr[index][1])


def binarySearch_nonRecursive(arr, x):
    hi = len(arr) - 1
    low = 0
    while True:
        mid = (low + hi)//2
        if x == arr[mid][0]:
            return mid
        elif low == hi:
            return -1
        elif x > arr[mid][0]:
            low = mid + 1
        else:
            hi = mid - 1


def binarySearch_Recursive(arr, x, low, hi):
    mid = (low + hi)//2
    if x == arr[mid][0]:
        return mid
    elif low == hi:
        return -1
    elif x > arr[mid][0]:
        low = mid + 1
        return binarySearch_Recursive(arr, x, low, hi)
    else:
        hi = mid - 1
        return binarySearch_Recursive(arr, x, low, hi)

def FibonacciSearch(arr, x):
    n = len(arr)
    fibMm2 = 0
    fibMm1 = 1
    fibM = fibMm2 + fibMm1 

    while fibM < n: 
        fibMm2 = fibMm1
        fibMm1 = fibM
        fibM = fibMm2 + fibMm1
    
    offset = -1

    while fibM > 1:
        i = min(fibMm2 + offset, n-1)
        if x > arr[i][0]:
            fibM = fibMm1
            fibMm1 = fibMm2
            fibMm2 = fibM - fibMm1
            offset = i
        elif x < arr[i][0]:
            fibM = fibMm2
            fibMm1 = fibMm1 - fibMm2
            fibMm2 = fibM - fibMm1
        else:
            return i

    if fibMm1 and arr[n-1][0] == x:
        return n-1
    else:
        return -1


phonebook = []
choice = 0
while(choice != 4):
    print("What do you want to do?")
    print("1. Add a friend")
    print("2. Search a friend")
    print("3. Display Phonebook")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")
        addFriend(phonebook, name, number)
    elif choice == 2:
        if len(phonebook) == 0:
            print("Phonebook is empty")
        else:
            searchFriend(phonebook, input("Enter name: "))
    elif choice == 3:
        if phonebook == []:
            print("Phonebook is empty")
        else:
            print("\tName\t\tMobile Number")
            for i in phonebook:
                print(i[0], "\t\t", i[1])
    elif choice == 4:
        print("Exiting...\nThank you for using the phonebook program!")
    else:
        print("Wrong input! Please try again.")
    print()