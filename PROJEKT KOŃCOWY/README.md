# Program do rezerwacji miejsc w kinie
> Opis realizowanych zadań podczas zajęć z dnia 20.05.2023

## Spis treści
* [Podsumowanie](#Podsumowanie)
  * [Opis struktury danych](#WOpis Struktury danych)
  * [Generator Nauczyciela](#Generator Nauczyciela)

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



### Kod wykorzystany do stworzenia struktury danych
````
CREATE TABLE Movies (
  movie_id INT PRIMARY KEY,
  title VARCHAR(255),
  duration INT
);

CREATE TABLE Rooms (
  room_id INT PRIMARY KEY,
  room_name VARCHAR(255),
  capacity INT
);

CREATE TABLE Screenings (
  screening_id INT PRIMARY KEY,
  movie_id INT,
  room_id INT,
  start_time DATETIME,
  FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
  FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

CREATE TABLE Bookings (
  booking_id INT PRIMARY KEY,
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
````
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
# Hackaton-2
