import bmi

def user_input(message, type):
    while True:
        try:
            user_input = type(input(message))
            return user_input
        except ValueError:
            print("Podano złe dane!")
def main():
    weight  = user_input("Podaj wage w kilogramach: ", int)
    height = user_input("Podaj wzrost w centymatrach: ", int)
    print("Twoje podpowiedzi: ", bmi.calculate_bmi(weight, height))

main()