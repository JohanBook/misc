text = text.replace("!", ".").replace("?", ".")

for idx, line in enumerate(text.split(".")):
  line = line.strip()
  if not line:
    break

  words = line.lower().split(" ")
  
  first_char = words[0][0]
  alliteration = True
  for word in words:
    if word[0] != first_char:
      alliteration = False
  if alliteration and len(words) > 1:
    print(f"'{line}', sentence {idx}")
