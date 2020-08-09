if __name__ == '__main__':
    my_list= []
    table = [] #nested list containing names and grades
    l=[]     #list to save grades
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list = list([name, score])
        table.append(my_list)
    sorted_list= sorted(table) #nested list sorted according to the names
    for c,x in enumerate(sorted_list):
        a=x[1] #storing grades in variable a
        l.append(a)  #appending grades in the empty list l    
    l.sort(reverse=True) #list sorted in descending order
    s=sorted(set(l)) #list converted into sorted set to remove duplicate and find the second lowest grade
    for a,b in enumerate(sorted_list):
        if(s[1] == b[1]):
            sorted(b[0])
            print((b[0]))

            
       
        

            

    

