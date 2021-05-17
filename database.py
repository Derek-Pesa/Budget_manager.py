import sqlite3

conn = sqlite3.connect('fundDatabase.db')
c = conn.cursor()


# c.execute("""CREATE TABLE user001 (
#        first_name text string PRIMARY KEY,
#        second_name text,
#        id_number text,
#        phone_number text,
#        email text,
#        pin text
# )""")
# c.execute("""CREATE TABLE budgets (
#        budget_number integer PRIMARY KEY,
#        budget_name text,
#        budget_cost integer,
#        merit text,
#        frequency text
# )""")


def create_account(name1, name2, i_d, tel, email, pin):
    conn.execute("""INSERT INTO user001 (first_name, second_name, id_Number, phone_number, email, pin)
            VALUES (?, ?, ?, ?, ?, ?)""", (name1, name2, i_d, tel, email, pin))
    conn.commit()


def create_budget(bud_num, bud_name, bud_cost, bud_merit, freq):
    conn.execute("""INSERT INTO budgets (budget_number, budget_name, budget_cost, merit, frequency)
    VALUES (?, ?, ?, ?, ?)""", (bud_num, bud_name, bud_cost, bud_merit, freq))
    conn.commit()


def delete_bud(budget_num):
    conn.execute('DELETE FROM budgets WHERE budget_number = ?', (budget_num,))
    conn.commit()


def loggingInCheck(tel):
    c.execute("SELECT pin FROM user001 WHERE phone_number = ?", (tel,))
    xx = c.fetchall()
    for k in xx:
        return k


def settleBills():
    c.execute("SELECT sum(budget_cost) AS 'Total cost' FROM budgets")
    xx = c.fetchone()
    for k in xx:
        return k


def check_bill_cost(bud_num_set):
    c.execute("SELECT budget_cost FROM  budgets WHERE budget_number = ?", (bud_num_set,))
    aa = c.fetchone()
    for v in aa:
        return v


def updateBillBal(bal, bud_num_set):
    conn.execute("UPDATE budgets SET budget_cost = ? where budget_number = ?", (bal, bud_num_set,))
    conn.commit()


names = []


def get_budget_names():
    c.execute("SELECT budget_name FROM budgets")
    bn = c.fetchall()
    for k in bn:
        names.append(k)

# conn.execute("DROP TABLE user001")
# c.execute("SELECT budget_name FROM budgets WHERE budget_number = 2")
# print(c.fetchall())
# c.execute("DELETE FROM budgets WHERE budget_name == 'water'")
# conn.commit()


# non = "derek"
# nan = []

# c.execute("SELECT pin FROM user001 WHERE phone_number = '0741120439'")
# spent = c.fetchone()
# print(spent)

# c.execute("SELECT sum(budget_cost) AS 'Total cost' FROM budgets")
# vv = c.fetchone()
# print(vv)
# bud_num_set = 1
# c.execute("SELECT budget_cost FROM  budgets WHERE budget_number = ?", (bud_num_set,))
# aa = c.fetchone()
# print(aa)
