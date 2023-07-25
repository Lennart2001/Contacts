#prog
def showcase_commands():
    print('\033[1m' + '> Asterisks Search (Case Insensitive)' + '\033[0m')
    print(" - SELECT name FROM test_table WHERE name LIKE 'Le%';")
    print(" - SELECT name FROM test_table WHERE name LIKE '%Le';")
    print(" - SELECT name FROM test_table WHERE name LIKE '%Le%';")
    print(" - SELECT name FROM test_table WHERE name LIKE '%L%e%';")

    print('\033[1m' + '> Asterisks Search (Case Insensitive) TWO Columns' + '\033[0m')
    print(" - SELECT name, age FROM test_table WHERE name LIKE 'Le%' AND age > 30;")
    print(" - SELECT name, age FROM test_table WHERE name LIKE 'Le%' OR age > 30;")
    print(" - SELECT name, surname FROM test_table WHERE name LIKE 'Le%' AND surname LIKE '%son';")

    print('\033[1m' + '> Limit Search' + '\033[0m')
    print(" - SELECT name FROM test_table LIMIT 50;")

    print('\033[1m' + '> Sorted Search' + '\033[0m')
    print(" - SELECT name FROM test_table ORDER BY my_column DESC;")
    print(" - SELECT * FROM test_table ORDER BY my_column ASC;")

    print('\033[1m' + '> Two Column Asterisks with Limit and Sorted' + '\033[0m')
    print(" - SELECT name, surname FROM test_table WHERE name LIKE 'Le%' AND surname LIKE '%son' ORDER BY name DESC LIMIT 50;")

    print('\033[1m' + '> Delete a Table' + '\033[0m')
    print(" - DROP TABLE test_table;")

    print('\033[1m' + '> Create a Table' + '\033[0m')
    print(" - CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, birthday DATE);")


showcase_commands()

