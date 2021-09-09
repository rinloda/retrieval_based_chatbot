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