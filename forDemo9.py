courses = {'aisc1000-01':65, 'comp1027-4':68, 'comp1027-5': 59, 'csd1000-01':24}
codes = list (courses.keys())#converting the keys of the dict into a list
codes.sort()
for var in codes: # codes is a list
    print (courses[var])
