# def get_fib(position):
#     if position == 0 or position == 1:
#         return position
#     return get_fib(position - 1) + get_fib(position - 2)
#
#
# print(get_fib(5))
def climbStairs(self, n: int) -> int:

    way = {1: 1, 2: 2, 3: 3}

    for x in range(4, n + 2):
        
           way[x] = way[x - 1] + way[x - 2]

    return way[n]
