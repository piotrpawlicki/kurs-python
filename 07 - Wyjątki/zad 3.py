my_list = ["a", "word", 5, 18, 0, 1.15, "XX", 5.55]

user_index = int(input("podaj indeks: "))
try:
    result = 1 / my_list[user_index]
    print(result)

except ValueError:
    print("value error")

except ZeroDivisionError:
    print("zero division error")

except IndexError:
    print("index error")

except Exception as e:
    print("mistake:", str(e))