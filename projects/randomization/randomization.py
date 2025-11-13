import random
import moduleA


print(moduleA.myModule1FromModuleA)

print(moduleA.myModule2FromModuleA)

print()
print()
print()


# random.random() kullamımında  0.0 <= x < 1.0 aralığında bir float sayı döner

# random.uniform(a, b) kullamımında a <= x <= b aralığında bir float sayı döner

randomFloat1 = random.uniform(12, 22)
print("randomFloat1:", randomFloat1)




kuyruklar = random.randint(0, 1)

if kuyruklar % 2 == 0:
    print("Yazı")

else:
    print("Tura") 