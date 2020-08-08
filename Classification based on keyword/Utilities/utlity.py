from flashtext.keyword import KeywordProcessor

keywords = ["AC Services",
"Tyres and Wheel Care",
"Cleaning and Detailing",
"Denting and Painting",
"Batteries",
"Insurance Services",
"Light and Fitments",
"Glass and Custom Services",
]

# for keyword processing
kp0=KeywordProcessor()
for word in keywords:
    kp0.add_keyword(word)

# to calculate the percentage of Matching_value
def percentage1(dum0,dumx):
    try:
        ans=float(dumx)/float(dum0)
        ans=ans*100
    except:
        return 0
    else:
        return ans


