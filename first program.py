print("Hello Python 101")

#use to comment 

#Phyton Types
# 11 = int
# 21.213 = float
# "Hello Word" = str
# True or False = bool

print(type(11)) #return type

#convert types
number = 1.0
print(type(number))
number = int(number)
print(type(number))

#expressions: mathematical operations
print(10 + 5 + 3 + 4)
print(90 - 30)
print(3 * 5)
print(10 / 2)
print(10 % 3)

#with variables
x = 100 + 5 + 3 + 4 + 8
print(x)
y = 2 * 30
print(y)
print(x / y)

#access index in strings
name = "Marcella Lara"
print(name[0])
print(name[4])
print(name[-4])
print(name[0:8])

#return total
print(len(name))

#str + str
complete_name = name + " Esteves"
print(complete_name)

#str * a number
print(name * 3)

#new line
print("Marcella Lara \n Esteves")

#escape sequences
print("Marcella Lara \t Esteves")

#method upper case
a = "marcella lara"
print(a.upper())

#method replace
print(a.replace("lara", "esteves"))

#lists and tuples (tuples are immutable, lists are mutable)
tuple_1 = ("Marcella", 1.2, 50, True)
print(type(tuple_1))
print(tuple_1[1])

list_1 = ["Marcella", 19, 1.9, False]
print(type(list_1))
print(list_1[3])

#tuples nesting
tuple_nt = (("Marcella", "Joana"), (1, 6, 7), (1.2, 1.5), ("jogos", "brinquedos"))
print(tuple_nt[3])
print(tuple_nt[3][0])

#concatenate lists
list_1.extend(["pop", 10])
print(list_1)

#convert string to list
sp = "A, B, C, D"
print(sp.split())

#set (no duplicate elements)
set_1 = {"pop", "rock", "jazz", "rock"}
print(set_1)

#dictionaries (the argument is the key and return the value)
dic_1 = {"Thriller": 1982, "Back in Black": 1980, "The Dark Side of The Moon": 1973, "The Bodyguard": 1992}
print(dic_1["Back in Black"])
print("Back" in dic_1)
print(dic_1.values())