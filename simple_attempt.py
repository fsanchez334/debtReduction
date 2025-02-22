#Calculate the non-negotiables
import datetime
import heapq
sample_prices = [516, 450, 320, 330]
non_negotiables = sum(sample_prices)
todays_date = datetime.datetime.now()

print(todays_date)
print("This is the total sum that needs to be covered, regardless: {}".format(non_negotiables))

# Now, suppose we have the previous balance prior to the check amount
previous_balance = 330 #Suppose this is the starting point
remainder = non_negotiables - previous_balance
take_home_pay = 3300
pay_remaining = take_home_pay -  remainder
hard_stop = pay_remaining - (take_home_pay * .5)
print("From the previous period, we have {}".format(previous_balance))
print("Assuming we use this to cover the non-negotiables, we have {} left to cover".format(remainder))
print("*"*20)
print("BEGIN REPORTING")
print("*" * 20)
print("The take home pay: {}".format(take_home_pay))
print("The breakdown of the 50-30-20 rule of the pay:")
print("50%: {}".format(take_home_pay * .5))
print("30%: {}".format(take_home_pay * .3))
print("20%: {}".format(take_home_pay * .2))
print("Post non-negotiables, we have {}".format(pay_remaining))
print("To be within 50% we have {} left to use".format(hard_stop))
#Keep in mind that the 50-30-20% applies monthly, we will assumea bi-weekly pay
#For now, we will make a dictionary of the credit cards, where the keys are dummy names and the values are tuples
# A pair where the first is the amount in a given period and the second is the interest rate
'''
   - Amount spent during the statement period
   - Interest Rate
   - Statement balance
   - Due Date
   - Credit Limit
'''
credit_cards = {
    'cc_1': (50, 30.49, 125, datetime.datetime(2025, 2, 11), 15000),
    'cc_2': (2100, 27.24, 2500, datetime.datetime(2025, 2, 11), 40000),
    'cc_3': (800, 19.34, 12900, datetime.datetime(2025, 2, 21), 15000), 
    'cc_4': (2500, 22.49, 5200, datetime.datetime(2025, 3, 1), 8000), 
    'cc_5': (5000, 19.25, 6500, datetime.datetime(2025, 2, 28), 12000)
}

#Now, we will calculate the potential interest each card can yield
interests = [[keys, (values[2] * ((values[1] / 100) / 365) * 30) + values[0], values[2] + (values[2] * ((values[1] / 100) / 365) * 30)] for keys, values in credit_cards.items()]

#We will have to prioritize which card to prioritize based on the due date, relative to today
#Now we need to access the dictionary and get the due date
for credit_tuple in interests:
    #Get the credit card
    print(credit_tuple)
    credit_ID = credit_tuple[0]
    #Get the date object 
    date_object = credit_cards[credit_ID][3]
    #Calculate the difference
    days = (date_object - todays_date).days
    credit_tuple.insert(0, days)

heapq.heapify(interests)
#The credit card with the upcoming due date will be the payment that should be prioritized
print("Here are the credit cards we are dealing with")
print("*" * 90)
print(interests)
print("*" * 90)
while len(interests) > 0: 
    #Now, we will have to substract it from the remaining
    card_information =  heapq.heappop(interests)
    #See whether we can pay the interest or the statement balance
    print(card_information)
    min_choice = min(card_information[-2:]) if card_information[-1] > hard_stop else card_information[-1]
    print("I will be paying {}".format(min_choice))
    if min_choice > hard_stop:
        break
    else:
        hard_stop -= min_choice
        #After we pay each card, we need to update the balance on that card
        
#In this case, there is leftover money - we can ask the user where to use this money
    
