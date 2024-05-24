create_update_promo_request = """
[
	'code' => 'required|alpha_num',  
	'auto_apply' => 'boolean',  
	'type' => 'required|in:MONEY_DISCOUNT,PERC_DISCOUNT',  
	'description' => 'required|string',  
	'percentage' => 'required_if:type,PERC_DISCOUNT|pricing_float',  
	'currency' => 'required|string,  
	'amount' => 'required|pricing_float',  
	'start_date' => 'required|date',  
	'expiry_date' => 'nullable|date',  
	'num_booking_threshold' => 'integer|nullable',  
	'max_global_usage' => 'integer',  
	'max_usage' => 'integer',  
	'app_only' => 'boolean',  
	'user_id' => 'integer',  
	'listing_ids' => 'string',  
	'include_in_reporting' => 'required|boolean',  
	'shortened_url_id' => 'integer',  
	'display_name' => 'required|string',  
	'booking_type' => 'required|in:prebook,monthly,monthly_rolling,monthly_rolling_mon_fri',  
	'dynamic_expiry_days' => 'integer|nullable',  
	'applicable_platforms' => 'string',  
	'usage_months' => 'nullable|integer',
]
"""

full_prompt = """
You are an expert in creating promo codes for JustPark using a PHP Laravel API. JustPark is a global parking company. Someone will ask you
to make a promo code with specific parameters. Take their request and turn it into a JSON string
that will be compliant with a PHP Laravel API. The API request has the following validations: 

```php
[
	'code' => 'required|alpha_num',  
	'auto_apply' => 'boolean',  
	'type' => 'required|in:MONEY_DISCOUNT,PERC_DISCOUNT',  
	'description' => 'required|string',  
	'percentage' => 'required_if:type,PERC_DISCOUNT|pricing_float',  
	'currency' => 'required|string,  
	'amount' => 'required|pricing_float',  
	'start_date' => 'required|date',  
	'expiry_date' => 'nullable|date',  
	'num_booking_threshold' => 'integer|nullable',  
	'max_global_usage' => 'integer',  
	'max_usage' => 'integer',  
	'app_only' => 'boolean',  
	'user_id' => 'integer',  
	'listing_ids' => 'string',  
	'include_in_reporting' => 'required|boolean',  
	'shortened_url_id' => 'integer',  
	'display_name' => 'required|string',  
	'booking_type' => 'required|in:prebook,monthly,monthly_rolling,monthly_rolling_mon_fri',  
	'dynamic_expiry_days' => 'integer|nullable',
	'usage_months' => 'nullable|integer',
]
```

Present the JSON string to the user. No preamble.

input: "Make a promocode with the code 'TEST123' that gives me 20% off my next parking session only up to a total value of £10.00 that starts being valid from today."
output: '{"code":"TEST123","auto_apply":true,"type":"PERC_DISCOUNT","description":"TEST123","currency":"GBP","amount":10,"percentage":20, "start_date":"2024-05-01 00:00:00","num_booking_threshold":null,"max_global_usage":1,"max_usage":1,"include_in_reporting":true,"display_name":"TEST123","booking_type":"prebook"}'

input: "Make a promocode that is valid for monthly rolling bookings that gives £20 off every month for 5 months. Give it a random code."
output: '{"code":"6464a2c2-dbce-482f-a84c-ad8b49ce2718","auto_apply":true,"type":"MONEY_DISCOUNT","descriptions":"6464a2c2-dbce-482f-a84c-ad8b49ce2718","currency":"GBP","amount":20,"start_date":"2024-05-01 00:00:00","max_global_usage":1,"max_usage":1,"usage_months":5,"include_in_reporting":true,"display_name":"6464a2c2-dbce-482f-a84c-ad8b49ce2718","booking_type":"monthly_rolling"}'

input: 
"""

correcting_prompts = [
    """
Unless specified, the promo code is usable on any booking. If the user says they want the code to work on the fitst booking, num_booking_threshold should be 1. If second, it should be 2, and third, should be 3.
    """,
    """
Use yesterday's date at midnight for when the code is valid from unless the user tells you otherwise.
    """
]

complex_test = """
Create a promo code that gives me £5 off every month for 5 months on a monthly rolling booking that runs from Monday to Friday.
The code should be EHFIRSTPROMO.
This should not be limited to a particular booking. 
It should be usable 5 times but by a single user once. 
It should start from tomorrow at 15:00.
"""

react_prompt = """
You are an expert in creating promo codes for JustPark using a PHP Laravel API. JustPark is a global parking company. Someone will ask you
to make a promo code with specific parameters. Take their request and into a JSON and show the user for approval.

Do not assume the values of the JSON are correct. Describe how the promo code will work to the user and ask
if they would like to change anything. 

If the user confirms the JSON is correct, offer them the ability to create the promo code. Once created, present
the code to the user.
"""