import pandas as pd
import os

input_file_path = 'labels/comments_score.xlsx'
df = pd.read_excel(input_file_path)

selected_columns = df.iloc[:, :2]

output_file_path = 'files/NoHeader.xlsx'

if os.path.exists(output_file_path):
    os.remove(output_file_path)

selected_columns.to_excel(output_file_path, index=False, header=False)

