#Calculate the non-negotiables
sample_prices = [516, 450, 320, 330]
non_negotiables = sum(sample_prices)
print("This is the total sum that needs to be covered, regardless: {}".format(non_negotiables))

# Now, suppose we have the previous balance prior to the check amount
previous_balance = 330 #Suppose this is the starting point
remainder = non_negotiables - previous_balance
take_home_pay = 3300
print("From the previous period, we have {}".format(previous_balance))
print("Assuming we use this to cover the non-negotiables, we have {} left to cover".format(remainder))
print("*"*20)
print("BEGIN REPORTING")
print("*" * 20)
print("The take home pay: {}".format(take_home_pay))
print("After taking care of the non-negotiables, we have {}".format(take_home_pay -  remainder))

#Keep in mind that the 50-30-20% applies monthly - so we will have to half, assuming a bi-weekly pay
#For now, we will make a dictionary of the credit cards, where the keys are dummy names and the values are tuples
# A pair where the first is the amount in a given period and the second is the interest rate

credit_cards = {
    'cc_1': (50, 30.49),
    'cc_2': (2100, 27.24), 
    'cc_3': (800, 19.34), 
    'cc_4': (2500, 22.49),
    'cc_5': (5000, 19.25)
}

#Now, we will calculate the potential interest each card can yield
interests = [values[0] + (values[0] * ((values[1] / 100) / 365) * 30)  for values in credit_cards.values()]
print(interests)

#Now, we will have to get our take_home_pay and calculate how much we have left after we take care of the non-negotiables
# remaining_pay = take_home_pay - remainder
# print(remaining_pay)
# #Now the rule above states only 10%
# print(take_home_pay * 0.1)
# # We will have to see which one we can cover