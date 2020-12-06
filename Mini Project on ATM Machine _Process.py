import time
print('Welcome to the Login Page')
import sqlite3
file = sqlite3.connect('Bank_Project.db')
cur = file.cursor()

cur.execute("""create table if not exists Bank_records(Si_No INTEGER PRIMARY KEY AUTOINCREMENT,Username text,Pin int,Total_Amount int,Mini_statement text) """)
print('Table is created ')
file.commit()

def Insert(User,Pin,Amount):
    cur.execute('insert into Bank_records(Username,Pin,Total_Amount) values(?,?,?)',(User,Pin,Amount))
    print('The Data is inserted');print()
    file.commit()
Username = cur.execute('select Username from Bank_records')
# Insert('Rahul',1552,5600)
# Insert('Dravid',2564,48000)
# Insert('Dhoni',1094,30000)
# Insert('Sachin',4568,56000)
# Insert('Kohili',7895,11000)

# This is getting theinformation from the Database and reading and adding into the Dictonary

username = []
pin = []
for x in Username:
    username.append(x)    
Pin = cur.execute('select Pin from Bank_records')
pin = []
for y in Pin:
    pin.append(y)

data = dict(zip(username,pin))

print(data)
user = input('Enter the Username : ');
pin = int(input('Enter the Pin: '));

restart = 'Y'
try:
    if data[(user,)] == (pin,):
        print('Please wait . We are checking the details....')
        time.sleep(5)
        print('Congratulations You Sucessfully Login .....');print()

        while True:
            if restart in ('Y','yes','YES','Yes','y','continue','Conti','con','Continue','CONTINUE','continue'):
                print('\tWelcome to the "DHANA-LAKSHMI" BANK');print()
                print("The following options are available below :");
                print("\t1.Balance   \t\t2.Withdraw");
                print("\t3.Pinchange \t\t4.Deposit");print()
                print()
                Option = int(input("Choose your choice : "))

                if Option == 1:
                    def Balance():
                        Amount = cur.execute("select Username,Pin,Total_Amount from Bank_records")
                        for x in Amount:
                            if x[0]== user:
                                print("The Available balance in your account is Rs=",str(x[2])+'/-')

                    Balance()
                    restart = input('Do want Continue or Exit :')
                    print();print();print()

                if Option == 2:
                    Amount = int(input('Please enter the Amount :'))
                    def Withdraw(Amount):
                        Bal = cur.execute('select Username,Total_Amount from Bank_records')
                        for x in Bal:
                            if x[0] == user:
                                if x[1]>=Amount:
                                    Give = x[1]-Amount
                                    print('Please wait for transaction...')
                                    time.sleep(5)
                                    print('Please collect the Amount Rs='+str(Amount)+'/-');
                                    time.sleep(5)
                                    def Update(Give,user):
                                        cur.execute("update Bank_records set Total_Amount = {} where Username ='{}'".format(Give,user))
                                        print('The Updatetion is sucessfully done')
                                        file.commit()
                                    Update(Give,user)
                                else:
                                    print('Insufficient funds in your account')
                                    print('Try again latter !')
                    Withdraw(Amount)
                    restart = input('Do want continue or Exit :')
                    print();print()

                if Option == 3:
                    Old = int(input('Please enter the Old pin Number : '))
                    if Old == pin:
                        New = int(input('Please Enter the New Pin Number :'))
                        Confirm = int(input('Please confirm the New Pin Number :'))
                        if New == Confirm :
                            def Update(New):
                                cur.execute('update Bank_records set Pin={} where Pin = {}'.format(New,Old))
                                print('Please wait we are changing the Pin Number')
                                time.sleep(5)
                                print('The Pin is Updated sucessfully');print()
                                file.commit()
                            Update(New)
                        else:
                            print('You New pin is doesn\'t match ')
                    restart = input('Do want continue or Exit :');
                    print();print()

                if Option == 4:
                    Pin = int(input('Please confirm the Pin Number :'));
                    if Pin == pin:
                        Amount = int(input('How much Amount do want to deposit :'));
                        Bal = cur.execute('select Username ,Total_Amount from Bank_Records');
                        for x in Bal:
                            if x[0]==user:
                                Total = x[1]+Amount
                                def Update(Total,user):
                                    cur.execute("update Bank_records set Total_Amount = {} where Username = '{}'".format(Total,user))
                                    print('Please wait we are varifying your account')
                                    time.sleep(5)
                                    print("The Deposited sucessfully Done");print()
                                    file.commit()

                                Update(Total,user)
                    restart = input('Do want continue or Exit :')
                    print()

    else:
        print("Please wait...!!!!")
        time.sleep(5)
        print()
        print("Entered Detail's is wrong")
        print('sorry try again latter !!!\nAfter Sometime....')


except Exception as As:
        print("There is no Records on this Username and Password")
file.close()
            
