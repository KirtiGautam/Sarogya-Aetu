print("Loading pincodes for Bangalore region.....")
file = open('bangalore/pincodes.txt', 'r')
pincodes = file.readlines()
pincodes = [int(pincode.strip()) for pincode in pincodes]