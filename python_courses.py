education_levels = {
  "primary_school" : ["English language", "Physical education", "Art", "Mathmatics", "Music"],
  "secondry_school" : ["English language", "Physical education", "Mathmatics", "Physics", "Chemistry"],
  "high_school" : ["English language", "Physical education", "Mathmatics", "Physics", "Chemistry", "Biology", "Computer science"]
}



for element in education_levels.values():
  for course in element:
    if course == "Computer science" :
      confirmation_message = f"It shows you are in the last year of high school"
      print(confirmation_message)
    elif course == "Biology":
      rejection_message = "You are in highschool but not in the last year"
      print(rejection_message)



# fruit = "pineApple"
# print("It is nice fruite") if fruit  else print("Its is falsy value. There is not any fruit here")

# sequence_numbers = [1,2,3,4]
# print(type(sequence_numbers))

# print("Type of sequence_numbers is <class 'list'>") if isinstance(sequence_numbers, list) else print("It has a different type")

# if fruit == "pineApple":
#   pass


fruit = "peach"

match fruit:
  case "Banana"| "pear" | "papaya" | "apple":
    print("Nice fruit")
  case "cherry" | "peach" | "watermelone"  :
    print("Lovely fruit")
  case "pineApple" | "nectarin" | "appricot":
    print("Great fruit")