# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:35:56 2023

@author: aosen
"""


dataPoints = []
maxProfit = 0
maxLoss = 0
profitMonth = ""
lossMonth = ""
total = 0
current = 0
change = 0
file = open("budget_data.csv", "r")
for line in file:
    data = line.split(",")
    try:
        data[1] = int(data[1].replace("\n", ""))
        dataPoints.append(data)
        total = total+data[1]
        net_chng = data[1]-current
        if maxProfit < net_chng:
            maxProfit = net_chng
            profitMonth = data[0]
        if maxLoss > net_chng:
            maxLoss = net_chng
            lossMonth = data[0]
        if current != 0:
            change = change + net_chng
        current = data[1]
    except:
        print()
analysis = "Financial Analysis \n---------------------------- \nTotal Months: "+str(len(dataPoints))+"\nTotal: $"+str(total)+"\nAverage Change: $"+str("{:.2f}".format(
    change/(len(dataPoints)-1))) + "\nGreatest Increase in Profit: "+profitMonth + " ($"+str(maxProfit)+")\nGreatest Decrease in Profit: "+lossMonth + " ($" + str(maxLoss)+")"
print(analysis)
with open('PyBank.txt', 'w') as f:
    f.write(analysis)
