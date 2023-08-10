import sqlite3

def query_data():
    conn = sqlite3.connect('car_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT AutoMakers.name, GROUP_CONCAT(CarModels.name) FROM AutoMakers ' +
                   'JOIN AutoMakerCarModel ON AutoMakers.id = AutoMakerCarModel.automaker_id ' +
                   'JOIN CarModels ON AutoMakerCarModel.model_id = CarModels.id ' +
                   'GROUP BY AutoMakers.name')

    automaker_models = cursor.fetchall()

    for automaker, models in automaker_models:
        print(f"Auto Maker: {automaker}")
        print(f"Models: {models}")
        print("--------------------")

    conn.close()

if __name__ == '__main__':
    query_data()

