import sqlite3

def create_tables():
    conn = sqlite3.connect("powerball.db")
    c = conn.cursor()
    
    c.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='users'
    ''')
    if not c.fetchone():
        c.execute('''
            CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                email TEXT UNIQUE NOT NULL,
                                password TEXT NOT NULL)
        ''')
    c.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='numbers'
    ''')
    if not c.fetchone():
        c.execute('''
            CREATE TABLE numbers (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  user_id INTEGER,
                                  main_numbers TEXT NOT NULL,
                                  powerball INTEGER NOT NULL,
                                  FOREIGN KEY (user_id) REFERENCES users(id))
        ''')
    c.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='history'
    ''')
    if not c.fetchone():
        c.execute('''
            CREATE TABLE history (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 main_numbers TEXT NOT NULL,
                                 powerball INTEGER NOT NULL,
                                 date DATE NOT NULL)
        ''')
    conn.commit()
    conn.close()

def add_user(name, email, password):
        conn = sqlite3.connect("powerball.db")
        c = conn.cursor()
        c.execute("INSERT INTO numbers (user_id, main_numbers, powerball) VALUES (?, ?, ?)", (user_id, str(main_numbers), powerball))
        conn.commit()
        conn.close()

def add_history(main_numbers, powerball, date):
    conn = sqlite3.connect("powerball.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (main_numbers, powerball, date) VALUES (?, ?, ?)", (str(main_numbers), powerball, date))
    conn.commit()
    conn.close()

def add_numbers(user_id, main_numbers, powerball):
    conn = sqlite3.connect("powerball.db")
    c = conn.cursor()
    c.execute("INSERT INTO numbers (user_id, main_numbers, powerball) VALUES (?, ?, ?)", (user_id, str(main_numbers), powerball))
    conn.commit()
    conn.close()


