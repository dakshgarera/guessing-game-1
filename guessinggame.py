num = 5
num_of_tries = 0

print("Welcome to number guessing game")

while True:
    try:
        lucky_num = int(input("pleasew enter your lucky number from 1 to 10:"))

        if lucky_num > 11 or lucky_num < 1:
            print("please entder number from 1 to 10")
            continue

            if lucky_num == num:
                print("yow won !!")
                break
            else:
                    print("Sorry its wrong number")
                    num_of_tries +=1

                    if num_of_tries == 3:
                        print("your 3 attempts exceeded")
                        print("better luck next time!!")
                        break

    except:
        print("pleasee enter number from 1 to 10")   
        continue     