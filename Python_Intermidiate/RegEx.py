import re
#
# text = '''
# Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information
# on Tesla's products can be found at https://www.tesla.com/. Also here are leading influence's
# for tesla related news,
# https://twitter.com/teslarati
# https://twitter.com/dummy_tesla
# https://twitter.com/dummy_2_tesla
# '''
#
# pattern = '\.com\/([^ |,|.\|\n]+)'
# matches = re.findall(pattern, text)
# print(matches)
#
# # Efficient Method
# pattern = 'https:\/\/twitter\.com\/([a-zA-Z0-9_]+)'
# matches = re.findall(pattern, text)
# print(matches)
#
#
# text = '''
# Concentration of Risk: Credit Risk
# Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
# restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
# or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
# and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
# hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
# Concentration of Risk: Supply Risk
# We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
# products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
# suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
# '''
#
# pattern = 'Concentration of Risk: ([a-zA-Z ]+)'
# matches = re.findall(pattern, text)
# print(matches)
#
#
# text = '''
# Tesla's gross cost of operating ihsdhfcikhnaishuifc lease vehicles in FY2021 Q1 was $4.85 billion.
# BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.'''
#
# pattern = 'FY(\d{4} [a-zA-Z]\d)'
# matches = re.findall(pattern, text)
# print(matches)
#
# # Efficient Method
# pattern = 'FY(\d{4} (?:Q[1-4]|S[1-2]))'  # (?:) is used to enclosed the pattern.
# matches = re.findall(pattern, text)
# print(matches)
#
# pattern = 'i[a-zA-Z]+'  # (?:) is used to enclosed the pattern.
# matches = re.findall(pattern, text)
# print(matches)

f = open('numbers', 'r')
l = []
sum = 0
#
# for i in f:
#     i = i.strip()
#     num = re.findall('[0-9]+', i)
#     if num == []: continue
#
#     l.append(num)
# print(l)

file = f.read()

num = re.findall('[0-9]+', file)

for nums in num:
    nums = int(nums)
    sum += nums

print(sum)



