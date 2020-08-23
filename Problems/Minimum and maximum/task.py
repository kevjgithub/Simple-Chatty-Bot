first_number = int(input())
second_number = int(input())
print(first_number if max(first_number, second_number) == first_number else second_number)
print(first_number if min(first_number, second_number) == first_number else second_number)
