import csv

import time
'''
1.bill printing
2.shop name
3.date
4.name of customer
5.list of product
6.total

'''

with open("final bill.csv", "w+") as fp:
    w = csv.writer(fp)

class bill:
    def __init__(self,name):
        self.customer=name
        self.shop="VIJAY SALES"
        self.time=time.ctime(time.time())

    def final(self):
        with open("final bill.csv","w")as fp:
            w = csv.writer(fp)
            w.writerow([" ","CASH RECEIPT"," "])
            w.writerow([" ", self.shop, " "])
            w.writerow([self.time , " ", " "])
            w.writerow(["customer :", self.customer , " "])
            w.writerow(["###########################","##################","###########"])
name_customer=input("enter coustomer name  : ").upper()
obj=bill(name_customer)
obj.final()





























