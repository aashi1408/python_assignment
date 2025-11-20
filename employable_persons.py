#Employable_persons
n = int(input())#count of applicants
min_skill = int(input())

for b in range(n):
    skills_have = int(input())
    if(skills_have>=min_skill):
        print("YES")
    else:
        print("NO")
