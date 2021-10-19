my_sent = input('Enter sentence ') # my_name to my_sent
words = my_sent.split() # split a sentence to the parts
rev_string = [word[::-1] for word in words] # reverse all words in sentence
rev_sent=" ".join(rev_string)  # Add everything back to normal view
print(rev_sent.capitalize()) # 1st letter Capital

# one -liner 
print(' '.join(word[::-1] for word in my_sent.split(" ")).capitalize())