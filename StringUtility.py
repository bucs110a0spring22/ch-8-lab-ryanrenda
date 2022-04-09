class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
    num_vowels=0
    for char in self.string:
      if char in "aeiouAEIOU":
        num_vowels = num_vowels+1
    return str(num_vowels) if num_vowels <5 else "many"

  def bothEnds(self):
    return '' if len(self.string) <= 2 else self.string[0:2] + self.string[-2:] 

  def fixStart(self):
    return self.string if len(self.string) <= 1 else self.string[0] + self.string[1:].replace(self.string[0],'*')

  def asciiSum(self):
    total = 0
    for char in self.string:
      total = total + ord(char)
    return total

  def cipher(self):
    code = ""
    for i in self.string:
      if i.isalpha():
        if i.islower():
          rearrange = (ord(i) - 97 + len(self.string)) % 26
          rearrange = rearrange + 97
        if i.isupper():
          rearrange = (ord(i) - 65 + len(self.string)) % 26
          rearrange = rearrange + 65
        letter = chr(rearrange)
      else: letter = i
      code = code + letter
    return code
        
    