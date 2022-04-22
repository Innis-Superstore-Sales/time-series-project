# Superstore Sales: 2018 Goals and Forecast

This repository contains all deliverables for the superstore time series project including additional files used 
in the process of producing the final deliverables.

Click this [link](https://docs.google.com/presentation/d/1UIXDBEbHVVMIBVPWmz8MOXP0YEflioVAFBfA8wPpOgo/edit?usp=sharing) for the slideshow.

**Repository Format**
<details>
<summary>Click to expand</summary>

- README.md: Contains a full outline of the project, information regarding the format of the repository, and instructions for reproducing the results.
- acquire.py: Contains a class that can be used to acquire the superstore data from the MySQL database.
- get_db_url.py: Contains helper code needed to access the MySQL database.
- prepare.py: Contains functions used for preparing the data for exploration and modeling including cleaning the data, removing outliers, and splitting the data.
- wrangle.py: Contains convenience functions that can be used to both acquire and prepare the data in one step.
- explore.py: Contains functions used for producing visualizations in the final report.
- model.py: Contains functions used for building various forecast models.
- evaluate.py: Contains functions used for evaluating forecast models.
- superstore_sales_report.ipynb: The final report containing an outline of all steps taken, with results, and extraneous details removed.
- notebooks/
    - wrangle.ipynb: Contains all the steps taken in the acquisition and preparation phases of the pipeline.
    - explore.ipynb: Contains all the steps taken in the exploratory analysis phase of the pipeline.
    - model.ipynb: Contains all the steps taken in the modeling phase of the pipeline.

</details>

___

## Table of Contents

1. [Project Summary](#project-summary)
2. [Project Goals](#project-goals)
3. [Project Description](#project-description)
4. [Initial Questions](#initial-questions)
5. [Data Dictionary](#data-dictionary)
6. [Recreate This Project](#instructions-for-recreating-this-project)
7. [Outline of Project Plan](#outline-of-project-plan)
    1. [Data Acquisition](#data-acquisition)
    2. [Data Preparation](#data-preparation)
    3. [Exploratory Analysis](#exploratory-analysis)
    4. [Modeling](#modeling)
8. [Conclusion](#conclusion)

___

## Project Summary

Our team conducted time series analysis on four years of sales figures from a superstore in order to determine sales goals for the next year and the courses of action that would help to reach those goals. We used Pandas and Seaborn to gather insights, and used FB Prophet to create a sales and profit forecast.

___

## Project Goals

Given four years of sales data, identify sales patterns in order to produce a sales, and profit, forecast for 2018, and determine what courses of action will lead to increased sales in the future.

___

## Project Description

With growing demands in the market the VP of sales at a superstore giant has asked us, what should our sales goals for 2018 be? Given sales data for the years 2014 through 2017 the goal of this project is to determine what trends exist in the sales data that can help us determine what sales trends we can expect in 2018. Furthermore, we aim to discover where strengths, or weaknesses, exist in the sales numbers so that we can provide recommendations for improving sales, and profit, going forward.

___

## Initial Questions

- What are the total sales trends on a weekly basis?
- What are the total sales trends on a monthly and quarterly basis?
- Are there any times in the year when sales are consistently higher, or lower, than the rest of the year?
- Does separating the data by region provide clearer sales trends?
- Does separating the data by product category provide clearer sales trends?
- Is there a relationship between discount and profit?

___

## Data Dictionary

<details><summary>Click to expand</summary>

| Variable              | Meaning      |
| --------------------- | ------------ |
| Order Date            | Order Date of the product. |
| Region Name           | Region where the Customer belongs. |
| Category              | Category of the product ordered. |
| Sales                 | Sales of the Product. |
| Quantity              | Quantity of the Product. |
| Discount              | Discount provided. |
| Profit                | Profit/Loss incurred. |

</details>

___

## Instructions For Recreating This Project

1. Clone this repository into your local machine using the following command:
```bash
git clone git@github.com:Innis-Superstore-Sales/time-series-project.git
```
2. You will need Pandas, Numpy, Matplotlib, Seaborn, SKLearn, statsmodels, and prophet installed on your machine.
3. If you don't have login credentials for the MySQL database hosted at data.codeup.com acquire login credentials.
4. Create a file in the main directory titled "env.py" and put your login credentials in the following format:
```python
username = "your_username"
password = "your_password"
hostname = "data.codeup.com"
```
5. Now you can start a Jupyter Notebook session and execute the code blocks in the superstore_sales_report.ipynb notebook.

___

## Outline of Project Plan
---
### Data Acquisition

In this phase the superstore data is acquired from the MySQL database hosted at data.codeup.com. The data is cached in a .csv file for faster loading and convenience.

- The wrangle.ipynb notebook in the notebooks directory contains a reproducible step by step process for acquiring the data with details 
and explanations.

- The acquire.py file contains all the data acquisition code used in the final report notebook.

- The _acquire.py file contains a data acquisition class used in the acquire.py file.

- The get_db_url.py file contains code used to access the MySQL database.

**Steps Taken:**
1. Create an SQL query that can be used to acquire the data from the database.
2. Ensure that all the data has been properly acquired.
3. Encapsulate all acquisition code in acquire.py.

### Data Preparation

In this phase the superstore data is prepared for exploration and modeling. Preparation includes renaming columns, removing unneeded columns, setting the date as the index, and separating the data into various groups that are to be analyzed. Additionally, code for removing outliers is created to allow for outliers to be removed from the dataset if they skew the data in a way that makes analysis difficult.

- The wrangle.ipynb notebook in the notebooks directory contains a reproducible step by step process for preparing the data with details and explanations.

- The prepare.py file contains all the data preparation functions used in the wrangle module.

- The wrangle.py file contains code used in the final report for acquiring and preparing the data.

**Steps Taken:**
1. Analyze the data to determine how it should be cleaned.
2. Rename columns for ease of use.
3. Remove unneeded columns.
4. Set the date to a datetime type and set it as the index.
5. Analyze the dates to determine if upsampling, or downsampling, is necessary.
6. Separate the data into various groups that will be analyzed in exploration.
7. Encapsulate all preparation code in prepare.py and wrangle.py.

### Exploratory Analysis

In this phase the superstore data is analyzed to determine what sales trends exist in the data. We start by analyzing total sales by weeks, months, quarters, and years to see if any patterns exist. We also analyze discounts and profits to determine if any insights can be gained from those features. We then perform similar analysis for each region represented in the data and each product category represented in the data. Finally, we perform additional analysis with outliers removed to see if the trends change depending on the absence of outlying data.

- The explore.ipynb notebook in the notebooks directory contains a reproducible step by step process for exploring the data with details and explanations.

- The explore.py file contains all the data exploration functions used in the final report notebook.

**Steps Taken:**
1. Analyze weekly, monthly, quarterly, and yearly total sales data.
2. Analyze weekly, monthly, quarterly, and yearly sales data per region.
3. Analyze weekly, monthly, quarterly, and yearly sales data per product category.
4. Analyze the discount feature in the data being sure to resample with average instead of sum.
5. Perform additional analysis on total sales with outliers removed.
6. Document all key takeaways.
7. Encapsulate any code that will be used in the final report in explore.py.

### Modeling

In this phase a sales forecasting model is produced to predict the expected sales, and profit, trends in 2018. Before doing this the data is split into train, validate, and test datasets to keep some data as unseen in order to maintain the integrity of our forecasting models. Various models are developed and the best one is chosen to produce the 2018 sales forecast.

- The model.ipynb notebook in the notebooks directory contains a reproducible step by step process for exploring the data with details and explanations.

- The model.py file contains all the modeling functions used in the final report notebook and model.ipynb notebook.

- The evaluate.py file contains helper functions used for evaluating the performance of the forecasting models.

**Steps Taken:**
1. Acquire, prepare, and split the data.
2. Establish a baseline model.
3. Create various total sales forecasting models.
4. Create various ensemble models using the data separated by region.
5. Create various ensemble models using the data separated by product category.
6. Evaluate the performance of all models and choose the model with the best performance.
7. Use the best model to produce a sales, and profit, forecast for 2018.

___

## Conclusion

There is a steady increase in sales, and profit, over the four year span of 2014 through 2017, but rate of increasing growth is not significant. Large discounts are affecting the bottom line and resulting in losses. Our best forecast predicts continued sales growth in 2018, but there is room for improvement.

Our recommendations are as follow:
- Maintain momentum in the second half of the year, what we're doing is working.
- Target low sales month such as January and February by running promotions to increase sales numbers.
- Set a maximum discount rate to minimize losses.
- Begin tracking the reason why discounts are being, since that is something we would like to analyze.

___

[Back to top](#superstore-sales-2018-goals-and-forecast)