# Task 5 FIFA World Cup
# With 9 FIFA World Cup wins between them, Brazil and Italy two of
# the most successful soccer countries in the world. Write a program
# that works out who won their latest soccer match, given the scores
# of both teams.

def main():
    #Write your code here
   italy_score = input('Italy: ')
   Brazil_socre = input('Brazil: ')
   if italy_score < Brazil_socre:
     print ('Brazil won the match.')
   elif Brazil_socre > italy_score:
     print ('Italy won the match.')
   elif Brazil_socre == italy_score:
     print ('The match was a draw')
   else:
     print()



    # End of your code here





if __name__ == '__main__':
    main()