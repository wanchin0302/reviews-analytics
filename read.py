data = []
count = 0
with open("reviews.txt", "r") as f:
	 for line in f:
	 	data.append(line)
	 	count =+ 1
	 	if count % 1000 == 0:  # %餘數，1000的倍數 
	 	    print(len(data))  #每1000筆，印一次計數
print(len(data))
print(data[0])
print("-----------------")
print(data[1])