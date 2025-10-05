class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        
        Args:
            initial_balance (float): Starting balance for the account (default 0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        
        Args:
            amount (float): Amount to deposit
        """
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if funds are sufficient.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")