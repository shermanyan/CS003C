"""
Sherman Yan
Assignment 10 - P9.10
"""


##
# creates a voting machine
#
class VotingMachine:

    def __init__(self):
        self._democrats = 0
        self._republicans = 0

    ##
    # add one to democrats
    #
    def voteDemocrats(self):
        self._democrats += 1

    ##
    # add one to republicans
    #
    def voteRepublicans(self):
        self._republicans += 1

    ##
    # set democrat votes to 0
    # set republican votes to 0
    #
    def clear(self):
        self._republicans = 0
        self._democrats = 0

    ##
    # returns democrat amount + republican amount
    # return@ democrats, republicans
    def getTallies(self):
        return self._democrats, self._republicans


def voting(voteMachine):

    try:
        votingChoice = int(input("Voting options.\n"
                                 "1 - Vote Democrats\n"
                                 "2 - Vote Republican\n"
                                 "3 - View tallies\n"
                                 "4 - Clear history\n"
                                 "5 - Exit\n"
                                 "Enter your option from above: "))
        if votingChoice == 1:
            voteMachine.voteDemocrats()
        elif votingChoice == 2:
            voteMachine.voteRepublicans()
        elif votingChoice == 3:
            demScore, repScore = voteMachine.getTallies()
            print("Democrats:", demScore, "Republicans:", repScore)
        elif votingChoice == 4:
            voteMachine.clear()
            print("Tallies cleared")
        elif votingChoice == 5:
            demScore, repScore = voteMachine.getTallies()
            print("Here are the results of the voting")
            print("Democrats:", demScore, "Republicans:", repScore)
            exit()
        else:
            raise ValueError("Invalid choice")
    except ValueError as valError:
        print("ERROR:", str(valError))
    return voting(voteMachine)


def main():
    print("- Voting booth -")
    voter = VotingMachine()
    voting(voter)


if __name__ == '__main__':
    main()


"""
Sample Run
- Voting booth -
Voting options.
1 - Vote Democrats
2 - Vote Republican
3 - View tallies
4 - Clear history
5 - Exit
Enter your option from above: 1
Voting options.
1 - Vote Democrats
2 - Vote Republican
3 - View tallies
4 - Clear history
5 - Exit
Enter your option from above: 1
Voting options.
1 - Vote Democrats
2 - Vote Republican
3 - View tallies
4 - Clear history
5 - Exit
Enter your option from above: 2
Voting options.
1 - Vote Democrats
2 - Vote Republican
3 - View tallies
4 - Clear history
5 - Exit
Enter your option from above: 2
Voting options.
1 - Vote Democrats
2 - Vote Republican
3 - View tallies
4 - Clear history
5 - Exit
Enter your option from above: 3
Democrats: 2 Republicans: 2
Voting options.
1 - Vote Democrats
2 - Vote Republican
3 - View tallies
4 - Clear history
5 - Exit
Enter your option from above: 4
Tallies cleared
Voting options.
1 - Vote Democrats
2 - Vote Republican
3 - View tallies
4 - Clear history
5 - Exit
Enter your option from above: 5
Here are the results of the voting
Democrats: 0 Republicans: 0
"""