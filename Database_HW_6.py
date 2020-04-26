## Matt Hopkins
## Homework 6
## April 25th 2020

##note to self must be in 32 bit
import mysql.connector 

def menu():
    print ("\n1 -> prints table for login\n" +
           "2 -> prints table for accounts\n" +
           "3 -> prints table for joined table\n" +
           "4 -> Login and print users account\n" +
           "5 -> Login and print users account with secure login\n" +
           "6 -> Update balance\n" +
           "7 -> Switch to restricted user\n" +
           "8 -> Swith to admin user\n")
    
def printLogin(mycursor):
    mycursor.execute("SELECT * FROM login ")
    for i in mycursor:
        print(i)

def printAccounts(mycursor):
    mycursor.execute("SELECT * FROM accounts")
    for i in mycursor:
        print(i)

def printJoinedTable(mycursor):
    mycursor.execute("SELECT accounts.userName, actualName, accountNumber, balance, userPw FROM login JOIN accounts ON login.userName = accounts.userName;")
    for i in mycursor:
        print(i)

def printBalance(mycursor):
    userName = input("Please enter login name -> ")
    userPw = input("Please enter userPw ->")
    login = "Select * FROM login JOIN accounts ON login.userName = accounts.userName WHERE login.userName = '" + userName + "' and userPw = '" + userPw + "';"
    mycursor.execute(login)
##    mycursor.execute(login, multi = True) ## doesn't work
    for i in mycursor:
        print("hi")
        print(i)

def printBalanceProtected(mycursor):
    userName = input("Please enter login name -> ")
    userPw = input("Please enter userPw ->")
    mycursor.execute("SELECT * FROM  login JOIN accounts ON login.userName = accounts.userName WHERE login.userName = %s AND login.userPw = %s", (userName, userPw))
    for i in mycursor:
        print(i)

def updateBalance(mycursor):
    userName = input("Please enter login name -> ")
    amount = int(input("Enter amount, can be negative to debit account -> "))
    try:
        mycursor.execute("UPDATE accounts SET balance = " + str(amount) + " WHERE userName = '" + userName + "';")
    except mysql.connector.errors.ProgrammingError:
        print("\nSorry you do not have access to update accounts\n")
        
def switchToRestrictedUser():
    print("\nLogging on as Restriced User\n")
    db = mysql.connector.connect(
        host = "localhost",
        user = "new_user",
        passwd = "password",
        database="HW6_v2"
        )
    return db

def switchToAdminUser():
    print("\nLogging on as Admin User\n")
    db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="root",
    database="HW6_v2"
    )
    return db
    
db = switchToAdminUser()

while True:
    menu()
    mycursor = db.cursor()
    userSelection = input("Enter menu choice ==> ")
    if userSelection == '1':
        printLogin(mycursor)
    elif userSelection == '2':
        printAccounts(mycursor)
    elif userSelection == '3':
        printJoinedTable(mycursor)
    elif userSelection == '4':
        printBalance(mycursor)
    elif userSelection == '5':
        printBalanceProtected(mycursor)
    elif userSelection == '6':
        updateBalance(mycursor)
    elif userSelection == '7':
        db.close()
        db = switchToRestrictedUser()
    elif userSelection == '8':
        db.close()
        db = switchToAdminUser()
    else:
        break;
db.close()



