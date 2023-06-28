# to use external packages
# # first we need to install them
# find packages on https://pypi.org/
# look for updated and popular packages
# for example go to terminal and type
# pip install requests - to install requests package for web requests
# pip install pandas - to install pandas package for data analysis
# afterwards we can import them

import pandas as pd # very common way to import pandas
# pandas is huge so we do not want to pollute our namespace
# but we are lazy so we do not want to type pandas all the time

# let's make a dataframe from a dictionary
# for documentation go to https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
data = {"name": ["John", "Jane", "Joe"], "age": [20, 30, 40]}
df = pd.DataFrame(data)
print(df)