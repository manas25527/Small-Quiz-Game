import random

ques = ["Q. Which country has the highest life expectancy?","Q. Who was the first person to land on the moon?","Q. What is the hardest natural substance on Earth?","Q. What book holds the title of the best-selling book of all time, according to Guinness World Records?","Q. In a website browser address bar, what does “www” stand for?"]
ans1 = ["A. Monaco","B. San Marino","C. South Korea","D. Hong Kong"]
ans2 = ["A. Yuri Gagarin","B. Valentina Tereshkova","C. Buzz Aldrin","D. Neil Armstrong"]
ans3 = ["A. Quartz","B. Diamond","C. Gypsum","D. Apatite"]
ans4 = ["A. Harry Potter","B. Book of Mormon","C. Christian Bible","D. Bhagvad Gita"]
ans5 = ["A. World Wide Web","B. Wide World Web","C. World Web Wide","D. Web Wide World"]
allans = [ans1,ans2,ans3,ans4,ans5]

#Printing random from the list define above.
money = 0
strt = input("Do you want to start the game or not? Y/N: ") #strt = Start
i = 0
while (i<= 4):
    if strt == "Y" or strt == "y" or strt == "YES" or strt == "yes" :
        dplq1 = random.choice(ques)  #dplq = Display Question
        print(dplq1)

        if dplq1 == ques[0]:
            for i in range (0,4):
                print(ans1[i])
            ansipt = input("Enter your Answer: ")
            if ansipt == "A" or ansipt == "a":
                print("Correct Answer")
                money += 1000
            elif ansipt == "B" or ansipt == "C" or ansipt == "D" or ansipt == "b" or ansipt == "c" or ansipt == "d":
                print("Wrong Answer")
            else:
                print("Invalid Input")

        elif dplq1 == ques[1]:
            for i in range (0,4):
                print(ans2[i])
            ansipt = input("Enter your Answer: ")
            if ansipt == "D" or ansipt == "d":
                print("Correct Answer")
                money += 1000
            elif ansipt == "B" or ansipt == "C" or ansipt == "A" or ansipt == "b" or ansipt == "c" or ansipt == "a":
                print("Wrong Answer")
            else:
                print("Invalid Input")

        elif dplq1 == ques[2]:
            for i in range (0,4):
                print(ans3[i])
            ansipt = input("Enter your Answer: ")
            if ansipt == "B" or ansipt == "b":
                print("Correct Answer")
                money += 1000
            elif ansipt == "A" or ansipt == "C" or ansipt == "D" or ansipt == "a" or ansipt == "c" or ansipt == "d":
                print("Wrong Answer")
            else:
                print("Invalid Input")

        elif dplq1 == ques[3]:
            for i in range (0,4):
                print(ans4[i])
            ansipt = input("Enter your Answer: ")
            if ansipt == "C" or ansipt == "c":
                print("Correct Answer")
                money += 1000
            elif ansipt == "B" or ansipt == "A" or ansipt == "D" or ansipt == "b" or ansipt == "a" or ansipt == "d":
                print("Wrong Answer")
            else:
                print("Invalid Input")

        elif dplq1 == ques[4]:
            for i in range (0,4):
                print(ans5[i])
            ansipt = input("Enter your Answer: ")
            if ansipt == "A" or ansipt == "a":
                print("Correct Answer")
                money += 1000
            elif ansipt == "B" or ansipt == "C" or ansipt == "D" or ansipt == "b" or ansipt == "c" or ansipt == "d":
                print("Wrong Answer")
            else:
                print("Invalid Input")

        print(f"You earned: Rs.{money}")
        ques.remove(dplq1) #Once the question is printed it will not print that question again

    elif strt == "N" or strt == "n" or strt == "NO" or strt == "no":
        print("Get ready and then come you fool..!!")
        break
    else:
        print("Invalid Input")
        break
    # print(ques)
    i += 1
    if(len(ques) > 0):
        strt = input("Do you want to continue the game or not? Y/N: ")
    else:
        print("Amount Won", money)
        break
