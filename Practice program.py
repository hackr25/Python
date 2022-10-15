#implementation of operations in dictionary
applications={'1':{'Name':'ABC','MOB':'9967543211','Marks':'90'},
              '2':{'Name':'PQR','MOB':'9967543212','Marks':'70'},
              '3':{'Name':'XYZ','MOB':'9967543213','Marks':'80'}}
labels={'Name':'Candidate\'s Name',
        'MOB':'Contact Number',
        'Marks':'Marks obtained'}
print('The total number of applications=',len(applications))
application_no=input("Enter Application number")
response=input("Name (N) or contact number(C) or marks obtained(M)?")
if response=='N':
      key='Name'
if response=='C':
      key='MOB'
if response=='M':
      key='Marks'
if application_no in applications:
      print("The %s for application no=%s is %s." %(labels[key],application_no,applications[application_no][key]))
      
