import Class
import features.Recipe as Recipe

p = Class.Player()

c = "Ruby"

p.inventory[c] = 1

print(p.inventory)

r = Recipe.recipes()["Black Razor"]

l = filter(lambda a: not a.startswith('__'), dir(r))
for i in l:
    print(i)

if ("Ruby", 1) in p.inventory.items():
    print("yo")

for i in range(0, 6):
    print(i)
