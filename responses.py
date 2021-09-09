
# Topic 1: About Lecretia
# How does Lucretia work?
response_1_1 = """
I use advanced technology to answer questions and help you complete every banking tasks.
I can also offer personalized insights to help you manage cash flow and stay on top of your finances.
"""
# Is Lucretia safe and secure?
response_1_2 = """
I have the same industry-leading privacy and security features as the mobile app and Online Banking.
Be aware of your surroundings since other around you may be able to hear. Voice conversation are recorded and saved.
"""
# Give feedback about Lucretia
response_1_3 = """
You can tell me what you think about our interactions anytime by tapping on Feedback below.
Or, you can give general mobile app feedback by openning the app's Menu settings and tapping Share Your Feedback.
"""
blank_spot = "bank"
response_1 = [response_1_1, response_1_2, response_1_3]



#-------------------------#
## TOPIC 2: INSIGHT
# Show my insights 
response_2_1 = "I will show your insights"
    # show Balance Watch
    # show Spend Path

# Change my Lucretia insight settings
response_2_2 = "I'll take you to that screen to change insight setting now."
    #pop-up another screen show setting up Lucretia notification

# Learn about Lucretia insight
response_2_3 = """
I use advanced technology to provide important information about your accounts. Here's a little bit about Lucretia insights.
Lucretia Insights:
    Balance Watch:
      - I'll let you know if it look like your balance is trending toward a zero balance with the next 7 days
      
    Bill Reminder:
      - I'll help you schedule payments for eBils that are due within the next 5 days

    Duplicate Charge:
      - I'll give you a heads up when I see more than one charge for the same date and amount.

    Spend Path:
      - I'll provide weekly updates about your month-to-date and typical spending patterns to help you keep an eye on your budget.

    Recurring Charges:
      - I'll monitor your subscriptions, memberships and recurring charges to keep you updated on where your money is going. I'll also let you know if any of these carges increase unexpectedly

    Card Update Assistance:
      - If you move or get a new card. I'll share which merchants have your account on file so you can update your payment info.
    
    Posted Merchant Refunds:
      - I'll let you know when a credit or debit card refund posts to your accout.

    Credit Score Tracker:
      - I'll help you enroll to receive your Credit score and alert you if there's an important change to your credit score or rating
    
    Preferred Rewards:
      - I'll keep you posted on oppurtunities to earn more benefits and rewards from Preferred Rewards.

"""
## Balance Watch
# Respond to "Forecast my balance" 
response_2_3_1 =  """
Here's what I'm seeing for forecast your balance. Tap an account to see your 7-Day Balance Estimate
Keep in mind, since your estimate is based on typical spending and deposits, your actual balance may vary.
"""
    # Showing the balance of debit account. | Ex: Adv Plus Banking - 6360: $94.79

## Bill Reminder
# Respond to "Show my bill reminders" 
  # Scenario 1: No bills
response_2_3_2_1 = "Currently, you don't have any bills due within the next 30 days."
    
  # Scenario 2: Have bills
response_2_3_2_2 = "Your bills due within the next 30 days are:"

## Duplicate Charge
# Respond to "Do I have any duplicate charges" 
  # Scenario 1: No duplicate charge
response_2_3_3_1 = "I don't see any duplicate charges matching your search."  
  # Scenario 2: have duplicate charge
response_2_3_3_2 = "Your have {} duplicate charges."

## Spend Path
# Respond to "How's my spending?"
response_2_3_4 = """
Since it is the first of the month, I can only show you last month's spending
You spent $ last month.
"""
  # Note: sum the spending of last month

## Recurring Charges
# Respond to "Show my recurring charges"
response_2_3_5 = "What kind of recurring payment would you like to view?\n[a] Automatic payment or transfer \n[b] Recurring charge or subscription"


## Card Update Assistance
# Respond to "Which companies have my card on file?"
  # Scenario 1: No companies saved your card info
response_2_3_6_1 = "You don't save your card information with any merchants."  
  # Scenario 2: have companies saved your card info
response_2_3_6_2 = "You may have saved your card information at the following merchants."

## Posted Merchant Refunds
# Respond to "Do I have any refund?"
  # Scenario 1: No refund
response_2_3_7_1 = "I don't see any merchant refunds or return matching your search."  
  # Scenario 2: have companies saved your card info
response_2_3_7_2 = "You have {} refunds by the following merchants."

## Credit Score Tracker
# Respond to

## Preferred Rewards
# Respond to

response_2 = [response_2_1, response_2_2, response_2_3, response_2_3_1, response_2_3_2_1, response_2_3_2_2, response_2_3_3_1, response_2_3_3_2, response_2_3_3_1, response_2_3_3_2, response_2_3_4, response_2_3_5, response_2_3_6_1, response_2_3_6_2, response_2_3_7_1, response_2_3_7_2]

#-------------------------#
## TOPIC 3: FIND TRANSACTION
# 1. I want to see all my account activity
response_3_1 = "OK. Here's what I found."
    # Show the account activity from this year

# 2. Did I make payments from my credit card?
  # Scenario 1: No credit card
response_3_2_1 = "It doesn't look like you have an account for that."
  # Scenario 2: Have credit card
    # No payment:
response_3_2_2_1 = "I don't see any payment in your credit card."
    # Pay already
response_3_2_2_2 = "You have paid {} to your credit card."

# 3. I have a question about a deposit
  # Scenario 1: No deposit
response_3_3_1 = "I don't see any deposits matching your search."
  # Scenario 2: Have deposit
response_3_3_2 = "You have {} deposits."

# 4. Check te status of a purchase
response_3_4 = "Here's what I found."
    # Show the last purchase

# 5. Do I have any recent refunds
  # Scenario 1: No refund
response_3_5_1 = "I don't see any merchant refunds or return matching your search."  
  # Scenario 2: have companies saved your card info
response_3_5_2 = "You have {} refunds by the following merchants."

# 6. Did I have any grocery purchases over $100
  # Scenario 1: No grocery purchases over $100
response_3_6_1 = "I don't see any transactions matching your search."  
  # Scenario 2: have grocery purchases over $100
response_3_6_2 = "You have {} transactions which are grocery purchases over $100."

# 7. Can I see transaction activity for cable/satellite?
  # Scenario 1: No transaction activity for cable/satellite
response_3_7_1 = "I don't see any transactions activity for cable/satellite matching your search."  
  # Scenario 2: Have transaction activity for cable/satellite
response_3_7_2 = "You have {} transactions activity for cable/satellite."

# 8. What can I search for?
response_3_8 = """
Sure. I've listed some ways I can help you find specific transactions.
[1] Category Transaction
[2] Find Deposits
[3] Search by Amount
[4] Payment & Transfer History
[5] Date Search
[6] Search Your Check
[7] Merchant Purchase
[8] Account Activity
"""

# 9. Dispute a charge
response_3_9 = "Tap a transaction to get more details, including how to report a problem."
    # Show some last purchases

#-------------------------#
## TOPIC 4: FIND TRANSACTION
# 1. Forecast my balance
response_4_1 = """
Here's what I'm seeing for the week ahead. Tap an account to see your 7-Day Balance Estimate.
Keep in mind, since your estimate is based on typical spending and deposits, your actual balance may vary.
"""
    # Show account balance in in the next 7 Day Estimate 
  
# 2. What's my routing number?
response_4_2 = "Here are your routing numbers."
    # Show routing number

# 3. Order bills and coins
response_4_3 = "To get coins and bills, you'll need to place an order at a financial center."
  # Sub-response: Find a financial center
response_4_3_1 = "Let me pull that up for you."
    # Open a financial canter page

# 4. Order foreign currency
response_4_4 = """
I can take you to order foreign currency. Most orders are completed within 1 to 3 business days.
We can let you know when it's ready for pickup at your nearby financial center, and orders up to $1000 can be shipped to you.
"""
  # Sub-response: "Get started in the app"
response_4_4_1 = "I'll take you to that screen now."
    # Open a ordering foreign currency page

# 5. Open an account
response_4_5 = "I can take you to compare choices and apply for a new account."
  # Sub-response: "Get started"
response_4_5_1 = "I'll take you to that screen now."
    # Open comparing account page

# 6. What's my balance?
  # Scenario 1: Positive amount
response_4_6_1 = """
Your balance is ${}.
Tap an account and I'll take you to view more details.
"""
  # Scenario 2: Negative amount
response_4_6_2 = """
It look like your account is overdrawn by ${}.
Tap an account and I'll take you to view more details.
"""

# 7. Show my account numbers
response_4_7_1 = "No problem. Here's your account number {}."
response_4_7_2 = "Sure. Here's your account number {}."


#-------------------------#
## TOPIC 5: BILL PAY
# 1. Show me my bills
  # Scenario 1: No bills
response_5_1_1 = "Currently, you don't have any bills due within the next 30 days."
  # Scenario 2: Have bills
response_5_1_2 = "You have {} bills by the following merchants."

# 2. Make a payment
response_5_2 = """
Ok. Here's a list of bills and people you have set up to pay.
Please select the one you'd like. You can also add a new Pay To account or transfer recipient at the bottom of the list.
"""

# 3. Pay a bill
    # Check again later

# 4. Cancel a bill payment
  # Scenario 1: No bill
response_5_4_1 = """
I don't see any scheduled payments in the next 30 days.
But I can take you to see other types of transactions.
[1] View processing transaction
[2] View Zelle activity
[3] View recurring charges
[4] View past transactions
"""
  # Scenario 2: Have bill
response_5_4_2 = """
You have {} bills by the following merchants.
Which one you would like to cancel?
"""
    # Pop-up a list

# 5. What bills did I pay this month?
  # Scenario 1: No bill
response_5_5_1 = "I didn't find any transactions matching your search."
  # Scenario 2: Have bills
response_5_5_2 = "You have paid {} bills this month."

# 6. Show my scheduled payment
response_5_6_1 = """
I don't see any scheduled payments in the next 30 days.
But I can take you to see other types of transactions.
[1] View processing transaction
[2] View Zelle activity
[3] View recurring charges
[4] View past transactions
"""
  # Scenario 2: Have bill
response_5_6_2 = """
You have {} scheduled payment by the following merchants.
"""

# 7. Add a new bill to pay
response_5_7 = "Let's see. Let's go to the screen where you can do that, and then we'll pick up where we left off."