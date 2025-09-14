# Task 6 Find bear
# Write a program to work out whether a line of input text contains a
# bear or not. Your program needs to find cases where the word
# appears in full, with no breaks.

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