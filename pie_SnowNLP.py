import pandas as pd
import matplotlib.pyplot as plt



def get_length(file_path):

    df = pd.read_excel(file_path)
    first_column = df.iloc[1:, 0]

    return len(first_column)


length1 = get_length('labels/label1.xlsx')
length2 = get_length('labels/label2.xlsx')
length3 = get_length('labels/label3.xlsx')
length4 = get_length('labels/label4.xlsx')
length5 = get_length('labels/label5.xlsx')



data = [length1, length2, length3, length4, length5]


total = sum(data)

percentages = [(value / total) * 100 for value in data]

labels = ['0-0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8-1.0']

colors = plt.cm.Reds([i / float(len(labels)) for i in range(len(labels))])

plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

plt.savefig("pie/pie.png")

plt.clf()

print("饼图绘制完成")







