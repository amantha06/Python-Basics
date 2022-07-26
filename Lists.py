friends = ["Anirudh", "Parth", "Krish", "BigNose"]
print(friends[2:3])
friends[1] = "DOSA"
print(friends[1])

numbers = [2, 7, 9, 8, 13, 10]

friends.extend(numbers)
friends.append("Lingapparao")
friends.insert(1, "Ani")
friends.remove("Ani")
friends.clear()

print(friends)
