column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]

db = [dict(zip(column_names, row)) for row in db_rows]

CN, DB_R = zip(*db)
print(list(CN), list())