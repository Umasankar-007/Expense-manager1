import json          #cell 1
from datetime import datetime
with open("expense.json","r") as f:
    data=json.load(f)
    
# data    #cell 2

ei=data['expense_info']      #cell 3
# ei


# # view by date test
# for id in ei.keys():        #cell 4
#     if '10.10.2023' == ei[id]['date']:
#         print("id> {0} and details > {1}".format(id,ei[id]))
# else:
#     print("\nNot available such expense...")

    
#pick last id       #cell 5
c_list=list(ei)
L_ID=c_list[-1]
# print(L_ID)


#id increase by 1 and make it global variable         #cell 6
c_int=int(L_ID)
c_int+=1
n_id=str(c_int)
global n_id

class Expense:           #cell 7
    def __init__(self,ei):
        self.ei=ei
    def add_expense(self,category,name,date,amount): 
        global n_id
        self.ei[n_id]={'category':category,'name':name,'date':date,'amt':amount}
        print("DETAILS HAVE BEEN UPDATED...")
        
        #increament by 1 and so on...
        conv_int=int(n_id)
        conv_int+=1      
        n_id=str(conv_int)
    def view_details(self):
        print(self.ei)
    def view_by_date(self,dt_input):
        for id1 in self.ei.keys():
            if dt_input == self.ei[id1]['date']:
                print("id > {0} and details {1}".format(id1,self.ei[id1]))
        else:
            print("\nNot available such expense...")
    def view_by_amount(self,amt_input):    #Pick  >amount of transaction 
        for id2 in self.ei.keys():
            if amt_input < self.ei[id2]['amt']:
                print("Show expense above Rs:",amt_input)
                print("id > {0} and details {1}".format(id2,self.ei[id2]))
        else:
            print("\nNot available such expense...")
    def view_by_category(self,cat_input):  #category specific expense
        for id3 in self.ei.keys():
            if cat_input == self.ei[id3]['category']:
                print("id > {0} and details {1}".format(id3,self.ei[id3]))
        else:
            print("\nNot available such expense...")
    def all_category(self):
        for id4 in self.ei.keys():
            print("id > {0} and category > {1}".format(id4,self.ei[id4]['category']))
    def all_date(self):          
        for id5 in self.ei.keys():
            print("id > {0} and date > {1}".format(id5,self.ei[id5]['date']))
    def view_by_date_range(self,from_dt,to_dt):
        for id6 in self.ei.keys():
            date_format='%Y-%m-%d'
            obj_from_dt=datetime.strptime(from_dt,date_format).date()
            obj_to_dt=datetime.strptime(to_dt,date_format).date()
#             if from_dt or to_dt == self.ei[id6]['date']:
            dt_json=self.ei[id6]['date']
            obj_dt_json=datetime.strptime(dt_json,date_format).date()   #pick only date 
            if obj_from_dt<=obj_dt_json<=obj_to_dt:
                print("id > {0} and details > {1}".format(id6,self.ei[id6]))
        else:
            print("\nNot available such expense...")
    def view_by_year(self,year_input):
        for id7 in self.ei.keys():
            date_format='%Y-%m-%d'  
            date_json=self.ei[id7]['date']
            obj_date_json=datetime.strptime(date_json,date_format).year      #pick only year
            if year_input==obj_date_json:
                print("id > {0} and details > {1}".format(id7,self.ei[id7]))
        else:
            print("\nNot available such expense...")
    def delete_expense(self,id_input):    #delete by id
        for id8 in self.ei.keys():
            if id_input==int(id8):
                del self.ei[id8]
                print("DELETION DONE! DETAILS HAVE BEEN UPDATED...")
        else:
            print("\nNot available such expense...")
            
            
            
            
            
def main():      #cell 8
    exp=Expense(ei) #object create
    print("Welcome to Expense Manager")
    while True:
        try:
            print('''
                what do you want:
                1.Add expense
                2.View details
                3.Delete expense
                4.Exit
            ''')
            choice=int(input("\nEnter your choice : "))
            match choice:
                case 1: #Add expense
                    try:
                        no_add_exp=int(input("how many expense you want to add: "))
                        for i in range(no_add_exp):
                            category=input("Enter expense category name: ")
                            name=input("Enter expense name: ")
                            date=input("Enter expense date(YYYY-MM-DD format): ")
                            amount=int(input("Enter expense amount: "))
                            exp.add_expense(category,name,date,amount)
                        print(ei)
                    except Exception as e:
                        print(e,"\nEnter valid input...")
                case 2: #View details
                    while True:
                        try:
                            print('''
                            submenu of view details>>
                                what do you want:
                                1.View all
                                2.View by date
                                3.View by date range (will ask for start and end date)
                                4.view by >amount of transacion
                                5.view by category (case insensitive)
                                6.view by year wise
                                7.exit
                            ''')
                            choice1=int(input("Enter your choice : "))
                            match choice1:
                                case 1: #View all
                                    exp.view_details()
                                    
                                case 2: #View by date
                                    dt_input=input("Enter date(YYYY-MM-DD format): ")
                                    exp.view_by_date(dt_input)    
                                    
                                case 3: #View by date range
                                    print("All expense dates >> ")
                                    exp.all_date()       #show all dates first             
                                    print("Date input should be YYYY-MM-DD format...")
                                    from_dt=input("Enter from which date: ")
                                    to_dt=input("Enter to which date: ")
                                    exp.view_by_date_range(from_dt,to_dt)
                                    
                                case 4: #view by >amount of transacion
                                    try:
                                        amt_input=int(input("Enter amount(in Rs): "))
                                        exp.view_by_amount(amt_input)
                                    except Exception as e3:
                                        print("Enter valid input...")
                                        
                                case 5: #view by category
                                    print("All category >>")
                                    exp.all_category()   #show all category first 
                                    cat_input=input("Enter category: ")
                                    exp.view_by_category(cat_input)
                                    
                                case 6: #view by year wise
                                    try:
                                        print("Year input should be between 2000-2023 Yr...")
                                        year_input=int(input("Enter which year expense you want: "))
                                        if 2000<=year_input<=2023:
                                            exp.view_by_year(year_input)
                                        else:
                                            break
                                    except ValueError:
                                        print("Enter valid year format...")
                                case 7: #Exit from view details
                                    break
                                case _:
                                    print("\nPress only 1/2/3/4/5/6/7...")
                        except Exception as er1:
                            print("\nEnter valid choice...")
                case 3: #Delete expense
                    try:
                        id_input=int(input("Enter expense id: "))
                        exp.delete_expense(id_input)
                    except ValueError:
                        print("Not have such id...")
                case 4: #Exit
                    break
                case _:
                    print("press only 1/2/3...")
        except Exception as er:
            print("\nEnter valid choice...")
            
            
            
            
if __name__ == '__main__':        #cell 9
    main()
    
    
#save the final output         #cell 10
final = json.dumps(data,indent=2)
with open('export.json','w') as f:
    f.write(final)