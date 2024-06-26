#create a list of states

states = ["California", "New York", "Texas", "Pennsylvania", "Hawaii"]
# print(states[2])

#can change the name of item in the list by reassigning
states[1] = "NY"

#adding to a list
states.append("Washington")

#adding multiple of items to a list
states.extend(["Florida", "Oregon", "Chicago"])

print(states)

#nested lists - list within a list
fruits = ["strawberries", "apples", "oranges", "peaches"]
vegetables = ["kale", "celery", "spinach", "carrots"]
smoothie = [fruits, vegetables]
print(smoothie)
print(smoothie[1][1]) #this will index vegetable list then index 1 in vegetable list
