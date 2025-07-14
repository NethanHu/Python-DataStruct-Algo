from timeit import Timer

t1 = Timer("test1()", "from ListInit import test1")
print("concat %f seconds \n" % t1.timeit(number=1000))

t2 = Timer("test2()", "from ListInit import test2")
print("append %f seconds \n" % t2.timeit(number=1000))

t3 = Timer("test3()", "from ListInit import test3")
print("comprehension %f seconds \n" % t3.timeit(number=1000))

t4 = Timer("test4()", "from ListInit import test4")
print("cast list %f seconds \n" % t4.timeit(number=1000))

pop_zero = Timer("x.pop(0)", "from ListPop import x")
print("pop mid %f seconds \n" % pop_zero.timeit(number=1000))

pop_end = Timer("x.pop()", "from ListPop import x")
print("pop end %f seconds \n" % pop_end.timeit(number=1000))