In this assignment you will create the pricing module for Fuel Quote Form and put together the complete project that you have built so far.

Description:
Same as assignment 1.

Additional Details:

Create a pricing module that should calculate the price per gallon based on this formula.

Suggested Price = Current Price + Margin

Where,

Current price per gallon = $1.50 (this is the price what distributor gets from refinery and it varies based upon crude price. But we are keeping it constant for simplicity)
Margin =  Current Price * (Location Factor - Rate History Factor + Gallons Requested Factor + Company Profit Factor)

Consider these factors:
Location Factor = 2% for Texas, 4% for out of state.
Rate History Factor = 1% if client requested fuel before, 0% if no history (you can query fuel quote table to check if there are any rows for the client)
Gallons Requested Factor = 2% if more than 1000 Gallons, 3% if less
Company Profit Factor = 10% always

Example:
1500 gallons requested, in state, does have history (i.e. quote history data exist in DB for this client)

Margin => (.02 - .01 + .02 + .1) * 1.50 = .195
Suggested Price/gallon => 1.50 + .195 = $1.695
Total Amount Due => 1500 * 1.695 = $2542.50

Additional Validations:
• Make suggested price and total amount fields in your Quote form read-only, i.e. user cannot enter these values.
• Create another button on Quote Form before Submit, call it "Get Quote".
• After user enters all other fields in the form other than Suggested Price and Total Amount, allow user to click on "Get Quote", i.e. Get Quote and Submit Quote buttons should be disabled if there are no values entered in the form. 
• When user clicks on "Get Quote" button make a call to Pricing Module and populate the suggested price and total. 
• Display Suggested Price and Total Amount once you get the values from pricing module. 
• Make sure you do not lose any form values when you make a call to Pricing module.
• You can use AJAX call to achieve this i.e.  partial form submission. 
• Then user clicks on Submit Quote and you save the quote.

Deliverables:

1. Provide link to GitHub repository for TAs to view the code. (5 points)
2. Rerun the code coverage report. Code coverage must be above 80%. (2 points)
3. Demo prior to project due date. (3 points)
4. IMPORTANT: list who did what within the group. TAs should be able to validate in GitHub, otherwise team members who didn't contribute will receive a ZERO.


IMPORTANT:  
All group members must be present for demo. TAs will validate who did what.

What to turn in: 
- Only soft copy uploaded to BlackBoard before due date. 
- DO NOT SUBMIT CODE to BlackBoard. 
- Only one submission per group.
- No extensions.
- All group members must contribute equally.
