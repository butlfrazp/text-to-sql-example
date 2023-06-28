# LLM SQL Query Generator <!-- omit in toc -->

This repository contains the modules and logic to create SQL queries from a sql database.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Getting started](#getting-started)
  - [Creating the SQL Tables](#creating-the-sql-tables)
  - [Running the program](#running-the-program)


## Getting started

It is recommended to use a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) for this project.
There are two necessary components to get started

### Creating the SQL Tables

To get started, the SQL tables need to be created to run this project.
The SQL tables are used as the `main` program will read the tables to construct the queries.
There are sample scripts under `src/database/sample/Tables` to create different tables.
Feel free to either get started with these scripts or create your own tables.

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
