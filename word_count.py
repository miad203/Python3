def wordcount(sentence) -> int: 
  sentence = sentence.lower()
  article_and_preposition = [
    "a", 
    "an", 
    "the",
    "in",
    "on",
    "at",
    "to",
    "from",
    "with",
    "about",
    "for",
    "by",
    "of",
    "into",
    "over",
    "under",
    "between",
    "among",
    "after",
    "before",
    "through",
    "around",
    "without"
]
  word, letter = 0, 0
  words = sentence.split(' ')
  for each_word in words: 
    if each_word not in article_and_preposition:
      word+=1
    for each_letter in each_word: 
      letter+=1
  
  return word, letter

  
  
  

   
  
  
def main():
  user_inpt: str = input("Enter your sentence: ").strip()
  _word, _letter = wordcount(user_inpt)
  print(f"This sentence consist of {_word} word\nand {_letter} letter")
  

if __name__ == "__main__":
  main()
  
  