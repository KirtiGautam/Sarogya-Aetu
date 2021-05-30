import os

# Set your environment variables as 
# MOBILES and KEYS, add comma separated mobiles and 
# KEYS(in same order of mobiles) to the variables. This file reads
# them into variables which is used by notifier
# More info: https://www.callmebot.com/blog/free-api-whatsapp-messages/


MOBILES = os.environ.get('MOBILES').split(',')

KEYS = os.environ.get('KEYS').split(',')

MOBILE_DATA = [
    {'MOBILE': MOBILES[x], 'API_KEY': KEYS[x]}
    for x in range(len(MOBILES))
]

# API url endpoint of callmebot
API_URL= 'https://api.callmebot.com/whatsapp.php'


# Pincodes goes here
PINCODES = [141010]
