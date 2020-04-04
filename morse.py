# Text to Morse Convertor

__author__ = 'HusainShaikh895'
# • : dot used for representation


def char_to_morse(char):
	try:
		letters = {'a':'•-', 'b':'-•••', 'c':'-•-•', 'd':'-••', 'e':'•', 'f':'••-•', 'g':'--•', 'h':'••••', 'i':'••', 'j':'•---', 'k':'-•-', 'l':'•-••', 'm':'--', 'n':'-•', 'o':'---', 'p':'•--•', 'q':'--•-', 'r':'•-•', 's':'•••', 't':'-', 'u':'••-', 'v':'•••-', 'w':'•--', 'x':'-••-', 'y':'-•--', 'z':'--••', '0':'-----', '1':'•----', '2':'••---', '3':'•••--', '4':'••••-', '5':'••••', '6':'-••••', '7':'--•••', '8':'---••','9':'----•'}
		return letters[char]
	except:
		print('Invalid Input. Only Enter alphanumeric characters.')
		return None


def text_to_morse(text):
	try:
		words = list(text.split())
		newStr = ''
		for word in words:
			w = ''
			for char in word:
				w += char_to_morse(char)
				w += ' '
			newStr += w
			newStr += '   '
		return newStr
	except:
		return None


def morse_to_char(m):
	try:
		letters = {'a':'•-', 'b':'-•••', 'c':'-•-•', 'd':'-••', 'e':'•', 'f':'••-•', 'g':'--•', 'h':'••••', 'i':'••', 'j':'•---', 'k':'-•-', 'l':'•-••', 'm':'--', 'n':'-•', 'o':'---', 'p':'•--•', 'q':'--•-', 'r':'•-•', 's':'•••', 't':'-', 'u':'••-', 'v':'•••-', 'w':'•--', 'x':'-••-', 'y':'-•--', 'z':'--••', '0':'-----', '1':'•----', '2':'••---', '3':'•••--', '4':'••••-', '5':'•••••', '6':'-••••', '7':'--•••', '8':'---••','9':'----•'}
		morse = {v:k for k, v in letters.items()}
		morse['='] = ' '
		return morse[m]
	except:
		print('Invalid Input. Only Enter morse code for alphanumeric characters.')
		return None


def morse_to_text(morse):
	try:
		morse = morse.replace('.', '•')
		morse = morse.replace('  ', ' = ')
		morse = list(morse.split())
		newStr = ''
		for word in morse:
			newStr += morse_to_char(word)
		return newStr
	except:
		return None


def main():
	print('Text to Morse [t] or Morse to Text [m]')
	while(True):
		command = input('What do you want to do?: ').lower()
		if(command.startswith('t')):
			text = input('Enter the alphanumeric text to be converted: ').lower()
			print(text_to_morse(text))
		elif(command.startswith('m')):
			morse = input('Enter the morse code... seperate characters with one blank space and letters with two blank spaces')
			print(morse_to_text(morse))
		else:
			print('Invalid Input')
			break




if __name__ == '__main__':
	main()