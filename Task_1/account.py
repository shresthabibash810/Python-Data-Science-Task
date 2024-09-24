import csv

TRANSACTION_RECORDS = 'account_transactions.csv'
USER_RECORDS = 'user_records.csv'


class Account:

    ''' This class provides multiple functionalities for a pre-existing user account. A UserID, and a transaction account is first needed to be able use this 
    class. The User ID can be generated from the Customer class, and the transacion account can be created using the NewAccount class.

    Usage:
        uid = 1001
        account_number = 3330000407 (optional)
        myaccount = Account(uid,account_number)

    Returns:
        An account object with functions to view details, deposit, withdraw, and transfer money.

    Example 1 (passing both UID and Account number):

        myaccount = Account(1001, 3330000407)

        myaccount.deposit(100)
        > Deposits money (Rs. 100) to account number 1001.

        myaccount.withdraw(50)
        > Withdraws money (Rs. 50) from account number 1001.


    Example 2 (without passing in the Account number):

        youraccount = newAccount(1002)

        youraccount.deposit(100)
        youraccount.view_balance()
        youraccount.view_account_details()

    '''

    _attributes = ("UID", "Account Number", "Balance")

    def __init__(self, usr_id, acc_number=None):

        self.usr_id = usr_id
        self.acc_number = acc_number
        if self.acc_number is None:
            self.acc_number = self._get_account_number()

    def _get_account_number(self, uid=None):

        if not uid:
            uid = self.usr_id
        with open(TRANSACTION_RECORDS, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    if int(row[0]) == int(uid):
                        return row[1]
        print("Account not found. Please create a new account using the newAccount option.")

    def view_account_details(self):

        with open(TRANSACTION_RECORDS, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    if int(row[0]) == int(self.usr_id):
                        details = dict(zip(self._attributes[1:], row[1:]))

        for keys, values in details.items():
            print("{} : {}".format(keys, values))

    def view_balance(self, uid=None):

        if not uid:
            uid = self.usr_id

        with open(TRANSACTION_RECORDS, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    if int(row[0]) == int(uid):
                        return row[2]
        print("Error occurred. Please contact support.")
        return None

    def deposit(self, amount):
        '''Please complete this method. Your method should:
        1. Accept a single numeric value 'amount'.
        2. Update the TRANSACTION RECORDS file by adding the given 'amount' to existing amount for the current user object.
        3. The function need not return anything, or a simple confirmation (success/failure) if you wish to.

        NOTE: You can modify your function to accept other input arguments as well, but remember that the current test needs to be
        modified as well if you choose to do so.
        '''
        print("\nThe 'deposit' method in the 'Account' class needs to be completed to pass this step in the test and proceed to next step!!\n")

    def withdraw(self, amount):
        '''Please complete this method. Your method should:
        1. Accept a single numeric value 'amount'.
        2. Check if the required balance is available in the TRANSACTION RECORDS file for the current user.
        3. If condition 2 is satisfied, update the TRANSACTION RECORDS file to deduct the given 'amount' from existing amount 
        for the current user object.
        4. The function need not return anything, or a simple confirmation (success/failure) if you wish to.

        NOTE: You can modify your function to accept other input arguments as well, but remember that the current test needs to be
        modified as well if you choose to do so.
        '''
        print("\nThe 'withdraw' method in the 'Account' class needs to be completed to pass this step in the test and proceed to next step!!\n")

    def transfer_funds(self, uid, amount):
        '''Please complete this method. Your method should: 
        1. Accept two values, a. first value - the 4 digit user id to which you want the funds transferred to, b. second value - numeric 
        value representing the 'amount' that you want to transfer.
        2. Check if the 4 digit user id actually exists in the TRANSACTION RECORDS file. (RECEIVER)
        3. Check if the required balance is available in the TRANSACTION RECORDS file for the current user. (SENDER)
        4. If condition 2 and 3 is satisfied, update the TRANSACTION RECORDS file to deduct the given 'amount' from existing amount 
        for the current user object (SENDER).
        5. Update the TRANSACTION RECORDS file by adding the given 'amount' to existing amount for the given user id (RECEIVER).
        6. The function need not return anything, or a simple confirmation (success/failure) if you wish to.

        NOTE: You can modify your function to accept other input arguments as well, but remember that the current test needs to be
        modified as well if you choose to do so.

        '''
        print("\nThe 'transfer_funds' method in the 'Account' class needs to be completed to pass the test!!\n")
