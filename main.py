import sys
if len(sys.argv) <2:
	print ("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

#Create function get_book_text
def get_book_text(filepath):
	with open(filepath) as text: #open
		file_contents = text.read() #read
	return file_contents #return

from stats import count_words
from stats import count_char
from stats import count_char_sort

#Create function main to Call get_book_text
def main():
	relative_path = sys.argv[1] #set path of the book
	result_text = get_book_text(relative_path) #set result
	result_number = count_words(result_text)
	result_char	= count_char(result_text)
	result_char_sort = count_char_sort(result_char)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {relative_path}")
	print("----------- Word Count ----------")
	print(f"Found {result_number} total words")
	print("--------- Character Count -------")
	for item in result_char_sort:
		print(f"{item['char']}: {item["num"]}")


#Call Main()
main()
