myDict1 = {}
myDict1 ['ibm'] = '12345'
myDict1 ['ibm-x'] = '1245-x'
myDict1 ['hp'] = '45678'
myDict1 ['asus'] = '56901'
myDict1 ['lenovo'] = '12345'
print(myDict1 ['hp'])
search = input('enter comp. code: ')
for name,code in myDict1.items():
    if code == search:
        print (name)
        break
        #continue
else: print ('computer does not exist')