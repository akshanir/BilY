import textBased as tb

with open(r"C:\Users\Jody\Desktop\BilY\data\mostcommonwords.txt", encoding='utf-8') as file: # Use file to refer to the file object
  data = file.readlines()
  for i in data:
    if i[-1] == '\n':
      i = i[:-1]
      print(i, end = ' ')
  print(data)
  
