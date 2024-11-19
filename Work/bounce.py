# bounce.py
#
# Exercise 1.5
#
# My code

bounce_number = 1

height_initial = 100

height_final = (3/5) * height_initial #initial height of ball

while bounce_number < 10:
    print(bounce_number, round(height_final,4))
    bounce_number = bounce_number + 1
    height_final = (3/5) * height_final
    
print(bounce_number, round(height_final,4))

# # bounce.py

# height = 100
# bounce = 1
# while bounce <= 10:
    # height = height * (3/5)
    # print(bounce, round(height, 4))
    # bounce += 1
