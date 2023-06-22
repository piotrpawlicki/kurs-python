# Program do rezerwacji miejsc w kinie
> Opis projektu końcowego

## Spis treści
* [Podsumowanie](#Podsumowanie)
  * [Opis struktury danych](#Opis Struktury danych)
  * [Kod wykorzystany do stworzenia struktury danych](#Kod wykorzystany do stworzenia struktury danych)
  * [Wypełnienie tabeli przykłądowymi danymi](#Wypełnienie tabeli przykłądowymi danymi)

* [Wykorzystane_technologie](#Wykorzystane technologie)
* [Podziękowania](#Podziękowania)
* [Autor](#Autor)


## Podsumowanie
 - ### **Opis struktury danych**
  
1. Tabela "Movies":

   *  movie_id: 
   *  ID filmu (klucz główny)
   *  title: Tytuł filmu
   *  duration: Czas trwania filmu

2. Tabela "Rooms":

   * room_id: ID sali (klucz główny)
   * room_name: Nazwa sali
   * capacity: Pojemność sali (liczba miejsc)
   
3. Tabela "Screenings":

   * screening_id: ID seansu (klucz główny)
   * movie_id: ID filmu (klucz obcy powiązany z tabelą "Movies")
   * room_id: ID sali (klucz obcy powiązany z tabelą "Rooms")
   * start_time: Czas rozpoczęcia seansu
   
4. Tabela "Bookings":

   * booking_id: ID rezerwacji (klucz główny)
   * screening_id: ID seansu (klucz obcy powiązany z tabelą "Screenings")
   * seat_number: Numer miejsca zarezerwowanego



W powyższej strukturze mamy oddzielne tabele dla filmów, sal, seansów i rezerwacji. Powiązania między nimi są realizowane za pomocą kluczy obcych.

W tabeli "Movies" przechowujemy informacje o filmach, takie jak tytuł i czas trwania.

Tabela "Rooms" przechowuje informacje o salach, takie jak nazwa i pojemność.

W tabeli "Screenings" przechowujemy informacje o seansach, takie jak film (za pomocą klucza obcego do tabeli "Movies"), sala (za pomocą klucza obcego do tabeli "Rooms") oraz czas rozpoczęcia seansu.

W tabeli "Bookings" przechowujemy informacje o rezerwacjach, takie jak seans (za pomocą klucza obcego do tabeli "Screenings") oraz numer zarezerwowanego miejsca.

W tabeli "Rooms" przechowujemy informację o miejscach w danych salach kinowych.


### Kod wykorzystany do stworzenia struktury danych
````
DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies (
  movie_id INT PRIMARY KEY,
  title VARCHAR(255),
  duration INT
);



DROP TABLE IF EXISTS Rooms;
CREATE TABLE Rooms (
  room_id INT PRIMARY KEY,
  room_name VARCHAR(255),
  capacity INT
);

DROP TABLE IF EXISTS Seats;
CREATE TABLE Seats (
  seat_id VARCHAR(255) PRIMARY KEY,
  room_id INT,
  seat_number INT,
  FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

DROP TABLE IF EXISTS Screenings;
CREATE TABLE Screenings (
  screening_id INT AUTO_INCREMENT PRIMARY KEY,
  movie_id INT,
  room_id INT,
  start_time DATETIME,
  end_time DATETIME,
  FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
  FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);
DROP TABLE IF EXISTS Bookings;
CREATE TABLE Bookings (
  reservation_id INT AUTO_INCREMENT PRIMARY KEY,
  booking_id INT,
  screening_id INT,
  seat_number INT,
  FOREIGN KEY (screening_id) REFERENCES Screenings(screening_id)
);

````

#### Wypełnienie tabeli przykłądowymi danymi
````
INSERT INTO Movies (movie_id, title, duration)
VALUES
  (1, 'Film 1', 120),
  (2, 'Film 2', 105),
  (3, 'Film 3', 90);

-- Wypełnienie tabeli Rooms
INSERT INTO Rooms (room_id, room_name, capacity)
VALUES
  (1, 'Sala 1', 100),
  (2, 'Sala 2', 80);

-- Wypełnienie tabeli Screenings
INSERT INTO Screenings (screening_id, movie_id, room_id, start_time)
VALUES
  (1, 1, 1, '2023-06-07 10:00:00'),
  (2, 1, 1, '2023-06-07 13:00:00'),
  (3, 2, 2, '2023-06-07 15:30:00'),
  (4, 3, 1, '2023-06-07 18:00:00'),
  (5, 3, 2, '2023-06-07 20:30:00');
  
-- Wypełnienie tabeli Seats na podstawie tabeli Rooms
  INSERT INTO Seats (seat_id, room_id, seat_number)
SELECT 
  CONCAT(r.room_id, '_', s.seat_number) AS seat_id,
  r.room_id,
  s.seat_number
FROM Rooms r
CROSS JOIN (
  SELECT 
    (a.a + (10 * b.a) + 1) AS seat_number
  FROM
    (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS a
  CROSS JOIN
    (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS b
) s
WHERE s.seat_number <= r.capacity;
````

## Działanie programu

Do realizacji projektu wykorzystano trzy moduły
1. user_functions.py
2. cinema.py
3. menu.py

 - W module "user_functions.py" wykorzystano funkcje wejścia stworzone podczas kursu
 - Moduł "cinema.py" zawiera definicję klasy Cinema oraz opis wszystkich funkcji w klasie
 - Moduł menu.py zaiwera definicję menu oraz pozwala na uruchomienie programu.

## Wykorzystane technologie
- Python 3.9.13
- PyCharm 2023.1
- MySQL
- MySQL Workbench


## Podziękowania

- Instrukcje do zadań zostały przedstawione na https://github.com/ritaly/CODEME-python23/tree/main/hackaton_01
- Many thanks to StackOverFlow and chat.openai.com :)


## Autor
Created by Piotr Pawlicki (piotr.a.pawlicki@gmail.com)

