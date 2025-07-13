#Create function to count
def count_words(content):
	count_number = len(content.split())
	return count_number

def count_char(content):
	content_dict = {}
	lowercase_content = content.lower()
	for character in lowercase_content:
		if character in content_dict:
			content_dict[character] +=1
		else:
			content_dict[character] = 1
	return content_dict

def sort_on(item): #sorting function
	return item["num"]

def count_char_sort(count_char):
	sort_list =[]
	for key1 in count_char:
		if key1.isalpha():
			sort_list.append({"char": key1, "num": count_char[key1]})
	sort_list.sort(reverse=True, key=sort_on)
	return sort_list


