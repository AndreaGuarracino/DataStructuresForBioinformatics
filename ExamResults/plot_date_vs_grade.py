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

# Set the style for the plot
sns.set_style("whitegrid")
plt.figure(figsize=(20, 12))

# Create the boxplot
sns.boxplot(x='Date', y='Grade', data=data, color="lightblue", width=0.5)

# Add swarmplot for individual data points
sns.swarmplot(x='Date', y='Grade', data=data, color="navy", size=6, alpha=0.6)

# Customize the plot
plt.title('Data Structures for Bioinformatics Exam\nDistribution of Grades Over Time', fontsize=28, pad=20)
plt.xlabel('Exam Date', fontsize=24, labelpad=15)
plt.ylabel('Grade', fontsize=24, labelpad=15)
plt.xticks(rotation=45, ha='right', fontsize=20)
plt.yticks(fontsize=20)

# Increase tick label size
plt.tick_params(axis='both', which='major', labelsize=20)

# Add a horizontal line for the mean grade
mean_grade = data['Grade'].mean()
plt.axhline(y=mean_grade, color='red', linestyle='--', alpha=0.7, linewidth=2)
plt.text(plt.xlim()[1], mean_grade, f' Mean: {mean_grade:.2f}', 
         verticalalignment='center', fontsize=20, color='red', fontweight='bold')

# Adjust the layout and display the plot
plt.tight_layout()
plt.show()