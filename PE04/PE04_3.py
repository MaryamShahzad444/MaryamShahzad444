courses=["Mathmatics", "Physics" , "Chemistry" , "Biology" , "Computer Science"] #created alist courses
print("List of courses:", courses) # print courses
print("I am taking", len(courses),"courses") # using len method and printing the coureses
print("First course:", courses[0]) # using index
print("Last course:", courses[-1])
print("First four classes:", courses[:4])
print("Last four classes:", courses[1:])
print("Last four classes:", courses[-4:5])
print("Last four classes:", courses[-4:])
print("Classes except for the first and last:",courses[1:-1])
firstclass, *others, Lastclass = courses
print(others)


