from cinema import Cinema
from user_functions import *
import sys
def display_menu():
    print("======== Cinema Management System ========")
    print("1. Add Movie and screening (only for admins)")
    print("2. Add Room (only for admins)")
    print("3. Make reservation")
    print("4. Cancel reservation")
    print("5. Show all movies")
    print("6. Exit")
    print("=========================================")

def main_menu():
    cinema = Cinema()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1": # Add film
            entry = ask_for_password()
            if entry:
                pass
            else:
                print('Access denied')
                sys.exit()
            question = input("Do you want to add a movie or screening (m/s)? ")
            question = question.lower()
            while True:
                if question == "m":
                    title = input("Enter the movie title: ")
                    duration = int(input("Enter the duration in minutes: "))
                    cinema.add_movie(title, duration)
                    break
                elif question == "s":
                    cinema.display_movies()
                    movie_id = ask_number("Enter the movie ID: ",1,len(cinema.movies))
                    cinema.display_rooms()
                    room_id = ask_number("Enter the room ID: ",1,len(cinema.rooms))
                    cinema.add_screening(movie_id, room_id)
                    break
                else:
                    question = input("Please enter m or s: ")
                    question = question.lower()

        elif choice == "2":
            # Add room
            entry = ask_for_password()
            if entry:
                pass
            else:
                print('Access denied')
            room_name = input("Enter the room name: ")
            # max 1000 places in the room
            capacity = ask_number("Enter the capacity: ",1,1000)
            cinema.add_room(room_name, capacity)
        elif choice == "3":
            cinema.display_screenings()
            screenings = cinema.max_screening_id()
            screening_id = ask_number("On which Film do you want to make a reservation? Enter the screening ID: ",1,screenings)
            cinema.display_available_seats(screening_id)
            while True:
                seats = []
                answer = 'y'
                while answer == 'y':
                    seat_id = ask_number2("Which seat do you want to reserve? Enter the seat ID: ")
                    check_seat = cinema.check_seat(screening_id, seat_id)
                    if check_seat:
                        seats.append(seat_id)
                        answer = ask_yes_no('Would you like to book another seat? (y/n): ')
                    else:
                        print("Please choose another one.")
                        answer = ask_yes_no('Would you like to book another seat? (y/n): ')
                        if answer == 'n':
                            break
                        elif answer == 'y':
                            continue
                        else:
                            print("Invalid choice. Please enter y or n.")
                            break

                if answer == 'n':
                    break
            cinema.make_reservation(screening_id, seats)
        elif choice == "4":
            # delete booking
            booking_id = ask_number2("Enter the booking ID: ")
            cinema.cancel_reservation(booking_id)
        elif choice == "5":
             cinema.display_movies()
             answer = ask_yes_no('Would you like to see particular screenings? (y/n): ')
             if answer == 'n':
                 pass
             elif answer == 'y':
                cinema.display_screenings()
                answer2 = ask_yes_no('Would you like to make a reservation? (y/n): ')
                if answer2 == 'n':
                    pass
                elif answer2 == 'y':
                    screenings = cinema.max_screening_id()
                    screening_id = ask_number( "On which Film do you want to make a reservation? Enter the screening ID: ", 1, screenings)
                    cinema.display_available_seats(screening_id)
                    seat_id = ask_number2("Which seat do you want to reserve? Enter the seat ID: ")
                    cinema.make_reservation(screening_id, seat_id)
                break

        elif choice == "6":

             print("Exiting the program...")
             break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main_menu()