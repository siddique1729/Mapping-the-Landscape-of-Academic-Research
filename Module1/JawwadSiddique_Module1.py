# Name: Jawwad Shadman Siddique
# Module 1 - Exercises 1
# File Path: C:\CS332\Module1\JawwadSiddique_Module1.py
# (Replaced the file path above with my actual full path)

import pandas as pd

# Step 1: Creating the data inside Python
data = {
    "AGE": [21, 34, 56, 19, 47],
    "HEIGHT": [65, 70, 62, 71, 67],
    "FavCOLOR": ["blue", "blue", "yellow", "black", "purple"]
}

# Step 2: Converting dictionary to DataFrame
df = pd.DataFrame(data)

# Step 3: Saving the DataFrame as a CSV file in the same folder
df.to_csv("C:/CS332/Module1/MyData.csv", index=False)   # <-- Updating with actual path

# Step 4: Reading the CSV file into a new DataFrame
df = pd.read_csv("C:/CS332/Module1/MyData.csv")

# Step 5: Printing the DataFrame
print("Original DataFrame:")
print(df)

# Step 6: Printing the list of column names
col_names = list(df.columns)
print("\nColumn Names:")
print(col_names)

# Step 7: Deleting columns whose names are longer than 6 characters
for col in col_names:
    if len(col) > 6:
        df = df.drop(columns=[col])

# Step 8: Print the modified DataFrame
print("\nModified DataFrame:")
print(df)
