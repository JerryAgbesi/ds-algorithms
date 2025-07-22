from typing import List


def citadelGetMinOperations(executionTime: List[int], x: int, y: int) -> int:

      executionTime.sort()

      operations = 0

      while executionTime:
        executionTime[-1] -= x
        for i in range(len(executionTime) - 1):
            executionTime[i] -= y

            

        for i in range(len(executionTime)-1,-1,-1):
            if executionTime[i] < 1:
                del executionTime[i]

        operations += 1

      return operations

print(citadelGetMinOperations(executionTime = [3, 4, 1, 7, 6], x = 4, y = 2))