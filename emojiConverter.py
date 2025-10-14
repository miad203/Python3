emoji = {
	":)" : "happy",
	":(" : "sad",
	"<3" : "love",
	":'(" : "cry",
}

user_input = input('Enter your word: ')

output = ''

for each_word in user_input.split():
    if each_word not in emoji:
        output += each_word + " "
    else:
        if emoji.get(each_word) != None:
            output += emoji.get(each_word) + " " 

print(output)
