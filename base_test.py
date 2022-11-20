import sqlite3 as sq

#Database connection and create
#con = sq.connect("first db")
with sq.connect("store.db") as con:
    cur = con.cursor() #database management

    #Create table products
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
    name TEXT,
    sale INTEGER,
    sells INTEGER
    )
    """)

    #Program begin
    a = True
    while a:
        name = str(input("The name of your product: "))
        sale = int(input("How many items would you like to buy: "))
        sells = int(input("TOTAL: "))

        #Check for repetition
        cur.execute(f"SELECT name FROM products WHERE name = '{name}'")
        if cur.fetchone() is None:
            cur.execute(f"INSERT INTO products VALUES(?, ?, ?)", (name, sale, sells))
            print(f"record {name} saved")
        else:
            print("this entry already exists!")

            # if record exist. Updating
            b = input('want to update the post?')
            if b == "yes":
                cur.execute(f"UPDATE products SET name = '{name}', sale = '{sale}', sells = '{sells}' WHERE name = '{name}' ")
                print(f"record {name} updated")
            else:
                print("next")

        #breack or repeat
        b = input("would you like to continue: ")
        if "no" == b:
            a = False

    for value in cur.execute("SELECT * FROM products"):
        print(f"Database: \n{value}")

input("enter for escepe")
"""
    cur.execute("SELECT * FROM users WHERE  score <5 ORDER BY score DESC LIMIT 5 ")
    #resulte = cur.fetchone()
    #resulte2 =  cur.fetchmany(2)
    for i in cur:
        print(i)
        """
