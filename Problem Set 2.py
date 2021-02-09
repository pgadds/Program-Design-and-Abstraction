#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:18:30 2019

@author: navboi
"""

#Problem 1

month = 0
totalPay = 0
monthlyInterestRate = annualInterestRate / 12.0
while month <12:
    minPay = monthlyPaymentRate * balance
    unpayBal = balance - minPay
    totalPay += minPay
    balance = unpayBal + (monthlyInterestRate * unpayBal)
    month += 1
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minPay,2)))
    print('Remaining balance: ' + str(round(balance,2)))
print('Total paid: ' + str(round(totalPay,2)))
print(' Remaining balance: ' + str(round(balance,2)))

#Problem 2 
balance = 3329
annualInterestRate = 0.2
initBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
month = 0
minPay = 10
def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance
while calculate(month, balance, minPay, monthlyInterestRate) > 0:
    balance = initBalance
    minPay +=10
    month = 0
    calculate(month, balance, minPay, monthlyInterestRate)
print('Lowest Payment: ' + str(minPay))

#Problem 3 
init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
print('The Lowest Payment is:', round(monthlyPaymentRate, 2))
