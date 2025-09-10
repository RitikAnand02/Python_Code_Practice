# input user 5 subject marks 100. calculate the total 5 subject of marks out of 500. calculate 
#the percentage of 5 subject of marks . if percentile is grater than 75 will be pass otherwise fail.
sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
sub4 = int(input("Enter marks for subject 4: "))
sub5 = int(input("Enter marks for subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100
print("Total Marks:", total)
print("Percentage:", percentage)
if percentage > 75:
    print("Pass")
else:
    print("Fail")