import pymysql
from user_functions import *

class Cinema:
    def __init__(self):
        self.db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'password',
    database = 'kino'
    )

    def display_available_seats(self, room_id):
        cursor = self.db.cursor()
        query = f"SELECT seat_number FROM Seats WHERE room_id = {room_id}"
        cursor.execute(query)
        result = cursor.fetchall()

        print(f"Available seats for Room {room_id}:")
        row_str = ""
        for seat in result:
            if seat[0] is None:
                row_str += "X "
            else:
                row_str += "_ "

            if len(row_str) % 10 == 0:
                print(row_str)
                row_str = ""

        cursor.close()


    def make_reservation(self, room_id, seat_number):
        cursor = self.db.cursor()
        query = f"SELECT seat_number FROM Seats WHERE room_id = {room_id} AND seat_number = {seat_number}"
        cursor.execute(query)
        result = cursor.fetchone()
        if result is None:
            print(f"Seat {seat_number} in Room {room_id} does not exist.")
        elif result[0] is not None:
            print(f"Seat {seat_number} in Room {room_id} is already reserved.")
        else:
            update_query = f"UPDATE Seats SET seat_number = {seat_number} WHERE room_id = {room_id} AND seat_number IS NULL"
            cursor.execute(update_query)
            self.db.commit()
            print(f"Reservation successful. Seat {seat_number} in Room {room_id} is now reserved.")
        cursor.close()


        ## przerób, aby cancel reservation odbywało się za pomocą reservation id
    def cancel_reservation(self, room_id, seat_number):
        cursor = self.db.cursor()
        query = f"SELECT seat_number FROM Seats WHERE room_id = {room_id} AND seat_number = {seat_number}"
        cursor.execute(query)
        result = cursor.fetchone()

        if result is None:
            print(f"Seat {seat_number} in Room {room_id} does not exist.")
        elif result[0] is None:
            print(f"Seat {seat_number} in Room {room_id} is not reserved.")
        else:
            update_query = f"UPDATE Seats SET seat_number = NULL WHERE room_id = {room_id} AND seat_number = {seat_number}"
            cursor.execute(update_query)
            self.db.commit()
            print(f"Reservation for Seat {seat_number} in Room {room_id} is canceled.")

        cursor.close()

    def add_screening(self, room_id, screening_time):
        cursor = self.db.cursor()
        query = f"INSERT INTO Screenings (room_id, screening_time) VALUES ({room_id}, '{screening_time}')"
        cursor.execute(query)
        self.db.commit()
        print(f"Screening added to Room {room_id} at {screening_time}.")
        cursor.close()
