# students = ["Alice", "Javi", "Damien "]
# students.append("Delilah")
# print(students)
#
# students = ["Alice", "Javi", "Damien "]
# students.insert(1, "Zoe")
# print(students)
#
# students = ["Alice", "Javi", "Damien ", "Javi"]
# students.remove("Javi")
# print(students)
#
# # my_list.insert(index, element)
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "John", "Joe", "Chris", "Sam"]
# for name in smith_siblings:
#     print(name + " Smith")
#
# print(len(smith_siblings))
#
# # count = 0
# # for name in smith_siblings:
# #     count = count + 1
# #     print(count);
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "Brianna", "Javi"]
# for index in range(len(smith_siblings)):
#     smith_siblings[index] = smith_siblings[index] + " Smith"
#
# print(smith_siblings)
#
# superheroes = ["Captain Marvel", "Wonder Woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
# demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5?"))
#
# if demoted_hero in superheroes:
#     superheroes.remove(demoted_hero)
#     print("Top 5 heroes:", superheroes)
# else:
#     print("Hero not found.")
#
#
# names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
# print(names[::-1])
# print(names[4:2:-1])
# print(names[::-2])
# print(names[::2])
#
# state1 = 'New York'
# abbv1 = 'NY'
# state2 = 'California'
# abbv2 = 'CA'
# state3 = 'Texas'
# abbv3 = 'TX'


states = {"NY": "New York", "CA": "California", "TX": "Texas", "AZ": "Arizona", "HI": "Hawaii"}
state_input = str(raw_input("Enter state abbreviation:""))
