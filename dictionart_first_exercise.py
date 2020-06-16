fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit",
    "apple": "An apple a day keeps the doctor away"
}

print(fruit)
print(fruit["lime"])  # Lime is a key from dictionary fruit
fruit["pearl"] = "an odd shaped apple"
print(fruit['pearl'])
fruit['pearl'] = "does'nt interest everyone"
print(fruit['pearl'])
# del(fruit['apple'])
# del command is more powerful
print(fruit)
# print(fruit['tomoto'])
# fruit.clear()
# print(fruit)

# while True:
#     dict_key = input("Pleae enter a fruit: ")
#     if dict_key == 'quit':
#         break
#     # description = fruit.get(dict_key, "We don't have a " + dict_key)
#     # print(description)
#     # OR the below code
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)

# for i in range(10):
#     for snack in fruit:
#         print(snack + ' is ' + fruit[snack])
#     print('---' * 25)

# ordered_keys = list(fruit.keys())
# print(ordered_keys)
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for i in ordered_keys:
#     print(i + ' - ' + fruit[i])

# print("-----" * 15)
# for i in sorted(fruit.keys()):
#     print(i + ' - ' + fruit[i])
#
# for f in fruit:
#     print(f + " : " + fruit[f])

for val in fruit.values():
    print(val)
print("-----" * 15)
for key in fruit:
    print(fruit[key])



