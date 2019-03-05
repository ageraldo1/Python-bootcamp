import timeit

my_str = "-".join(str(n) for n in range(100))
print (my_str)

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
