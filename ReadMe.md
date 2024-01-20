# Simple Data Analyzing and Deployment

## Dataset

https://www.imf.org/~/media/Files/Publications/WEO/WEO-Database/2020/02/WEOOct2020all.ashx

The dataset which is in above is used. However, it was a broken file and was not read with **pandas** library. That's why, the file was read line by line using **openpyxl** library then the errors was fixed and was created new dataframe with following code.

```python
from openpyxl import load_workbook
import pandas as pd

file_path = 'WEOOct2020all.xlsx'

workbook = load_workbook(filename=file_path, data_only=True)

sheet = workbook[workbook.sheetnames[0]]

data_rows = []
for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, max_col=sheet.max_column):
    try:
        row_data = [cell.value for cell in row]
        split_data = [data.split('\t') if data is not None else [] for data in row_data]

        row_list = []
        for data in split_data:
            if data is not None:
                row_list.extend(data)  

        data_rows.append(row_list)
    except AttributeError as e:
        print("Warning: ", e)  

column_names = ['WEO Country Code', 'ISO', 'WEO Subject Code', 'Country', 'Subject Descriptor', 'Subject Notes', 'Units', 'Scale', 'Country/Series-specific Notes']
years = [str(year) for year in range(1977, 2023)]
# extra_columns = ['Extra' + str(i) for i in range(1, sheet.max_column - len(column_names) - len(years))]

all_column_names = column_names + years + ['Estimates Start After']

df = pd.DataFrame(data_rows)
df = df.iloc[:8660, 0:56]
df.columns = all_column_names

df['Country/Series-specific Notes'] = df[['Country/Series-specific Notes', '1977', '1978', '1979']].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
df = df.drop(columns=['1977', '1978', '1979'])

df.head()
```

## Tasks for Analyze the Data

1. Find top 10 countries that grew "Gross domestic product per capita" the most over the last decade

2. Draw OECD countries' "Population" growth over the last decade

3. Save the GDP growth figures in separate charts and save them as PNG files

4. Create 5 clusters out of the countries using GDP and "Volume of exports of goods"

   ​	a. draw the charts (x-axis - GDP, y - volume)

   ​	b. Add labels for the top 5 countries according to the GDP on the dots representing countries in each cluster

5. Find all the data fields from the year 2015 that are present in most of the countries

6. Create a predictor (use scikit) to predict GDP per capita (exclude other GDP-related fields). 

   ​	a. Show prediction error (MSE) on the training and the testing data sets

   ​	b. Name the fields that were used during training

   ​	c. Find the top 5 fields/features that contribute the most to the predictions

   ​	d. Train another predictor that uses those top 5 features

   ​	e. Save the predictor in a file

## Tasks for HTTP API Development

1. Create HTTP endpoint (WEB API) (use Flask):

   ​	a. The endpoint should accept JSON body using these fields: "continent, population, Gross national savings" and previously found top 5 features (6d task)

   ​		i. example: {"gross_nation_savings": 10, "continent": "Europe" …. }

   ​	b. The returned response (JSON) should contain field shows the predicted GDP per capita

2. Write an automated test (use unittest package) using flask (https://flask.palletsprojects.com/en/1.1.x/testing/#the-first-test) that would check whether the endpoint works

## Codes

**main.ipynb:** The code is used for create a fixed dataset and analyze the data according to tasks. In the last section of code, a predictor is created using **Ada Boost Algorithm**, then finding the most important 5 features. After that, a new model is trained for these 5 features and is saved.

**http_api.py:** Simple example of model deployment using flask

**test.py:** It connects the flask app and sends an example data with 5 features for test the http_api and the model.
