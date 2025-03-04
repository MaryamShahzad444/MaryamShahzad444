n=[] #(a) empty list called n
n.append(2) #(b) Add 2 and 4 into the list
n.append(4) 
print(n) #(c) print the list
n.insert(0,0) #(d) Add 0, 1 and 3 in proper order
n.insert(1,1) 
n.insert(3,3) 
print(n) #(e) Print the list
n.append(5) #(f) Add 5 in proper order
print(n) #(g) Print the list
removed_1=n.pop(0) #(h) Remove 0 from the list.
print(n) #(i) Print the list
removed_2=n.pop(n.index(2)) #(j) remove 2 from the list
print(n) #(k) Print the list
print(removed_2) #(j) Print removed no. 2 
removed_4=n.pop(n.index(4)) #(l) remove 4 from the list
print(n) #(m) Print the list
print(removed_4) #(l) Print removed no. 4
sum_removed=removed_1+removed_2+removed_4 #(n) Add all the removed numbers and 
print("sum of all removed items =",sum_removed) #(n) print the sum
n[0]=100 #(o) Change the first item to 100 and last item to 9.9
n[-1]=9.9 #(o) 
newNum=n.copy()
print(newNum)
n.clear() #(p) clear list
print("Original List:" , n) #(r) Print the original list, n and the newNum list
print("New List:", newNum)
del n #(s) Delete the list n
