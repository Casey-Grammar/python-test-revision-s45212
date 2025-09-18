# Task 9 Cat problem
# You've collected too many cats. Write a program to count how
# many cats you have by reading in their names. All your cats only
# have first names, with no spaces.

def main():
    #Write your code here
    cats = input('Cats: ')
    cat_list = cats.split()
    num_cats = len(cat_list)
    print(f"You have {str(num_cats)} cats.")
    



    # End of your code here





if __name__ == '__main__':
    main()