print("---Simple grade calculator---")

score = float(input("Enter marks from 0-100: "))

if score >= 80: # Range 80 - 100
    print("Grade: A ")
elif  score >= 70: # Range 70 - 79
    print("Grade: B ")
elif  score >= 60: # Range 60 - 69
    print("Grade: C ")
elif  score >= 50: # Range 50 - 59
    print("Grade: D ")
else: 
    print("Grade: F ") # Below 50
