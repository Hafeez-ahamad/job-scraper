import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine('sqlite:///data/jobs.db')
df = pd.read_sql('jobs', engine)

# Basic analysis
print("Job Listings Summary:")
print(df.describe())

# Salary distribution
plt.figure(figsize=(10, 6))
plt.hist(df['salary'].dropna(), bins=20, color='blue', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary ($)')
plt.ylabel('Frequency')
plt.savefig('data/salary_distribution.png')
plt.show()

# Jobs by location
location_counts = df['location'].value_counts()
plt.figure(figsize=(10, 6))
location_counts.plot(kind='bar', color='green')
plt.title('Jobs by Location')
plt.xlabel('Location')
plt.ylabel('Number of Jobs')
plt.savefig('data/jobs_by_location.png')
plt.show()

# Top companies hiring
company_counts = df['company'].value_counts().head(10)
plt.figure(figsize=(10, 6))
company_counts.plot(kind='bar', color='orange')
plt.title('Top Companies Hiring')
plt.xlabel('Company')
plt.ylabel('Number of Jobs')
plt.savefig('data/top_companies.png')
plt.show()
