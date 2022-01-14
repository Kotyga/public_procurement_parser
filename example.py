import sqlite3

conn = sqlite3.connect('cards.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS cards(
   number INT,
   amount DOUBLE);
""")
val = [('0338100000521000100', '448400.00'), ('0338100000521000099', '80500.00'),
       ('0161100008221000004', '35000.00'), ('0347000000121000054', '125051.45'),
       ('32110590678', '21109928.54'), ('32110750824', '5629302.00'),
       ('0347000000121000053', '144913.80'), ('0161100008221000003', '580000.00')]
cur.executemany("INSERT INTO cards VALUES(?, ?);", val)
conn.commit()

cur.execute("SELECT * FROM cards;")
results = cur.fetchall()
print(results)
