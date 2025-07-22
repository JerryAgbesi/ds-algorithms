from typing import List


def lightsBulbs( states: List[int], numbers: List[int]) -> List[int]:
    # I need to first find the prime factors of the given number
    # Next you move through the states and flip the number for every multiple of each prime factor

    def get_prime_factors(num):
            i = 2
            factors = []

            while i**2 <= num:
                if num % i:
                    i += 1
                else:
                    num //= i
                    factors.append(i)
            
            if num > 1:
                factors.append(num)
            return list(set(factors))
    
    for number in numbers:
        prime_factors = []

        prime_factors.extend(get_prime_factors(number))

        print(prime_factors)

        for num in prime_factors:
             for i in range(len(states)):
                  if ((i + 1) % num == 0):
                       states[i] = 0 if states[i] == 1 else 1
             print(states)
    
    return states

print(lightsBulbs(states = [1, 1, 0, 0, 1, 1, 0, 1, 1, 1], numbers = [3, 4, 15]))

# result = [1 0 0 1 0 0 0 0 1 1] 



