# ATM Machine

print()
print("Welcome to Sakesnake ATM Machine!")
print()


def get_time():
    import datetime
    return datetime.datetime.now()


def is_pin_format_correct(pin):
    if len(pin) < 4 or len(pin) > 4:
        return False

    return True


def is_pin_exist(pin):
    with open("atm files.txt") as f:
        line = f.readline()
        while line != "":
            if line.startswith(pin, 0, 4):
                return True

            line = f.readline()

        return False


# Update the log data of a user
def log_info(pin, data):
    with open(pin + "_log.txt", "a") as f:
        f.write(data)


# Get log data of user
def get_log_data(pin):
    with open(pin + "_log.txt", "r") as f:
        print(f.read())


# Withdraw amount from atm
def amt_withdraw(pin):
    file_name = pin + ".txt"
    print("Enter withdraw amount: ")
    withdraw = int(input())
    with open(file_name, "rt") as f:
        existing_amt = int(f.readline())
        remaining_funds = existing_amt - withdraw
        if remaining_funds < 0:
            print("Insufficient balance in your account.")
            exit()

        with open(file_name, "w") as f2:
            f2.write(str(remaining_funds))

    data = f"{get_time()} {withdraw} debited from account, your remaining balance: {remaining_funds} \n"
    log_info(pin, data)
    print("Please receive your cash below!!!")


# Deposit amount in bank
def deposit_amt(pin):
    file_name = pin + ".txt"
    print("Enter deposit amount: ")
    deposit = int(input())
    with open(file_name, "rt") as f:
        existing_funds = int(f.readline())
        total_funds = deposit + existing_funds

        with open(file_name, "w") as f2:
            f2.write(str(total_funds))

        data = f"{get_time()}: {deposit} credited in your account, Your balance: {total_funds} \n"
        log_info(pin, data)

    print(f"{deposit} Rs deposited successfully!!!")


# Check remaining balance
def remaining_balance(pin):
    file_name = pin+".txt"
    with open(file_name) as f:
        print("Your balance is: " + f.read())

    exit()



def actions(pin):
    print("1:- Withdrawal, 2:- Check Balance, 3:- View statement, 4:- Deposit")
    action = int(input())

    if action == 1:
        amt_withdraw(pin)
    elif action == 2:
        remaining_balance(pin)
    elif action == 3:
        get_log_data(pin)
    elif action == 4:
        deposit_amt(pin)


def login_account():
    print("Login account")
    pin = input("Enter your pin:\n")

    if is_pin_format_correct(pin) and is_pin_exist(pin):
        actions(pin)
    else:
        print("Please enter correct pin!!!")
        login_account()


def create_necessary_files(pin):
    # Inserting pin into file
    with open("atm files.txt", "a") as f:
        f.write(pin+"\n")

    # Creating account info file
    info_file_name = pin + ".txt"
    with open(info_file_name, "w") as f:
        f.write(str(1000))

    # Creating account statement/log file
    line = f"Account created at {get_time()}\n{get_time()}: 1000 credited in your account, Your balance: 1000\n"
    log_info(pin, line)

    print("Account created successfully!!!")


def create_account():
    print("Create account")
    pin = input("Enter your new pin:\n")

    if is_pin_format_correct(pin):
        create_necessary_files(pin)
    else:
        print("Please enter valid pin of only 4 digit!")
        create_account()


def start_machine():
    print("1:- Login, 2:- Create Account")
    action = int(input())

    if action == 1:
        login_account()
    elif action == 2:
        create_account()


start_machine()
