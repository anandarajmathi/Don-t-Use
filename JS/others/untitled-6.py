def duplicate_n_maker(n):   ### this function creates a function
  return lambda a, b, c:f(a) + o(b) - o(c)

dup3 = duplicate_n_maker(3) # dup3() is a new function
        # dup_str is 'gogogo'
print dup3(5)
print dup3(4)
