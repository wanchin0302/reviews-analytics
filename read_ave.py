data = []
count = 0
with open("reviews.txt", "r") as f:
	 for line in f:
	 	data.append(line)
	 	count =+ 1
	 	if count % 1000 == 0:  # %餘數，1000的倍數 
	 	    print(len(data))  #每1000筆，印一次計數
print("檔案已讀取完，共有"，len(data)，"筆資料")

#算留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print("留言的平均長度為: "，sum_len/len(data))
