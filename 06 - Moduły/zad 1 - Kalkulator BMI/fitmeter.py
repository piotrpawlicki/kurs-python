import bmi

def main():
    weight  = float(input("Podaj wage w kilogramach: "))
    height = float(input("Podaj wzrost w centymatrach: "))
    print("Twoje podpowiedzi: ", bmi.calculate_bmi(weight, height))

main()