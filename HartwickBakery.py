# Evan Johanns
# 10/14/19
# Hartwick Bakery

cookies = []
candy = []

def cookie_input():

    for i in range(0,6):
      input(f"Please enter the cookie sales for month {i} :")
      cookies.append(i)
      return

cookie_input()
for y in cookies:
    avgcookies = avgcookies + y




candy = []
for x in range(0,6):
    input(f"Please enter the candy sales for month {x}")
    candy.append(x)

