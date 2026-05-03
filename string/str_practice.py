Name = input("Enter your name: ")
print(f"Hello, {Name}!")

letter = '''Dear <|NAME|>,
   You are selected!
   Thanks and Regards,
   <|Date|>'''
print(letter.replace("<|NAME|>", Name).replace("<|Date|>", "2024-06-30"))