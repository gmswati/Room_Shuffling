def small_group(No_of_girls):
    i=0
    new_list=[]
    a=[]
    while i<len(Data['Room_no']):
        # print(Rooms_List[i])
        girls_list_Roomwise=[]
        j=0
        while j < No_of_girls:
            # a=Name_List.random()
            def girl_name():
                index= randint(0,len(Data['name'])-1) 
                # return Name_List[index]

            # name=girl_name()
                if Data['name'][index] not in new_list:
                    new_list.append(Data['name'][index])
                    girls_list_Roomwise.append(Data['name'][index])
                
                else:
                    girl_name()
            girl_name()
            j+=1
        a.append(girls_list_Roomwise)
        # print(girls_list_Roomwise)
        i+=1
    # print('a = ',a)

    i=0
    c=0
    while i<len(Data['name']):
        if Data['name'][i] not in new_list:
            if c==len(Data['Room_no']):
                c=0
                a[c].append(Data['name'][i])
            else:
                a[c].append(Data['name'][i])
            c+=1
        i+=1

    Suffeled_data={}
    j=0
    while j<len(Data['Room_no']):
    # print (Data['Room_no'][j],' : ',end='')
    # print(a[j])
        Suffeled_data[Data['Room_no'][j]]=a[j]

        j+=1

    print(Suffeled_data)






def big_group(No_of_girls):
    a=[]
    New_list=[]
    j=0
    z=(len(Data['name'])//No_of_girls)
    while j<(len(Data['name'])//No_of_girls):
        i=0
        girls_list_Roomwise=[]
        while i<No_of_girls:
            def girl_name():
                index= randint(0,len(Data['name'])-1) 
                    
                if Data['name'][index] not in New_list:
                    New_list.append(Data['name'][index])
                    girls_list_Roomwise.append(Data['name'][index])
                
                else:
                    girl_name()
            girl_name()
            i+=1
        j+=1
        a.append(girls_list_Roomwise)
        print(girls_list_Roomwise)
    
    i=0
    c=0
    l=len(a)
    list1=[]
    while i<len(Data['name']):
        if Data['name'][i] not in New_list:
            list1.append(Data['name'][i])
        i+=1

    a.append(list1)

    Suffeled_data={}
    j=0
    while j<len(a):
        Suffeled_data[Data['Room_no'][j]]=a[j]
        j+=1

    print(Suffeled_data)



from random import randint

Data={'name':['Swati','Karina','Shivani','Mansha','Poonam','Aarti','Jaya','Riti','Devangana','Anisha','sapna','swapna','shruti','pooja','priyanka','stuti','sweety','meena','teena','triveni','manisha','likhita','ashwini','neha','Anokhi','vaishali'],
        'Room_no':[501,502,503,604,632,798]
        }

print(len(Data['name']))
def girls_no(): 
    No_of_girls=int(input('enter the min no. of girls that should stay in a room:\n'))
    # print(len(Data['name'])//No_of_girls)
    if No_of_girls*len(Data['Room_no'])<=len(Data['name']):
        print("ok,let's start suffling")
        small_group(No_of_girls)
    else:
        big_group(No_of_girls)
        
girls_no()



