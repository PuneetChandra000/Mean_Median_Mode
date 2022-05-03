import pandas as pd

data = pd.read_csv("heightWeight.csv")

weight = data["Weight(Pounds)"].tolist()

sum = 0

for i in weight  :
    sum = sum + i


n = len(weight)

mean = sum/n

print("Mean : " , mean)

