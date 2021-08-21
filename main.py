def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter in "AEIOUaeiou":
       translation = translation + "t"
    else:
      translation = translation + letter  
  return translation

print(translate(input("enter a phrase: ")))
