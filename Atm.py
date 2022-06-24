class Atm:
    def __init__(self , cardnumber , pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("your balancee is : $100")

    def cashwithdrawl(self,amount):
        new_amount = 100-amount
        print("you withdrawed: " + str(amount) + " your remaining blance is: " + str(new_amount))

def main():
        name = input("Hello what is your name?")
        print("Hello " + name)
        cardnumber = input("Insert your card number: ")
        pin = input("enter your pin: ")
        new_user = Atm(cardnumber , pin)

        print("Choose your activity")
        print("1. Balance Enquiry")
        print("2. Cash Withdrawal")
        activity = int(input("Enter activity choice: "))

        if(activity == 1):
            new_user.balanceinquiry()
        elif(activity == 2):
            amount = int(input("enter the amount : "))
            new_user.cashwithdrawl(amount)
        else:
            print("Enter a valid number")


if __name__ == "__main__":
        main()
