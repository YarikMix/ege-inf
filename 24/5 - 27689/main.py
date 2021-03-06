with open("input.txt") as f:
	s = f.readline()

k = 0
max_len = 0
 
frags = ['X', 'Y', 'Z']
frag_index = 0
 
for i in s:
    if i == frags[frag_index]:
        k += 1
        frag_index = (frag_index + 1) % 3
    else:
        max_len = max(max_len, k)
        k = 0
        frag_index = 0
        if i == 'X':
            k = 1
            frag_index = 1
 
max_len = max(max_len, k)
 
print(max_len)

# Ответ: 13