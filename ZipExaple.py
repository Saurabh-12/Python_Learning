# As we see in map() section about applying something in parallel
#  between two lists? zip() makes this even easier.
firstName_list = ["Saurabh", "Sushant", "Sumant", "Raghav","Rudra"]
lastName_list = ["Sharma", "Kumar", "sharma", "kumar", "sharma"]

print([' '.join(x) for x in zip(firstName_list, lastName_list[::-1])])

