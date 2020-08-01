class Category:

    #Constructor
    def __init__(self, name):
        self.name= name
        self.ledger=list()

    #Deposit method
    def deposit(self, amount, description=""):
        # We append an object to the ledger list 
        # in the form of 
        # {"amount": amount, "description": description}
        #Initialising a dictionary
        self.depositDetail = dict()
        #Adding the amount and description to dictionary
        self.depositDetail["amount"] = amount
        self.depositDetail["description"]=description

        #Adding the deposit to the ledger list
        self.ledger.append(self.depositDetail)
    

    #Check_fund method
    def check_funds(self,amount):
        fundAvailable = 0
        n = len(self.ledger)
        for i in range(n):
            fundAvailable += self.ledger[i]["amount"]
        if fundAvailable<amount:
            return False
        else:
            return True

    #Withdraw method
    def withdraw(self,amount,description=""):
        # We need to check if the amount to be withdrawn 
        # is greater than or equal to the total amount
        check = self.check_funds(amount)

        if check:
            self.withdrawDetail = dict()
            self.withdrawDetail["amount"]=-(amount)
            self.withdrawDetail["description"]=description
            self.ledger.append(self.withdrawDetail)
            return True
        else:
            return False
        
        # get balance method that returns the current balance 
        # of the budget category based on the deposits 
        # and withdrawals that have occurred.
    def get_balance(self):
        fundAvailable = 0
        n = len(self.ledger)
        for i in range(n):
          fundAvailable += self.ledger[i]["amount"]
        return fundAvailable
        
        #Transfer method 
    def transfer(self, amount, objName):
        objectName = ""
        objectName = objName.name
        a=self.withdraw(amount,f"Transfer to {objectName}")
        if(a==True):
          objName.deposit(amount,f"Transfer from {self.name}")
          return True
        else:
          return False

    ### Withdrawl method for chart
    def get_withdrawls(self):
        fundAvailable = 0
        n = len(self.ledger)
        for i in range(n):
          amt = self.ledger[i]["amount"]
          if amt<0:
            fundAvailable += amt
        return fundAvailable

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            desc = f"{self.ledger[i]['description'][0:23]:23}"
            amt =  f"{self.ledger[i]['amount']:>7.2f}"
            items +=  desc + amt + '\n'
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output




###
def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getTotalCat(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    
    #Breakdown of spending rounded down to nearest 10th
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    title=""
    title = "Percentage spent by category\n"
    i = 100
    totals = getTotalCat(categories)
    
    for i in range(100, -1, -10):
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        title+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
    
    dashes = "-" + "---"*len(categories)
    names = []
    cat_names = ""
    for category in categories:
        names.append(category.name)

    maxLen = max(names, key=len)

    for x in range(len(maxLen)):
        nameStr = '     '
        i=0 
        nameslen = len(names)
        for name in names:
            if i<nameslen:
              if x >= len(name):
                nameStr += "   "
              else:
                 nameStr += name[x] + "  "
            else:
              if x >= len(name):
                nameStr += ""
              else:
                 nameStr += name[x] + ""
            i=i+1
        cat_names += '\n' +nameStr

    title+= dashes.rjust(len(dashes)+4) + cat_names
    return title

