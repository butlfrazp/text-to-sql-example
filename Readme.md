# LLM SQL Query Generator <!-- omit in toc -->

This repository contains the modules and logic to create SQL queries from a sql database.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Getting started](#getting-started)
  - [Creating the SQL Tables](#creating-the-sql-tables)
  - [Input Prompt](#input-prompt)
  - [Running the program](#running-the-program)
  - [Examples](#examples)


## Getting started

It is recommended to use a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) for this project.
There are two necessary components to get started

### Creating the SQL Tables

To get started, the SQL tables need to be created to run this project.
The SQL tables are used as the `main` program will read the tables to construct the queries.
There are sample scripts under `src/database/sample/Tables` to create different tables.
Feel free to either get started with these scripts or create your own tables.

### Input Prompt

The input prompt uses the default prompts from langchain for sql databases.
Examples of these prompts can be found [here](https://github.com/hwchase17/langchain/blob/master/langchain/chains/sql_database/prompt.py).
With the prompt, the table information and samples are passed to the prompt as well as question.

### Running the program

To run the program, start by copying `src/sample/.env.sample` to `src/sample/.env`.
Make sure to update the `env` file with the correct values.
If using the `devcontainer`, the DB connection string should match the DB connection string from the sample env file.
Next, run the program with the following command.

```python
# cd src/sample
# pip install -r requirements.txt (if not in dev conainer, it is recommended to use a virtual environment)
python -m main
```

The program will ask for a query in english. Please write the english query in the terminal.

### Examples

- Get all restaurants

  ```sql
  SELECT [Id], [Name] FROM [Restaurant]
  ```

- Get all restaurants that have a menu item that has a price less than 3

  ```sql
  SELECT DISTINCT r.[Name] 
  FROM [Restaurant] r 
  JOIN [Menu] m ON r.[Id] = m.[RestaurantId] 
  JOIN [MenuItem] mi ON m.[Id] = mi.[MenuId] 
  WHERE mi.[Price] < 3
  ```

- Get all resturants that have a breakfast menu

  ```sql
  SELECT [Restaurant].[Name]
  FROM [Restaurant]
  JOIN [Menu] ON [Restaurant].[Id] = [Menu].[RestaurantId]
  ```

- Get all resturants that have a lunch menu and an average rating of above 3

  ```sql
  SELECT DISTINCT R.[Name]
  FROM [Restaurant] R
  INNER JOIN [Menu] M ON R.[Id] = M.[RestaurantId]
  INNER JOIN [Rating] Ra ON R.[Id] = Ra.[RestaurantId]
  WHERE M.[MenuType] = 'Lunch'
  GROUP BY R.[Name]
  HAVING AVG(Ra.[Stars]) > 3
  ```

- Select the lunch menu items of the restaurant that has the highest average stars and the restaurant should have a lunch menu

  ```sql
  SELECT TOP 5 [MenuItem].[Id], [MenuItem].[MenuId], [MenuItem].[Name], [MenuItem].[Price]
  FROM [MenuItem]
  JOIN [Menu] ON [MenuItem].[MenuId] = [Menu].[Id]
  JOIN [Restaurant] ON [Menu].[RestaurantId] = [Restaurant].[Id]
  WHERE [Menu].[MenuType] = 'Lunch'
  AND [Restaurant].[Id] = (
      SELECT TOP 1 [Restaurant].[Id]
      FROM [Restaurant]
      JOIN [Menu] ON [Restaurant].[Id] = [Menu].[RestaurantId]
      JOIN [Rating] ON [Restaurant].[Id] = [Rating].[RestaurantId]
      WHERE [Menu].[MenuType] = 'Lunch'
      GROUP BY [Restaurant].[Id]
      ORDER BY AVG([Rating].[Stars]) DESC
  )
  ```

- Select the dinner menu items of the restaurant that has the highest average stars

  ```sql
  SELECT TOP 5 [MenuItem].[Id], [MenuItem].[MenuId], [MenuItem].[Name], [MenuItem].[Price]
  FROM [MenuItem]
  JOIN [Menu] ON [MenuItem].[MenuId] = [Menu].[Id]
  JOIN [Restaurant] ON [Menu].[RestaurantId] = [Restaurant].[Id]
  WHERE [Menu].[MenuType] = 'Dinner'
  AND [Restaurant].[Id] = (
      SELECT TOP 1 [Restaurant].[Id]
      FROM [Restaurant]
      JOIN [Rating] ON [Restaurant].[Id] = [Rating].[RestaurantId]
      GROUP BY [Restaurant].[Id]
      ORDER BY AVG([Rating].[Stars]) DESC
  )
  ORDER BY [MenuItem].[Id] ASC
  ```