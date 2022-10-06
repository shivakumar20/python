#State the problem clearly. Identify the input & output formats.
#Come up with some example inputs & outputs. Try to cover all edge cases.
#Come up with a correct solution for the problem. State it in plain English.
#Implement the solution and test it using example inputs. Fix bugs, if any.
#Analyze the algorithm's complexity and identify inefficiencies, if any.
#Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

#Tips:

#Name your function appropriately and think carefully about the signature
#Discuss the problem with the interviewer if you are unsure how to frame it in abstract terms
#Use descriptive variable names, otherwise you may forget what a variable represents

# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
# and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a 
# given number by turning over as few cards as possible. Write a function to help Bob locate the card.


def binary_search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <=high:

        mid = (high + low)//2  #Avoid getting float values

        print(f'lo: {low}, high : {high}, mid: {mid}, Number reqired: {x}')

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1




#-----------------------------------Special Case scenario---------------------------------------

#Input:
#{'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}

#Expected Output:
#2

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print(f'mid: {mid}, mid_number: {mid_number}')

    if mid_number == query:

        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        
        else:
            return 'found'

    elif mid_number < query:
        return 'left'

    else:
        return 'right'


def locate_card(cards, query):
    lo , hi = 0 , len(cards) - 1

    while lo <= hi:

        print(f'lo: {lo}, hi: {hi}')

        mid = (lo + hi) // 2
        
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
            
        elif result == 'left':
            hi = mid - 1
            
        elif result == 'right':
            lo = mid + 1

    return -1

cards = [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0]

query = 6

ans = locate_card(cards, query)

print(f'answer: {cards[ans]}' )