# f = open("jokerz_jokes.txt", "r")
# file = []
# for line in f:
# 	joke = []
# 	print(joke)
# 	if (line == "===\n"):
# 		file.append(joke)
# 		joke = []
# 	else:
# 		joke.append(line)
# print(file)

f = open('jokerz_jokes.txt', 'r')
x = f.readlines()
f.close()

for i, line in enumerate(x):
	if line == "===\n":
		x.remove(line)

result = []
counter = 0
for line in x:
	if counter <= 1:
		result.append(line)
		counter += 1
	else:
		counter = 0
		result.append("===\n")

f = open("processed_jokerz.txt", "w")
for joke in result:
	f.write(joke)