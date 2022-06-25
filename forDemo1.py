
for letter in 'English':
    print ('The current Letter is :', letter)
print('\nthank you!')

for server in ['ibm','lenovo','hp','dell']:
    print ('The current Letter is :', server)
print('\nthank you!')

for product in ('fan','ac','washer','stove'):
    print ('The current Letter is :', product)
print('\nthank you!')
'''
myDict1 = {}
myDict1['ibm']='12345'
myDict1['ibm-x']='23098'
myDict1['hp']='28764'
myDict1['dell']='09416'
# use for loop to iterate through the myDict1 entries hint: use items() method


dict1= {'empName': 'Simon', 'title': 'Director', 'yoEmp': '9'}
for key in dict1:
    print(key, 'corresponds to', dict1[key])

myDict1 = {}
myDict1['ibm']='12345'
myDict1['ibm-x']='23098'
myDict1['hp']='28764'
myDict1['dell']='09416'
#klist=[]
#vlist=[]

for key,value in myDict1.items():
    print ('key: '+key+' ' +'value :'+value)
    #print(value)
    if key!= 'ibm' or key!= 'hp':
        food_list2=list(myDict1.keys())
print(food_list2)

print()

for key in myDict1.keys():
    print (key,myDict1[key])

'''