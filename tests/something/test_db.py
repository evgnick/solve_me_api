import mysql.connector
import pytest

# Настройки для подключения к базе данных MySQL
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '3135449',
    'database': 'classicmodels'
}


# Функция для подключения к базе данных MySQL
def connect_db():
    return mysql.connector.connect(**DB_CONFIG)


# Фикстура для управления сессией (начало транзакции и откат после теста)
@pytest.fixture
def db_session():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    # Начинаем транзакцию
    conn.start_transaction()

    yield cursor  # Передаем курсор в тесты

    # После выполнения теста откатываем транзакцию
    conn.rollback()
    conn.close()


# Тест, обернутый в транзакционную сессию
def test_add_user(db_session):
    # Пример логики теста, который добавляет пользователя в базу через микросервис
    # response = requests.post('http://localhost:8000/add_user', json={'name': 'John', 'age': 30})
    # assert response.status_code == 200

    db_session.execute("SELECT * FROM offices WHERE city = 'NYC';")
    user = db_session.fetchone()
    print(user)
    assert user is not None
    assert user['city'] == "NYC"

