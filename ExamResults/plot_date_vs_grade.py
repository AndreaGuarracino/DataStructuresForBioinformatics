import matplotlib.pyplot as plt
import os
import pandas as pd
from datetime import datetime
import seaborn as sns

# Function to read the MD file and return a DataFrame
def read_md_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        lines = lines[2:]  # Skip the header and the underline
        student_ids = []
        grades = []
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) < 3:
                continue
            grade = parts[2].strip()
            if grade == 'absent':  # Skip the row if grade is 'absent'
                continue
            elif grade == '30L':
                grades.append(32)
            else:
                grades.append(int(grade))
            student_ids.append(parts[1].strip())
        return pd.DataFrame({'StudentID': student_ids, 'Grade': grades})

# Directory containing the MD files
directory = os.path.dirname(os.path.realpath(__file__))

# List to hold DataFrames for each date
dfs = []

# Iterate through the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        date_str = filename[:-3]  # Remove the .md extension
        date = datetime.strptime(date_str, '%Y.%m.%d').date() # Extract the date only
        filepath = os.path.join(directory, filename)
        df = read_md_file(filepath)
        df['Date'] = date
        dfs.append(df[['Date', 'Grade']])

# Concatenate all DataFrames
data = pd.concat(dfs, ignore_index=True)

# Sort by Date
data = data.sort_values(by='Date')

# Plotting the boxplot for all grades on the same date
plt.figure(figsize=(12,6))
sns.boxplot(x='Date', y='Grade', data=data, color="lightgray")
sns.swarmplot(x='Date', y='Grade', data=data, color="black", size=4) # Add points
plt.title('Grades over time')
plt.xlabel('Date')
plt.ylabel('Grade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

