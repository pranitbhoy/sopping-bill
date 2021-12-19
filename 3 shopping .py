from product import product
import  csv

t=[]
try:
    while True:
        select=int(input("select id of product   :"))
        print(product.get(select, "                              SELECT VALID PRODUCT "))
        p = product.get(select)

        with open("final bill.csv", "a+") as fp:
            w = csv.writer(fp)
            w.writerow([p.get("product"), p.get("price"), p.get("GST")])
        if select  > 100 and select < 121 :
            t.append((p.get("price")))
            t.append((p.get("GST")))

        if select==0:

            break

except:

    print("                              CHARACTER  IN ID ")

total=sum(tuple(t))

print(total)

with open("final bill.csv", "a+") as fp:
    w = csv.writer(fp)
    w.writerow(["TOTAL ","=",total])
    w.writerow([" ", "THANKS FOR VISIT"," "])

















