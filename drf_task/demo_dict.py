dict_1={}
dict_1[0]='name'
dict_1['numbers']=10,20,30
dict_1[0]='age'
dict_1['nested_dict']={'nested':{'name':'name_1','age':23}}
dict_1['nested_dict']={'nested':{'name':'name_1','age':24}}
print(dict_1)

dict_data={'doc_hos_id': 2, 'doc_id': 2, 'doc_name': 'dr divya dubey', 'doc_email': 'dr divya dubey@gmail.com', 'qualifcation': 'heart_speclist', 'salary': 100000}
print(dict_data['doc_name'])
dict_data['doc_name']='dr divya dubey'
print(dict_data)
print(dict_data.get('doc_name'))

# from datetime import datetime
dict_1={'id': 2, 'book_author_id': 2, 'book_publisher_id': 1, 'title': 'sql_title', 'price': 1000000, 'release_date': (2023, 3, 17)}
dict_2=dict_1.copy()
print(dict_1)
print(dict_2)
dict_1.clear()
print(dict_1)

for item,value in dict_2.items():
    print(item)
    print(value)

print(dict_2.items())
print(dict_2.get('title'))
print(dict_2.pop('id'))
print(dict_2)
print(dict_2.popitem())

input={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
l=[]
for item,value in input.items():
  l.append((item,value))
  l.sort()
print(dict(l))

# input={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# import pdb;pdb.set_trace()
# lst=[]
# for item,value in input.items():
#    lst.append((item,value))
# print(lst[0])
# for i in range(0,len(lst)):
#   print(lst[i])
#   for k in range(1,len(lst)):
#    if lst[i][1]>lst[k][1]:
#     lst[i][1]=lst[k][1]
# print(dict(lst))

input={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
lst=[]
for item,value in input.items():
   lst.append((item,value))
print(lst)
lst.sort(key = lambda x: x[1])
print(lst)

lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[0])
print(lst)

lst=[('rahul',24,'880'),('shri',23,'600'),('apple',30,'200'),('candy',64,'300')]
lst.sort(key=lambda x:x[2])
print(lst)

x=lambda a:a+10
print(x(10))

Input ={'a': 100, 'b':200, 'c':300}
sum=0
for item,value in Input.items():
  sum=sum+value
print("sum value id",sum)

Input ={'x': 25, 'y':18, 'z':45}
sum=0
for value in Input.values():
   print(value)
   sum+=value
print(sum)

list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
lst=[]
# import pdb;pdb.set_trace()
for list_item in list:
   for item,value in list_item.items():
      print(value)
      lst.append((item,str(value)))
      sorted(lst,key=lambda x:x[1])
print(dict(lst))

l=[1,3,5,78,00,7,77,89,9,90,00,]
print(sorted(l,reverse=True))

from operator import itemgetter
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
lst=sorted(list,key=itemgetter('age'))
lst=sorted(list,key=itemgetter('name'))
lst=sorted(list,key=itemgetter('name','age'))
print(lst)

dict_1={'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
lst=[] 
lst_1=[]
for item,value in dict_1.items():
    lst.append(([item]+value))
print(lst)

test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"] 
dict_1={}
# import pdb;pdb.set_trace()
for key in key_list:
  for value in test_list:
    dict_1[key]=value
  print(dict_1)

test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"] 
lst=[]
for idx in range(0,len(test_list),2):
   lst.append({key_list[0]:test_list[idx],key_list[1]:test_list[idx+1]})
print(lst)

      