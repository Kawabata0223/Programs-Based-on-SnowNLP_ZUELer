import pandas as pd
import os

csv_file_path = 'files/data.csv'
excel_output_path = 'files/comments.xlsx'

if os.path.exists(excel_output_path):
    os.remove(excel_output_path)


# 在第一行第一列添加文本
first_text = '文本'

df = pd.read_csv(csv_file_path)

df.loc[-1] = [first_text] + [''] * (df.shape[1] - 1)
df.index = df.index + 1
df = df.sort_index()

# 删除包含空值的行
df = df.dropna()

df.to_excel(excel_output_path, index=False, header=False)


print("预处理完成")




