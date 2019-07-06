import pandas as pd

# Read in the Excel File
sales = pd.read_excel('orders_summary.xlsx')

# Sort by Order and Descending Sales Value
sales = sales.sort_values('Order', ascending=True)
sales = sales.sort_values('Order Gross', ascending=False)
sales = sales.reset_index(drop=True)


print(sales.info())
print(sales.describe())