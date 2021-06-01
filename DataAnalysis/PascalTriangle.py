while(True):
    try:
        n=int(input("please enter the number of rows:"))
    except ValueError:
        print("error! please enter again")
    else:
        print("Received n")
        break
