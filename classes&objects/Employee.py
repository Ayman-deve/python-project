class Employee:
    def __init__(self,name,age,company,is_manager,rating):
        self.name=name
        self.age=age
        self.company=company
        self.is_manager=is_manager
        self.rating=rating    #the rating should be 1 ---> 10

    def excellance(self):

     if self.rating >=8 :
       return self.name+" is an Excellant Employee ;)"
     elif 8 >= self.rating >5:
        return self.name+" is a good Employee "
     else:
        return self.name +" should work harder -_-"


