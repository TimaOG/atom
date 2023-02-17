import requests
import psycopg2

url = "https://spacex-production.up.railway.app/"

query = """
  query ExampleQuery {
  launches {
    id
    mission_id
    rocket {
      rocket {
        id
        name
      }
    }
    mission_name
  }
}


"""

response = requests.post(url=url, json={'query': query})
data = response.json()['data']['launches']


# Подключение к базе данных
conn = psycopg2.connect(dbname="test", user="postgres", password="123", host="127.0.0.1", port=5432)

# Создание курсора
cur = conn.cursor()

# Создание таблицы
cur.execute("""
  CREATE TABLE launches (
    id varchar PRIMARY KEY, 
    mission_id varchar,
    rocket varchar,
    mission_name varchar
  );
  CREATE TABLE rocket (
    id varchar PRIMARY KEY, 
    name varchar
  );
  """)

for el in data:
  cur.execute("INSERT INTO launches (id, mission_id, rocket, mission_name) VALUES (%s, %s, %s, %s)", (el["id"], el["mission_id"], el["rocket"]["rocket"]["id"], el["mission_name"]))
  cur.execute("INSERT INTO rocket (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", (el["rocket"]["rocket"]["id"], el["rocket"]["rocket"]["name"]))

# Сохранение изменений
conn.commit()

cur.execute("SELECT count(*) from launches")
colvo = cur.fetchone()
print("Количество запусков - " + str(colvo[0]))

# Закрытие курсора и соединения с базой данных
cur.close()
conn.close()