information=[{'name':'Aryan', 'age':16, 'marks':89}, {'name':'Achal', 'age':19, 'marks':95},{'name':'Anshuman', 'age':18, 'marks':98},{'name':'Bharat', 'age':17, 'marks':94}]
user_choice=input('''ENTER THE OPERATION YOU WANT
(a) ADD NEW STUDENT
(b) DISPLAY ALL STUDENTS
(c) SEARCH A STUDENT BY NAME
(d) UPDATE MARKS
(e) DELETE A STUDENT
---> ''')
user_choice=user_choice.lower()
if user_choice == 'a':
    name=input('ENTER THE NAME OF THE STUDENT: ')
    age=int(input('ENTER THE AGE: '))
    marks=int(input('ENTER THE MARKS: '))
    information.append({'name': name , 'age':age,'marks':marks})
    print('SUCCESSFULLY ADDED')
elif user_choice =='b':
    for i in information:
        print(f'Name: {i['name']} , Age: {i['age']} , Marks: {i['marks']}')
elif user_choice =='c':
    who=input('ENTER THE NAME OF STUDENT TO SEARCH: ')
    for i in information:
        if who==i['name']:
            print(f'Name: {i['name']} , Age: {i['age']} , Marks: {i['marks']}')
    else:
            print('NOT FOUND !!')
elif user_choice =='d':
            who=input('ENTER THE NAME OF STUDENT: ')
            for i in information:
                if who==i['name']:
                    print('STUDENT FOUND !!')
                    mm=int(input('ENTER THE MARKS: '))
                    i['marks']=mm
                    print('UPDATED !!')
                    print(f'Name: {i['name']} , Age: {i['age']} , Marks: {i['marks']}')
            else:
                print('STUDENT NOT FOUND !!')
elif user_choice=='e':
    who=input('ENTER THE STUDENT NAME TO DELETE: ')
    for i in information:
        if i['name']==who:
            information.remove(i)
            print('DELETED SUCCESSFULLY !!')
            break
    else:
        print('STUDENT NOT FOUND')
else:
    print('ENTER VALID INPUT !!')
    

                    
            
            
            