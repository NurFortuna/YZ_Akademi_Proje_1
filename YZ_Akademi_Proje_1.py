


def getElements():
    
    list=[] #An empty list is taken to store the values of elements
    for i in range(5):
        #taking input from user
        elm=input(str(i+1)+" element: ")
        #inputs are appended in the list
        list.append(elm)
    return list
        
        
     
def dublicates(list):
    
    dublicates=[] #An empty list is taken to store the values of duplicate elements
    for i in range(len(list)):
        n=i+1 
        """
        The for loop is used to access the values in the list
        ,and the condition is used to check if the elements in
        the given list are not present in the empty list and j 
        and i equal
        """
        for j in range(n,len(list)): 
            if list[i] not in dublicates and list[i]==list[j]:
                #If the elements are not present, those values are appended to the list
                    dublicates.append(list[i]) 
            
      
    return dublicates


def getDublicates(list):
    
    new_list=[] #An empty list is taken to store the values of duplicate elements with index
    for i in range(len(list)):
        """The for loop is used to access the values in the list ,
        and the the elements are appended  to the list with index"""
        
        new_list.append(str(i+1)+"- "+list[i])
        
    return new_list

    
elm=getElements()
elmDub=dublicates(elm)
print(getDublicates(elmDub))

    