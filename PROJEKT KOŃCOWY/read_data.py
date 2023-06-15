import datetime
import pymysql

##połączenie z bazą danych

connection = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'password',
    database = 'kino'
)
def execute_query(query):
    # Utworzenie obiektu kursora
    cursor = connection.cursor()
    # Wykonanie zapytania SQL
    cursor.execute(query)
    # Pobranie wyników zapytania
    results = cursor.fetchall()
    # Zamknięcie kursora i połączenia
    cursor.close()
    connection.close()
    return results

def display_movies():
    query = """    SELECT
        s.screening_id AS 'nr Seansu',
        m.title AS 'Tytuł',
        m.duration AS 'Czas Trwania',
        s.start_time AS 'Początek seansu',
        r.capacity - COALESCE(SUM(b.seat_number), 0) AS 'Wolne miejsca'
    FROM
        Movies m
        LEFT JOIN Screenings s ON m.movie_id = s.movie_id
        LEFT JOIN Bookings b ON s.screening_id = b.screening_id
        LEFT JOIN Rooms r ON s.room_id = r.room_id
    GROUP BY
        s.screening_id, m.title, m.duration, s.start_time, r.capacity"""
    movies = execute_query(query)
    return movies
    #return    print(f"{title}, Czas trwania: {duration} min, Początek seansu: {start_time}, wolne miejsca : {capacity}")


def make_reservation():
    movie = display_movies()
    screening_id, title, duration, start_time, capacity = movie
    if capacity > 0 :
        pass
    else:
        pass


def cancel_reservation():
    pass

def check_input(user_input, type):
    while True:
        try:
            type(user_input)
            break
        except TypeError:
            print('Type Errpr')
        except ValueError:
            print('Type Error')

