from typing import List


def triplets(t: int, d: List[int]) -> int:
    # sorting the array will help in making sure the array is ascending
    
    d.sort()
    count = 0

    for i in range(len(d) - 2):
        

        l = i+1
        r = len(d) - 1

        while l < r:
            
            sum = d[i] + d[l] + d[r]

            print(f" {d[i]} + {d[l]} + {d[r]} = {sum}")

            if sum <= t:
                count += r-l
                l += 1
            else:
                r-=1

    return count


print(triplets( t = 8, d = [1, 2, 3, 4, 6]))