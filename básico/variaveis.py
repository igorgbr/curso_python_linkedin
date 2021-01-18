f = 0
print(f)

f = "abc"
print(f)

print("isto é uma string " + str(123))

# - global x local


def alguma_funcao():
    global f
    f = "def"
    print(f)


alguma_funcao()
print(f)
