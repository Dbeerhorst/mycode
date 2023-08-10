import sqlite3

conn = sqlite3.connect('car_database.db')
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute('DROP TABLE IF EXISTS AutoMakerCarModel')
cursor.execute('DROP TABLE IF EXISTS CarModels')
cursor.execute('DROP TABLE IF EXISTS AutoMakers')

# Create the AutoMakers table
cursor.execute('''
    CREATE TABLE AutoMakers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create the CarModels table
cursor.execute('''
    CREATE TABLE CarModels (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create the AutoMakerCarModel table
cursor.execute('''
    CREATE TABLE AutoMakerCarModel (
        automaker_id INTEGER,
        model_id INTEGER,
        FOREIGN KEY (automaker_id) REFERENCES AutoMakers (id),
        FOREIGN KEY (model_id) REFERENCES CarModels (id),
        PRIMARY KEY (automaker_id, model_id)
    )
''')

conn.commit()
conn.close()

