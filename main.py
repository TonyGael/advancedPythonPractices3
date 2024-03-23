# secuencias

# def my_generator(n): #  lazy executions
#     for x in range(n):
#         yield x**3
#
#
# values = my_generator(20)

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

# for x in values:
#     print(x)

############################################################3

# import sys
#
# def my_generator_1(n):
#     for x in range(n):
#         yield x**3
#
#
# # values = my_generator_1(100)  # prints ou 104 bits
# values = my_generator_1(500000)  # prints ou 104 bits
#
# print(sys.getsizeof(values))

################################################################

def infinite_sequence():  # controled by yield
    result = 1
    while True:
        yield result
        result *= 5


values = infinite_sequence()

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

# for x in values:
#     print(x)  # houston there is a problem here!

for x in range(20):
    print(next(values))
