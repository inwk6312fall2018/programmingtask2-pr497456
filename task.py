fin=open('Crime.csv')
list1=[]
list2=[]
dict1={}
dict2={}
for line in fin:
  line=line.strip()
  s=line.split(',')
# to get the repetition number 
  list1.append(s[-1])  #takes the type of crime
  for items in list1:
    if items not in dict1:
      dict1[items]=1
    else:
      dict1[items]+=1
# to get the ID
  list2.append(s[-2]) 
  for items in list2:
    if items not in dict2:
      dict2[items]=1
    else:
      dict2[items]+=1
#printing tabular format
  print("{:<8} {:<20}".format('Crime_type',' Crime_count')) 

  for k, v in dict1.items():
    value= v
  print("{:<8} {:<20}".format(k, value))
