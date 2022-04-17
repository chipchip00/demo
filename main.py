#Add libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('monthly.csv')
print("giá cả: ")
x= df["Date"].to_numpy();
y = df["Price"].to_numpy();

print('Nhập số năm:')
year = input()
month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
dfCurentYear = df[df['Date'].str.contains(year)]
year = str((int(year) -1))
dfLastYear = df[df['Date'].str.contains(str(int(year)-1))]

xCurr = month
yCurr = dfCurentYear["Price"].to_numpy()

yLast = dfLastYear["Price"].to_numpy()
print("Giá vàng lớn nhất trong năm: ")
print(np.amax(yCurr))
print("Giá vàng nhỏ nhất trong năm: ")
print(print(np.amin(yCurr)))
print("Giá vàng trung bình của năm: ")
print(np.mean(yCurr))
print("Độ lệch chuẩn: ")
print(np.std(yCurr))
print("2 tháng có giá vàng nhỏ nhất")
min2 = np.argpartition(yCurr,2)
min2 += 1
print(str(min2[0])+", "+str(min2[1]))

plt.figure()
plt.title("Gia vang nam: "+ str(int(year) +1)+" và "+year)
plt.plot(xCurr,yCurr)
plt.xlabel("Date")
plt.ylabel('Price')

plt.plot(month,yLast,"Yellow")
plt.xlabel("Date")
plt.ylabel('Price')

plt.figure()
plt.title("Gia vang tat ca cac nam")
plt.plot(x,y)
plt.xlabel("Date")
plt.ylabel('Price')
plt.show()

def print_hello():
    print("Hello World!")