# Task 7 Count down
# You've developed a healthy interest in space exploration and want
# to get ready for your own rocket launch, starting with the launch
# count-down sequence. You're not sure how long your engines will
# take to flare up (you haven't built the rocket yet!) so you decide to
# write a program that can read in the number to count down from!

def main():
    #Write your code here
    time_to_launch = int(input("Time to launch: "))
    print("Counting down ...")

    for i in range(time_to_launch, 0, -1):
     print(i, "...")
    print("Blast Off!")

    
    # End of your code here





if __name__ == '__main__':
    main()