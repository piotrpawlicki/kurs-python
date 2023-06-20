import pymysql
from user_functions import *
import datetime as t
from tabulate import tabulate


class Cinema:
    def __init__(self):
        self.db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'password',
    database = 'kino'
    )

    def display_available_seats(self, screening_id):
        cursor = self.db.cursor()
        query = f"""
        SELECT s.seat_number, b.booking_id
        FROM Seats s
        LEFT JOIN (
            SELECT seat_number, booking_id
            FROM Bookings
            WHERE screening_id = {screening_id}
        ) b ON s.seat_number = b.seat_number
        WHERE s.room_id = (
            SELECT room_id
            FROM Screenings
            WHERE screening_id = {screening_id}
        )
        """
        cursor.execute(query)
        result = cursor.fetchall()

        cursor2 = self.db.cursor()
        query2 = f"""
        SELECT Screenings.room_id, Rooms.capacity
        FROM Screenings
        JOIN Rooms ON Screenings.room_id = Rooms.room_id
        WHERE Screenings.screening_id = {screening_id}
        """
        cursor2.execute(query2)
        room_id, capacity = cursor2.fetchone()

        print(f"Available seats for Screening ID {screening_id} in Room ID {room_id}:")
        row_str = ""
        for i in range(1, capacity + 1):
            seat_found = False
            for seat in result:
                if seat[0] == i and seat[1] is None:
                    seat_found = True
                    break

            if seat_found:
                row_str += str(i) + " "
            else:
                row_str += "X "

            if i % 10 == 0:
                print(row_str)
                row_str = ""

        cursor.close()
        cursor2.close()

    def check_seat(self, screening_id, seat):
        cursor = self.db.cursor()

        # Check if the seat exists for the specified screening
        seat_id = f"CONCAT({screening_id}, '_', {int(seat)})"
        check_query = f"SELECT seat_number FROM Seats WHERE seat_id = {seat_id}"
        cursor.execute(check_query)
        result = cursor.fetchone()

        if result is None:
            print("The seat does not exist.")
            return False

        # Check if the seat is already reserved for the specified screening
        check_query = f"SELECT seat_number FROM Bookings WHERE seat_number = {int(seat)} AND screening_id = {screening_id}"
        cursor.execute(check_query)
        result = cursor.fetchone()

        if result is not None:
            print("The seat is already reserved.")
            return False

        cursor.close()
        return True

    def make_reservation(self, screening_id, seats):
        cursor = self.db.cursor()

        # Check if the seats exist for the specified screening
        for seat in seats:
            if not self.check_seat(screening_id, seat):
                return

        # Generate a unique booking_id for the reservation
        booking_id_query = f"SELECT COALESCE(MAX(booking_id), 0) + 1 FROM Bookings"
        cursor.execute(booking_id_query)
        booking_id = cursor.fetchone()
        booking_id = booking_id[0]

        # Make reservations for the available seats
        insert_query = f"INSERT INTO Bookings (booking_id, screening_id, seat_number) VALUES "
        insert_values = []
        for seat in seats:
            insert_values.append(f"({booking_id}, {screening_id}, {int(seat)})")
        insert_query += ", ".join(insert_values)
        cursor.execute(insert_query)

        print(f"Your booking number: {booking_id}")

        self.db.commit()
        cursor.close()

    def cancel_reservation(self, booking_id):
        cursor = self.db.cursor()
        query = f"SELECT seat_number FROM Bookings WHERE booking_id = {booking_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        # result = result[0]

        if result is None:
            print(f"Booking ID {booking_id} does not exist.")
        else:
            delete_QUERY = f"DELETE FROM Bookings WHERE booking_id = {booking_id}"
            cursor.execute(delete_QUERY)
            print(f'Booking {booking_id} is canceled')
            self.db.commit()
        cursor.close()

    def add_movie(self, title, duration):
        cursor = self.db.cursor()
        # Check if the movie already exists
        check_query = f"SELECT title FROM Movies WHERE title = '{title}'"
        cursor.execute(check_query)
        result = cursor.fetchone()
        #result = result[0]
        if result == title:
            print(f"Movie {title} already exists.")
        else:
            query = f"""
                    INSERT INTO Movies (movie_id, title, duration)
                    SELECT COALESCE(MAX(movie_id), 0) + 1, '{title}', {duration}
                    FROM Movies
                    """
            cursor.execute(query)
            self.db.commit()
            print(f"Movie {title} added.")
        cursor.close()

    def add_screening(self, movie_id, room_id, start_time):
        cursor = self.db.cursor()

        # Check if the movie exists
        check_query = f"SELECT title FROM Movies WHERE movie_id = {movie_id}"
        cursor.execute(check_query)
        result = cursor.fetchone()

        if result is None:
            print(f"Movie ID {movie_id} does not exist.")
            return

        # Check if the room exists
        check_query = f"SELECT room_id FROM Rooms WHERE room_id = {room_id}"
        cursor.execute(check_query)
        result = cursor.fetchone()

        if result is None:
            print(f"Room ID {room_id} does not exist.")
            return

        # Check if the screening already exists
        check_query = f"SELECT screening_id FROM Screenings WHERE room_id = {room_id} AND start_time = '{start_time}'"
        cursor.execute(check_query)
        result = cursor.fetchone()

        if result is not None:
            print(f"Screening ID {result[0]} already exists.")
            return

        # Check if the time slot is available
        check_query = f"""
        SELECT MAX(end_time) 
        FROM Screenings 
        WHERE room_id = {room_id} AND end_time <= '{start_time}'
        """
        cursor.execute(check_query)
        result = cursor.fetchone()
        if result[0] is not None:
            proposed_start_time = (result[0] + t.timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"The selected time slot is not available. Proposed start time: {proposed_start_time}")
            answer = input('Do you accept proposed time? (Y/N) ')
            if answer.lower() == 'y':
                start_time = proposed_start_time
                # Add the new screening

                insert_query = f"""
                    INSERT INTO Screenings ( movie_id, room_id, start_time, end_time)
                    SELECT  {movie_id}, {room_id}, '{start_time}', DATE_ADD('{start_time}', INTERVAL m.duration MINUTE)
                    FROM Movies m
                    WHERE m.movie_id = {movie_id}
                """
                cursor.execute(insert_query)
                self.db.commit()
                print("Screening added successfully.")
                result = cursor.fetchone()
            else:
                print("Screening not added.")
            return
        else:
            # Add the new screening
            insert_query = f"""
                    INSERT INTO Screenings ( movie_id, room_id, start_time, end_time)
                    SELECT  {movie_id}, {room_id}, '{start_time}', DATE_ADD('{start_time}', INTERVAL m.duration MINUTE)
                    FROM Movies m
                    JOIN Screenings s on m.movie_id = s.movie_id
                    WHERE m.movie_id = {movie_id}
            """
            cursor.execute(insert_query)
            self.db.commit()
            print("Screening added successfully.")

        cursor.close()

    def display_screenings(self):
        cursor = self.db.cursor()
        query = f"""
        SELECT s.screening_id, s.start_time, m.title, r.room_name
        FROM Screenings s
        JOIN Movies m on s.movie_id = m.movie_id
        JOIN Rooms r on s.room_id = r.room_id
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print(tabulate(result, headers=['Screening ID', 'Start Time', 'Movie Title', 'Room Number']))
        cursor.close()

    def add_room(self, room_name, capacity):
        cursor = self.db.cursor()
        # Check if the room already exists
        check_query = f"SELECT room_name FROM Rooms WHERE room_name = '{room_name}'"
        cursor.execute(check_query)
        result = cursor.fetchone()
        #result = result[0]
        if result == room_name:
            print(f"Room {room_name} already exists.")
        else:
            query = f"""
                    INSERT INTO Rooms (room_id, room_name, capacity)
                    SELECT COALESCE(MAX(room_id), 0) + 1, '{room_name}', {capacity}
                    FROM Rooms
                    """
            cursor.execute(query)
            self.db.commit()
            print(f"Room {room_name} added.")
        cursor.close()

    def display_movies(self):
        cursor = self.db.cursor()
        query = f"""
        SELECT movie_id, title, duration
        FROM Movies
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print(tabulate(result, headers=['Movie ID', 'Title', 'Duration']))
        cursor.close()

    def display_rooms(self):
        cursor = self.db.cursor()
        query = f"""
        SELECT room_id, room_name, capacity
        FROM Rooms
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print(tabulate(result, headers=['Room ID', 'Room Name', 'Capacity']))
        cursor.close()

    def max_screening_id(self):
        cursor = self.db.cursor()
        query = f"""
        SELECT MAX(screening_id)
        FROM Screenings
        """
        cursor.execute(query)
        result = cursor.fetchone()
        result = result[0]
        return result

    def select_seats(self, screening_id):
        cursor = self.db.cursor()

        # Retrieve the room capacity for the specified screening
        capacity_query = f"SELECT capacity FROM Rooms WHERE room_id = (SELECT room_id FROM Screenings WHERE screening_id = {screening_id})"
        cursor.execute(capacity_query)
        capacity = cursor.fetchone()[0]

        # Display available seats for the specified screening
        available_seats_query = f"""
            SELECT seat_number
            FROM Seats
            WHERE seat_id NOT IN (
                SELECT CONCAT({screening_id}, '_', seat_number)
                FROM Bookings
                WHERE screening_id = {screening_id}
            )
            ORDER BY seat_number
        """
        cursor.execute(available_seats_query)
        available_seats = [str(row[0]) for row in cursor.fetchall()]

        print(f"Available seats for Screening ID {screening_id}:\n{' '.join(available_seats)}")

        # Prompt the user to select seats
        selected_seats = input("Enter seat numbers (comma-separated): ").split(",")

        # Validate the selected seats
        valid_seats = []
        for seat in selected_seats:
            seat = seat.strip()
            if seat.isdigit() and 1 <= int(seat) <= capacity:
                valid_seats.append(seat)

        if not valid_seats:
            print("Invalid seat selection.")
            return

        # Make the reservation for the selected seats
        self.make_reservation(screening_id, valid_seats)

        cursor.close()