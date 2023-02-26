import csv
import os
import pandas as pd
import time

class Bank():

    def __init__(self):
        self.loggedin = False
        self.cash = 0
        self.transferCcash = False
        self.user_field = ['Name', 'Mobile No', 'Email ID', 'Balance', 'Account Type', 'Account No', ]
        self.log_details = ['Email ID', 'Password']
        self.trans = ['Transaction ID', 'Note']
        self.acc = 66
        self.admin_login = False

    def register(self, name, ph, mail, password, account_type, cash, DoB):
        cash = self.cash + cash
        account_no = self.acc * ph + DoB
        trans_id = account_no + ph
        contitions = True
        note = f"Account Created Successfully, With Balance of: {cash}"
        if cash >= 1000:
            if len(str(ph)) > 10 or len(str(ph)) < 10:
                print('Invalid Phone Number! Please Enter 10 digit Number')
                contitions = False

            elif len(password) < 5 or len(password) > 18:
                print('Enter password greater than 5 and less than 18 character')
                contitions = False

            elif contitions == True:
                if os.path.exists(f'{name}.csv'):
                    print('Custumer Exist')

                else:
                    if account_type in ['saving', 'current']:
                        with open(f'{name}.csv', 'w', newline='') as user_details:
                            writer = csv.DictWriter(user_details, fieldnames=self.user_field)
                            writer.writeheader()
                            writer.writerow({'Name': name, 'Mobile No': ph, 'Email ID': mail, 'Balance': cash,
                                             'Account No': account_no, 'Account Type': account_type})
                            print('Account Created successfully')

                        with open(f'{name}_log_details.csv', 'w', newline='') as log_details:
                            write = csv.DictWriter(log_details, fieldnames=self.log_details)
                            write.writeheader()
                            write.writerow({'Email ID': mail, 'Password': password})

                        with open(f"{name}_transaction.csv", "w", newline="") as transaction:
                            writein = csv.DictWriter(transaction, fieldnames=self.trans)
                            writein.writeheader()
                            writein.writerow({'Transaction ID': trans_id, 'Note': note})

                    else:
                        print('Invalid Account type')
        else:
            print(f"For Opening account min balance should be 1000 you entered: , {cash}")

    def login(self, mail, password):
        if os.path.exists(f'{name}_log_details.csv'):
            if mail.endswith('.com'):
                with open(f"{name}_log_details.csv", "r") as f:
                    details = f.readlines()
                    for line in details:
                        if mail and password in line:
                            self.loggedin = True
                            print('Successfully Logged In!!!')

                        elif self.loggedin == True:
                            print(f"Welcome {name}, Sir")

            else:
                print("Wronge Credentials")
        else:
            print('Your are not Rigister With Us')

    def add_cash(self, name, amount):
        add_note = f"Successfully Amount Added : {amount}"
        if amount > 0:
            my_list = list()
            res = {}
            add_trans = list()
            self.mail = mail
            with open(f"{name}.csv", "r+") as s:
                details = csv.reader(s)
                for line in details:
                    my_list.append(line)
                new = int(my_list[1][3])
                my_list[1][3] = str(new + amount)
                key_list = my_list[0]
                value_list = my_list[1]
                for key in key_list:
                    for value in value_list:
                        res[key] = value
                        value_list.remove(value)
                        break
            with open(f"{name}.csv", "w", newline='') as new_details:
                write = csv.DictWriter(new_details, fieldnames=key_list)
                write.writeheader()
                write.writerow(res)
            with open(f"{name}_transaction.csv", "r") as v:
                details = csv.reader(v)
                for line in details:
                    add_trans.append(line)
                old = int(add_trans[-1][0])
                new = old + 1
            with open(f"{name}_transaction.csv", "a", newline="") as details:
                tra = csv.writer(details)
                tra.writerow([new, add_note])

        else:
            print("Enter Vaild Value for Amount")

    def mail_change(self, new_mail):
        res = {}
        my_list = list()
        ch_list = list()
        res1 = {}
        add_tran = list()
        note = "Successfully Email ID Changed"
        with open(f"{name}.csv", "r") as file:
            detail = csv.reader(file)
            for n in detail:
                my_list.append(n)

        with open(f"{name}.csv", "w", newline='') as lines:
            details = csv.DictWriter(lines, fieldnames=self.user_field)
            my_list[1][2] = new_mail
            key = my_list[0]
            value = my_list[1]
            for keys in key:
                for values in value:
                    res[keys] = values
                    value.remove(values)
                    break
            details.writeheader()
            details.writerow(res)

        with open(f'{name}_log_details.csv', 'r') as files:
            detaile = csv.reader(files)
            for line in detaile:
                ch_list.append(line)
        with open(f"{name}_log_details.csv", "w", newline='') as line:
            detail = csv.DictWriter(line, fieldnames=self.log_details)
            ch_list[1][0] = new_mail
            key = ch_list[0]
            value = ch_list[1]
            for keys in key:
                for values in value:
                    res1[keys] = values
                    value.remove(values)
                    break
            detail.writeheader()
            detail.writerow(res1)

        with open(f"{name}_transaction.csv", "r") as ch_mail:
            details = csv.reader(ch_mail)
            for lines in details:
                add_tran.append(lines)
            old = int(add_tran[-1][0])
            new_id = old + 1

        with open(f"{name}_transaction.csv", "a", newline="") as mail_ch:
            ch = csv.writer(mail_ch)
            ch.writerow([new_id, note])

    def veiw_transaction(self):
        transaction = pd.read_csv(f"{name}_transaction.csv", index_col=False)
        print(transaction)

    def ph_change(self, new_ph):
        my_list = list()
        res = {}
        add_tran = list()
        note = 'Mobile Number Successfully Updated'
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print('Invalid Phone Number! Please Enter 10 digit Number')
        else:
            with open(f"{name}.csv", "r") as file:
                details = csv.reader(file)
                for n in details:
                    my_list.append(n)

            with open(f"{name}.csv", "w", newline='') as lin:
                tails = csv.DictWriter(lin, fieldnames=self.user_field)
                my_list[1][1] = str(new_ph)
                key = my_list[0]
                value = my_list[1]
                for keys in key:
                    for values in value:
                        res[keys] = values
                        value.remove(values)
                        break
                tails.writeheader()
                tails.writerow(res)

            with open(f"{name}_transaction.csv", "r") as ch_ph:
                details = csv.reader(ch_ph)
                for lines in details:
                    add_tran.append(lines)
                old = int(add_tran[-1][0])
                new_ta = old + 1

            with open(f"{name}_transaction.csv", "a", newline="") as ph_ch:
                ch = csv.writer(ph_ch)
                ch.writerow([new_ta, note])

    def admin(self, mail, password):
        if mail.endswith('.com'):
            with open('admin_details.csv', 'r') as line:
                details = csv.reader(line)
                for lines in details:
                    if mail and password in lines:
                        self.admin_login = True
                        print('Successfully Logged In!!!')

    def check_bal(self):
        my_list = list()
        with open(f'{name}.csv', 'r') as file:
            details = csv.reader(file)
            for i in details:
                my_list.append(i)
        #         my_list[1][3] = int(my_list[1][3])
        bala = my_list[1][3]
        return bala

    def pass_change(self, new_pass):
        my_list = list()
        res = {}
        add_tran = list()
        note = 'Password Successfully Updated!!'
        if len(password) < 5 or len(password) > 18:
            print('Enter password greater than 5 and less than 18 character')

        else:
            with open(f'{name}_log_details.csv', 'r') as file:
                details = csv.reader(file)
                for line in details:
                    my_list.append(line)
            with open(f'{name}_log_details.csv', 'w', newline='') as files:
                deatil = csv.DictWriter(files, fieldnames=self.log_details)
                my_list[1][1] = new_pass
                keys = my_list[0]
                values = my_list[1]
                for key in keys:
                    for value in values:
                        res[key] = value
                        values.remove(value)
                        break
                deatil.writeheader()
                deatil.writerow(res)
            with open(f"{name}_transaction.csv", "r") as pass_ch:
                details = csv.reader(pass_ch)
                for lines in details:
                    add_tran.append(lines)
                old = int(add_tran[-1][0])
                new_id = old + 1
            with open(f"{name}_transaction.csv", "a", newline="") as ch_pass:
                ch = csv.writer(ch_pass)
                ch.writerow([new_id, note])

    def transfer_cash(self, tf_name, amount, acc_no):
        my_list = list()
        my_list1 = list()
        res = dict()
        res1 = dict()
        if os.path.exists(f'{tf_name}.csv'):
            with open(f'{tf_name}.csv', 'r') as file:
                details = csv.reader(file)
                for i in details:
                    my_list.append(i)
            if str(acc_no) in my_list[1][5]:
                self.transferCcash = True
                with open(f'{tf_name}.csv', 'w', newline='') as files:
                    some = csv.DictWriter(files, fieldnames=self.user_field)
                    my_list[1][3] = str(int(my_list[1][3]) + int(amount))
                    keys = my_list[0]
                    values = my_list[1]
                    for key in keys:
                        for value in values:
                            res[key] = value
                            values.remove(value)
                            break
                    some.writeheader()
                    some.writerow(res)
                with open(f'{name}.csv', 'r') as file:
                    details = csv.reader(file)
                    for i in details:
                        my_list1.append(i)
                    with open(f'{name}.csv', 'w', newline='') as files:
                        changes = csv.DictWriter(files, fieldnames=self.user_field)
                        my_list1[1][3] = str(int(my_list1[1][3]) - int(amount))
                        ke = my_list1[0]
                        val = my_list1[1]
                        for key in ke:
                            for value in val:
                                res1[key] = value
                                val.remove(value)
                                break
                        changes.writeheader()
                        changes.writerow(res1)
            else:
                print('Invalid Account Number')
        else:
            print("Invalid Customer Name or Customer Does not Exist's")

    def wait(self):
        i = 0
        while i < 10:
            print(".", end='')
            time.sleep(1)
            i = i + 1
        print('')


if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome to Lakshmi Chit Fund")
    print("1.User Login")
    print("2.Admin Login")
    print("3.Create a New Account")

    user = int(input("Make Decision: "))

    if user == 1:
        print("Logging in")
        name = input('Enter Your Name')
        mail = input("Enter Your Email")
        password = input('Enter your Password: ')
        print('Plaese Wait!! Verifing Your Data:', end='')
        Bank_object.wait()
        Bank_object.login(mail, password)
        while True:
            if Bank_object.loggedin:
                print("1.Add Amount")
                print("2.Check Banlance")
                print("3.Transfer Amount")
                print("4.Edit Profile")
                print("5.View Statement")
                print("6.Logout")

                login_user = int(input())
                if login_user == 1:
                    amount = int(input("Enter Amount: "))
                    Bank_object.add_cash(name, amount)
                    print("\n1.Back Menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 2:
                    print('Fleching Your Balance:', end='')
                    Bank_object.wait()
                    balance = Bank_object.check_bal()
                    print(f'Your Current balance is: {balance}')
                    print("\n1.Back Menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    print('Your Current Balance is: ', Bank_object.check_bal())
                    print('1.Transfer Within Bank')
                    print('2.Transfer to Other Bank')
                    user = int(input())
                    if user == 1:
                        amount = int(input("Enter Amount: "))
                        if amount > 0 and amount <= int(Bank_object.check_bal()):
                            tf_name = input("Enter Person Name: ")
                            acc_no = int(input("Enter person Account number: "))
                            print('Amount Beeing Transfer:!!', end='')
                            Bank_object.wait()
                            Bank_object.transfer_cash(tf_name, amount, acc_no)
                            print('Your Updated Balance is: ', Bank_object.check_bal())
                            print("\n1.Back Menu")
                            print("2.Logout")
                            choose = int(input())
                            if choose == 1:
                                continue
                            elif choose == 2:
                                break
                        elif amount <= 0:
                            print("Enter Valid Amount")
                        elif amount > int(Bank_object.check_bal()):
                            print("Insaficaint Balance")
                    elif user == 2:
                        print('This Service is Not Available Right Now!!! Sorry for inconvince!!!')

                elif login_user == 4:
                    print("1.Email Change")
                    print("2.Password Change")
                    print("3.Phone Number Change")
                    edit_profile = int(input())

                    if edit_profile == 1:
                        new_mail = input("Enter Your New Email: ")
                        Bank_object.mail_change(new_mail)
                        print("\n1.Back Menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                    elif edit_profile == 2:
                        new_pass = input('Enter New Password!: ')
                        Bank_object.pass_change(new_pass)
                        print("\n1.Back Menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                    elif edit_profile == 3:
                        new_ph = int(input("Enter Your New Number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.Back Menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif login_user == 5:
                    Bank_object.wait()
                    show = Bank_object.veiw_transaction()
                    print(show)

                elif login_user == 6:
                    break

            else:
                print("ohhh!! Get Rigester your self")
                break

    elif user == 2:
        mail = input("Enter Your Email")
        password = input('Enter your Password: ')
        Bank_object.admin(mail, password)
        while True:
            if Bank_object.admin_login:
                print('1.View Total Account in Bank')
                print('2.Veiw Total Amount Bank Hold')
        pass


    elif user == 3:
        print("Creating new account")
        name = input("Enter Your Name: ")
        ph = int(input('Enter your phone Number: '))
        password = input('Create a Password: ')
        print('Select One of Two \nSaving \nCurrent')
        account_type = input('Enter Account type: ')
        mail = input('enter mail: ')
        cash = int(input('Enter Opening Balance, min 1000: '))
        DoB = int(input('Enter Date Of Birth ddmmyyy: '))
        Bank_object.register(name, ph, mail, password, account_type, cash, DoB)