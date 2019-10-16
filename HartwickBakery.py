# Evan Johanns
# 10/14/19
# Hartwick Bakery


months = int(input("please enter the number of months the bakery was open: "))
candy_sold = []
cookies_sold = []


def lists():
    # total = 0

    for i in range(0, months):
      cookies = input(f"Please enter the number of cookies sold for month {i + 1}: ")
      cookies_sold.append(cookies)

    for x in range(0, months):
     candy = input(f"please enter the number of candy sold for each month {x + 1}: ")
     candy_sold.append(candy)
     # total = total + int(candy)


lists()


def average():
    total_cookie = 0
    for cookies in cookies_sold:
        total_cookie = int(total_cookie) + int(cookies)
    cookie_avg = int(total_cookie) / int(months)

    total_candy = 0
    for candy in candy_sold:
        total_candy = int(total_candy) + int(candy)

    candy_avg = int(total_candy) / int(months)

    print(f"the average of cookies sold is {cookie_avg} per month.")
    print(f"the average for candy sold is {candy_avg} per month.")

average()


def minimum():
    cookies_sold.sort()
    candy_sold.sort()
    print(f"The minimum cookies sold was {cookies_sold[0]}")
    print(f"The minimum candy sold was {candy_sold[0]}")


minimum()


def maximum():
    sorted(cookies_sold)
    sorted(candy_sold)
    print(f"The maximum cookies sold was {cookies_sold[months - 1]}")
    print(f"The maximum candy sold was {candy_sold[months - 1]}")


maximum()


total_cookie = 0
total_candy = 0

for candy in candy_sold:
    total_candy = int(total_candy) + int(candy)     # accumulator for total candy

for cookies in cookies_sold:
    total_cookie = int(total_cookie) + int(cookies)     # accumulator for total cookies

if total_candy < total_cookie:
    print("Cookies was the most popular item sold!")
else:
    print("Candy was the most popular item sold")
