import re
'''
Jiajie Sven Yan
'''
def is_phone_number(input_string):
	"""
	the U.S. Phone number format standard is from
	https://en.wikipedia.org/wiki/North_American_Numbering_Plan
	"""
	num_pattern=re.compile(r'''
	    ^\(?[\d]{3}\)?[\s-]?         #area code
	    [\d]{3}[\s-]?                #central office code
	    [\d]{4}$                     #subscriber number
	''',re.X)
	is_valid=num_pattern.search(input_string);
	if is_valid:return True
	else:return False

def is_email_address(input_string):
	"""
	for local part, we define only letters, numbers and underscore are legal;
	for domain, we apply L (letters) D (digits) H (hyphen) rule.
	https://en.wikipedia.org/wiki/Email_address
	"""
	email_pattern=re.compile(r'''
	    ^\w+@
	    [a-zA-Z0-9](?:[\d]*[a-zA-Z-]+[\d]*)*[a-zA-Z0-9] #top-domain should not all be numbers
	    (?:\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*)+$    #hyphen should not be the start or end
	''',re.X)
	is_email=email_pattern.search(input_string)
	if is_email: return True
	else: return False
