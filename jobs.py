import _sqlite3 as sq

def insert_table_j(cur,name, age, table):
    cur.execute(f"INSERT INTO '{table}' VALUES(?, ?)", (name, age))
    print(f"record {name} saved")

def update_table_j(cur, name, age, table):
    cur.execute(f"UPDATE '{table}' SET name = '{name}', age = '{age}'  WHERE name = '{name}' ")
    print(f"record {a} updated")

def print_db(cur):
    for value in cur.execute(f"SELECT * FROM jobs"):
        print(f"Database: \n{value}")

    for value in cur.execute(f"SELECT * FROM customers"):
        print(f"Database: \n{value}")


def insert_table_c(cur, number, money, table):
    cur.execute(f"INSERT INTO '{table}' VALUES(?, ?)", (number, money))
    print(f"record {number} saved")

with sq.connect("job.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS jobs(
    number AUTOINCREMENT PRIMARY KEY,
    name TEXT,
    age INTEGER 
    )
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS customers(
       number INTEGER,
       money INTEGER 
       )
       """)

    a = True
    while a:
        table = input("name table: ")
        if table == "jobs":
            name = input("input name: ")
            age = input("input age: ")

            cur.execute(f"SELECT name FROM '{table}' WHERE name = '{name}'")

            if cur.fetchone() is None:
                insert_table_j(cur, name, age, table)

            else:
                print("this entry already exists!")

                b = input('want to update the post?')

                if b == "yes":
                    update_table_j(cur, name, age, table)
                else:
                    print("next")



        elif table == "customer:":
            number = input("input number: ")
            money = input("input money: ")

            insert_table_c(cur, number, money, table)

        else:
            print(f"table {table} not exist! repeat")

        b = input("would you like to continue: ")
        if "no" == b:
            a = False

    print_db(cur)

input("enter for escepe")