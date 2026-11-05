# Unit 4 - Python Database, DataFrames, and Charts

This folder contains practical programs for MySQL database operations, pandas DataFrames, and data visualization with Matplotlib.

## Practicals

| No. | Topic |
|---|---|
| 1 | Connect Python with a MySQL database |
| 2 | Create a table, insert records, and display records |
| 3 | Update records in a MySQL table |
| 4 | Delete records from a MySQL table |
| 5 | Demonstrate DataFrames in Python |
| 6 | Create DataFrames in different ways |
| 7 | Create a pie chart |
| 8 | Create a histogram |
| 9 | Create a bar graph |
| 10 | Create a line graph |

## Requirements

- Python 3
- MySQL Server and `mysql-connector-python` for Practicals 1-4
- `pandas` for Practical 5
- `pandas` and `numpy` for Practical 6
- `matplotlib` for Practicals 7-10

Install the Python packages with:

```bash
python -m pip install mysql-connector-python pandas numpy matplotlib
```

For the MySQL programs, update the connection settings in each script to match your local MySQL configuration. Practicals 2-4 use the `college` database and `student` table.

Run a practical from this folder with:

```bash
python "01.Connect Python with MySQL Database.py"
```
