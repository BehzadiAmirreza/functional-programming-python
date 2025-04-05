class PrimeNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 2
    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.max_num:
            num = self.current
            self.current += 1
            
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                return num
        
        raise StopIteration

prime_nums = PrimeNumbers(50)
for num in prime_nums:
    print(num, end=', ')
