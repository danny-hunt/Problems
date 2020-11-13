
A_base = 20000
B_base = 19000

def fifteen_years_of_a(A_base):
    sum = 0
    salary = A_base
    for _ in range(30):
        sum += 0.5*salary
        salary += 200
    return salary

print(fifteen_years_of_a(A_base))

def fifteen_years_of_b(B_base):
    sum = 0
    salary = B_base
    for _ in range(15):
        sum += salary
        salary *= 1.035
    return salary

print(fifteen_years_of_b(B_base))

