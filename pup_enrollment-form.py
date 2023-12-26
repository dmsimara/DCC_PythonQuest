name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gwa = float(input("Enter your previous general weighted averag: "))
member = bool(input("Are you a member of AWS Cloud Club? (yes/no): "))

print("\nPUP Enrollment Form\nName: %s\nAge: %d\nGWA: %.2lf\nAwstaunot: %s" % (name, age, gwa, member))