s = 'aba' #input("Enter string to be repeated: ")
n = 10 #int(input("Enter number of characters to be considered: "))

s_len = len(s)
cur_count = 0
res = 0

# aba aba aba a
x, y = divmod(n, len(s))
res = s[:y].count("a") * (x + 1) + s[y:].count("a") * x

print("res:" + str(res))
