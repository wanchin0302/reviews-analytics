data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
print("檔案已讀取完, 共有", len(data), "筆資料")
print(data[0])


wc={} # wc=word_count
for d in data:
	words = d.split(" ")
	for word in words:
		if word in wc:
			wc[word] =+ 1
		else:
			wc[word] = 1  #新增進字典是WC字典			
for word in wc:
	if wc[word] > 1000:
		print(word, wc[word])

print(len(wc))
print(wc["Joyce"])

while True:
	word = input("請問您想查什麼字:")
	if word == "q":
		break
	if word in wc:
		print(word, "出現過的次數為:", wc[word])
	else:
		print("查無此字。")
print(謝謝使用)