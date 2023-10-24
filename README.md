### sql-alchemy

## Table of Contents
- [Intro to SQL Alchemy)](#sql-alchemy)
- [What is ORM?](#ORM)
- [Project Overview](#project-overview)
- [Part1: Analyze and Explore the Climate Data](#part1)
- [Part2: Design Climate App](#part2)

# Intro to SQL ALCHEMY

![image](https://github.com/JasmineBamba/sql-alchemy/assets/135666038/ba408867-fc09-4693-95eb-75a5a7b4397c)

SQLAlchemy is an open-source SQL toolkit and Object-Relational Mapping (ORM) library for Python that bridges the differences among the various SQL dialects. A single Python script that uses SQLAlchemy can perform the same query across the different SQL dialects, such as:

![image](https://github.com/JasmineBamba/sql-alchemy/assets/135666038/5ec782d3-f59c-48c5-bfee-f88fc58edbf7)

## What is ORM?

ORM, which stands for Object-Relational Mapping, is a programming technique that allows you to work with a relational database using object-oriented programming concepts. In other words, it bridges the gap between the object-oriented model used in programming languages like Python, Java, or C# and the relational model used in databases like MySQL, PostgreSQL, or SQLite.

In an ORM system, database tables are represented as classes, and rows in those tables are represented as objects. This enables developers to interact with the database using high-level programming constructs, such as classes and objects, rather than writing raw SQL queries.

![image](https://github.com/JasmineBamba/sql-alchemy/assets/135666038/51bdb75f-45db-4c6d-9254-15d499a2cbfe)

## Project Overview

In this project we prepare to go on an extended vacation in Honolulu, Hawaii, and have recognize the importance of planning our trip with valuable insights into the local climate. To aid in our travel preparations, we have chosen to conduct a comprehensive climate analysis of the region.

## Part1: Analyze and Explore the Climate Data

In this section, we will conduct a thorough climate analysis and explore the climate database which is stored hawaii.sqlite using Python and SQLAlchemy. The analysis will involve the use of SQLAlchemy ORM queries, data manipulation with Pandas, and visualization using Matplotlib. 

**Precipitation Analysis:**

- Find the Most Recent Date:
Start by identifying the most recent date in the dataset. This date will serve as a reference point for our analysis.

- Retrieve the Previous 12 Months of Precipitation Data:
Without the need to pass the date as a variable, design a query to fetch the data for the previous 12 months starting from the most recent date.

- Select "date" and "prcp" Values:
From the queried data, choose only the "date" and "prcp" values for analysis.

- Create a Pandas DataFrame:
Load the query results into a Pandas DataFrame, making sure to explicitly set the column names as "date" and "prcp."

- Sort the DataFrame:
Organize the data in the DataFrame by sorting the values based on the "date" column, ensuring a chronological order.

- Visualize the Precipitation Data:
Utilize the built-in plotting capabilities of Pandas by using the DataFrame's plot method. This will enable us to create a graphical representation of the precipitation data, providing a visual overview of precipitation trends.

![image](https://github.com/JasmineBamba/sql-alchemy/assets/135666038/620d92e5-8537-4917-8be6-dc90f2671928)
![image](https://github.com/JasmineBamba/sql-alchemy/assets/135666038/88618726-8f2f-48a3-995c-2d49721dd5c2)



**Station Analysis:**

- Total Number of Stations:
Designed a query to calculate the total number of stations in the dataset.

- Identifying Most-Active Stations:
Designed a query to identify the most-active stations, which are stations with the highest number of observations.
Listed the stations and their observation counts in descending order.
Determined which station ID had the greatest number of observations.

- Temperature Statistics:
Designed a query to calculate the lowest, highest, and average temperatures, specifically filtering on the station ID of the most-active station found in the previous query.

- Temperature Observation (TOBS) Analysis:
Created a query to obtain the temperature observations (TOBS) for the station with the most observations.
The query focused on retrieving data from the previous 12 months of TOBS observations for that specific station.

- Visualization:
Plotted the TOBS results as a histogram with 12 bins to provide a visual representation of the temperature distribution.

![image](https://github.com/JasmineBamba/sql-alchemy/assets/135666038/d7fcb88a-e872-4633-97f2-103a5d9b99a5)

- Session Closure:
Closed the SQLAlchemy session to release system resources and complete the analysis.


## Part2: Design Climate App

