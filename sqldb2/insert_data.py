import sqlite3

def insert_data():
    conn = sqlite3.connect('car_database.db')
    cursor = conn.cursor()

    # Insert data into AutoMakers table
    automakers = [('Toyota',), ('Ford',), ('Honda',)]
    cursor.executemany('INSERT INTO AutoMakers (name) VALUES (?)', automakers)

    # Insert data into CarModels table
    car_models = [('Corolla',), ('Camry',), ('Mustang',), ('Civic',), ('Accord',)]
    cursor.executemany('INSERT INTO CarModels (name) VALUES (?)', car_models)

    # Insert data into AutoMakerCarModel table
    automaker_car_model = [
        (2, 3),  # Ford - Mustang
        (3, 5),  # Honda - Accord
        (3, 4),  # Honda - Civic
        (1, 2),  # Toyota - Camry
        (1, 1)   # Toyota - Corolla
    ]
    cursor.executemany('INSERT INTO AutoMakerCarModel (automaker_id, model_id) VALUES (?, ?)', automaker_car_model)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_data()

