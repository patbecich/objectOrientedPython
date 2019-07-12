
class Bet:
    '''Represents an individual bet'''

    def __init__(self, amount=0, odds=100):
        '''Initialize a bet (default $0 at +100 odds)'''
        self.amount = amount
        self.odds = odds

    def calcPayout(self):
        '''Evaluate the potential payout of a bet based on odds and bet value'''
        if self.odds >= 100:
            return self.amount + self.amount * (self.odds / 100)
        elif self.odds <= -100:
            return self.amount + self.amount * (100/abs(self.odds))
        else:
            return "invalid odds"

    def givePayout(self, result):
        '''Evaluate the payout of a bet based on result'''
        if result == "L":
            return 0
        elif result == "W":
            return self.calcPayout()
        else:
            return "invalid result: Use 'W' for win and 'L' for lose"


class runningTotal:
    '''Calculates a running total'''

    def __init__(self, transactionList):
        '''Initialize an empty list'''
        self.runningTotal = []
        for transaction in transactionList:
            self.runningTotal.append(transaction.givePayout(transaction[1]))
        print(runningTotal)
