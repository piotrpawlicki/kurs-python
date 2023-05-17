data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]


def show_days(name, days):
    print(name)
    for day in days:
        if day < 10:
            day = f'0{day}'
        if (int(day)+1) % 7 == 0:
            print(day)
        else:
            print(day, end= " ")

'''
def show_days(month,days):
    print(month)
    for i in range(0, len(days),7):
        week = days[i : i+7]
        for day in week:
            if day <10:
            print(f'0{day}', end=' ')
        print()
'''
for month_name, month_days in data:
    show_days(month_name, month_days)
    print()
'''    
month_details = data[0]
print(month_details[0])
'''