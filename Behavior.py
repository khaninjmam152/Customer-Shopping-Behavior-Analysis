import pandas as pd

# Read CSV file 
df = pd.read_csv( 'customer_shopping_behavior.csv' )

# Display data 
# print(df.head())

#display info
print(df.info())

# summary statistics using describe ()= iska mtlab sakbo include kro
print(df.describe(include='all'))

#missing value find
print(df.isnull().sum())

df['Review Rating'] = df.groupby('Category') ['Review Rating'].transform (lambda x: x.fillna(x.median()))
print(df.isnull(). sum())

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df.columns

df = df.rename(columns= {'purchase_amount_(usd)': 'purchase_amount'})
print(df.columns.tolist())

labels= ['Young_Adult', 'Adult', 'Middle_aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
df[['age', 'age_group']].head(10)
# Count customers in each age group

print(df['age_group'].value_counts())


frequency_mapping ={
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 months' : 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days', 'frequency_of_purchases']].head(10))

df[['discount_applied','promo_code_used']].head(10)
df= df.drop('promo_code_used', axis=1)
df.columns
df.head()

# Save updated DataFrame into cleaned CSV
df.to_csv("cleaned_customer_shopping_behavior.csv", index=False)

print("Cleaned CSV saved successfully!")
print(df.columns.tolist())
print(df.head())