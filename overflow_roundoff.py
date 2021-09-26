import sys

# In Python 3, integers do not have a limit
# However, floating point numbers do.

# Maximum safe float in Python
print(sys.float_info.max)

# When we add to it, it stays the same
print(sys.float_info.max + 1)
print(sys.float_info.max + 2)

# Roundoff
result = 0.1 + 0.1 + 0.1
print(result)
