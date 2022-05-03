#exercize 1

for n in range(20):
    print(n**3)
    if n**3 == 1000:
        break



#exercize 2


for n in range(1, 101):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)
   

   #exercize 3

age = int(input("type in your age here"))

if age < 18:
    print('kids')
elif age > 17 and age <65:
    print('adults')
else:
    print('seniors')