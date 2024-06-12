import re
import unidecode

def generate_variations(keyword):
	variations = []
	variations.append(keyword)  # Add the original keyword
	variations.append(keyword.replace(' ', ''))  # Replace spaces with * *
	variations.append(keyword.replace(' ', '* *'))  # Replace spaces with * *
	variations.append(keyword.replace(' ', '-'))  # Replace spaces with *-*
	variations.append(keyword.replace(' ', '+'))  # Replace spaces with *+*
	variations.append(keyword.replace(' ', '%20'))  # Replace spaces with *%20*
	variations.append(keyword.replace(' ', '_'))  # Replace spaces with *_*

	return variations

def is_ascii(s):
	return all(ord(c) < 128 for c in s)

def process_keywords(input_file, output_file):
	with open(input_file, 'r', encoding='utf-8') as file:
		keywords = [line.strip() for line in file.readlines()]

	all_variations = set()
	for keyword in keywords:
		if not is_ascii(keyword):
			ascii_keyword = unidecode.unidecode(keyword)
			if not is_ascii(ascii_keyword):
				continue
			keyword = ascii_keyword
		variations = generate_variations(keyword)
		all_variations.update(variations)

	sorted_variations = sorted(all_variations, key=lambda x: re.sub(r'[^a-zA-Z0-9]', '', x).lower())
	unique_variations = list(dict.fromkeys(sorted_variations))

	# Filter out empty or whitespace-only lines
	final_variations = [variation for variation in unique_variations if variation.strip()]

	with open(output_file, 'w', encoding='utf-8') as file:
		for i, variation in enumerate(final_variations):
			if i != 0:
				file.write('\n')
			file.write(variation)

def main():
	input_file = 'keywords.txt'
	output_file = 'complete_keystrings.txt'

	process_keywords(input_file, output_file)
	print("Complete keystrings generated, duplicates removed, sorted, and written to", output_file)

if __name__ == "__main__":
	main()