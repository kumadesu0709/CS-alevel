sounds = {"cat":"meow", "dog":"woof"}
print(sounds)
print(sounds["dog"])
print(sounds["cat"])

sounds["cat"] = "purr"
print(sounds["cat"])
print(sounds)

sounds["cow"] = 'moo'
print(sounds["cow"])

print(sounds.get("donkey"))
print(sounds.get("donkey", "huh?"))
print(sounds)

zoo_counting = {'lions' : 2, "tigers":1}

print(f'We have {zoo_counting["lions"]} lions')#uses "'" and """" because doesn't want to confuse python
print("\nIn this zoo:")
for animal in zoo_counting:#only loops over the key (i.e. in this case the animal in the dictionary
    print(f"we have {zoo_counting[animal]} {animal}")
if "bears" in zoo_counting:
    print("\nwe have bears")
else:
    print("\nWe don't have bear")

zoo_counting["lions"] = zoo_counting['lions'] + 1
print(f'\nWe have {zoo_counting["lions"]} lions')