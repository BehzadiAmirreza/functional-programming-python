def create_counter(start=0):
    count = start
    def counter(): 
        nonlocal count 
        count += 1     
        return count
    return counter

counter1 = create_counter()
print(counter1())  # Outputs: 1
print(counter1())  # Outputs: 2
print("******************************")

counter2 = create_counter()
print(counter2())  # Outputs: 1
print(counter2())  # Outputs: 3
print(counter2())  # Outputs: 2
print("******************************")

counter3 = create_counter(3)
print(counter3())  # Outputs: 4
print(counter3())  # Outputs: 5
print("******************************")