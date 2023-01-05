def isHappyNumber(number: int, showProcess: bool = True) -> bool:
    lstNewNumber: list[int] = [int(item) ** 2 for item in str(number)]
    sqrSum: int = sum(lstNewNumber)
    if showProcess:
        print("The process:\n" + str(number) + ": " + ','.join(str(x) for x in lstNewNumber) + " -> " + str(sqrSum))
    return (True if sqrSum == 1 else False) if len(str(sqrSum)) == 1 else isHappyNumber(sqrSum, showProcess)


if __name__ == "__main__":
    print("Hi! ;)")
    while True:
        op = input("Do you want to use range or a specefic numer?(r/s)").lower()
        number = int(input("Please enter an positive integer number:"))
        match op:
            case 'r':
                for i in range(number):
                    print(str(i) + (" is Happy :D" if isHappyNumber(i, False) else " is sad :("))
            case 's':
                print("Your number is Happy :D" if isHappyNumber(number) else "Your number is sad :(" ) 
            case _:
                print("I did not get it! :|")
        if input("Do you want to do it again?(y/n)").lower() != "y":
            break
    print("By! :)")