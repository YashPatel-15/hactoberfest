import sqlite3
con = sqlite3.connect('vk.db')
cur = con.cursor()

# Create table

cur.execute('''CREATE TABLE Bank (account_no real, CustomerName text, Balance real, phone real, address text)''')

# Insert a row of data
cur.execute("INSERT INTO Bank VALUES (101,'virani keval',40000,9726189535,'Vadodara')")
cur.execute("INSERT INTO Bank VALUES (102,'sapan shah',30000,1234567890,'jamnagar')")
cur.execute("INSERT INTO Bank VALUES (103,'uttam pragda',15000,2345678901,'Surat')")
cur.execute("INSERT INTO Bank VALUES (104,'Kshitij Naria',45000,3456789012,'Surat')")

#update a row of data
cur.execute("UPDATE Bank SET address = 'Mumbai' WHERE account_no = 104")


#deletion of a row
cur.execute("DELETE from Bank WHERE account_no = 103 ")

for row in cur.execute('SELECT * FROM Bank WHERE Balance >= 20000'):
       print(row)
# Save (commit) the changes
con.commit()
