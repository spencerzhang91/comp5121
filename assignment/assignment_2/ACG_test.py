# This sql test if to make sure about the Apriori Candidate Generation algorithm.

import sqlite3
conn = sqlite3.connect('pageview.db')
c = conn.cursor()

try:
    c.execute("DROP TABLE candidate")
    c.execute("DROP TABLE webview")
except sqlite3.OperationalError:
    print("Starts new test below:\n")
else:
    print("Starts new test below clean:\n")

c.execute("CREATE TABLE candidate (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, litemset1 text, litemset2 text, litemset3 text)")
c.execute("CREATE TABLE webview (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, litemset1 text, litemset2 text)")

c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (1,11);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (3,4);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (5,6);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (6,7);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (6,8);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (7,8);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (1,1);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (3,3);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (6,6);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (7,7);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (8,8);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (11,1);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (4,3);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (6,5);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (7,6);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (8,6);')
c.execute('INSERT INTO webview (litemset1, litemset2) VALUES (8,7);')

conn.commit()

for row in c.execute("SELECT * FROM webview"):
    print(row)
print('-------------\n\n\n\n')
co = 0
for row in c.execute('''SELECT p.litemset1, p.litemset2, q.litemset2
             FROM webview p, webview q
             WHERE p.litemset1 = q.litemset1'''):
    co += 1
    print(row)
print(co)