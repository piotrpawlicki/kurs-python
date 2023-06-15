from student import Student

anna = Student("na", "Kowalska", 23, 4.5)
jan = Student("Jan", "Nowak", 22, 4.0)

print(anna.email)
anna.name = 'Anna'
print(anna.fullname)


anna.fullname = "Wisniewska Anna"
print(anna)