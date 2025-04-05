number = 20
prime_numbers = {num for num in range(2, number + 1) if sum(1 for div in range(2, num) if num % div == 0) < 2}
print(prime_numbers)
