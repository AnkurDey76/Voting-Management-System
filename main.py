Nominee1 = input("Enter the name of first nominee: ")
Nominee2 = input("Enter the name of second nominee: ")

nm1_votes=0
nm2_votes=0

voter_id=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no_of_voter=len(voter_id)


while True:
    if voter_id==[]:
        print("Voter session is over!")
        if nm1_votes>nm2_votes:
            percentage=(nm1_votes/no_of_voter)*100
            print(Nominee1 ,"has won the vote with", percentage, "% majority")
            break

        elif nm2_votes>nm1_votes:
            percentage=(nm2_votes/no_of_voter)*100
            print(Nominee2 ,"has won the vote with", percentage, "% majority")
            break

        elif nm1_votes==nm2_votes:
            print(Nominee1 ,"& ",Nominee2 ,"got equal vote...\n so the government will decide will rule")
            break


  
    voter=int(input("Enter your voter id: "))
    if voter in voter_id:
        print("You are a voter! ")
        voter_id.remove(voter)
        print("--------------------------------------")
        print("To give vote to ", Nominee1, "'press 1'")
        print("To give vote to ", Nominee2, "'press 2'")
        print("--------------------------------------")
        
        vote=int(input("Enter your precious vote: "))
        if vote==1:
            nm1_votes+=1
            print("Thank you! for casting your important vote")
        elif vote==2:
            nm2_votes+=1
            print("Thank you! for casting your important vote")
        elif vote>2:
            print("Check your pressed key")


    else:
        print("Unfortunately: You are not a voter anymore or  You've already given your vote!")


