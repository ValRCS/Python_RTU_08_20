# Apgrieztie vārdi
 
sentence = input("Ievadiet teikumu: ")

def get_reversed_words(sentence:str) -> str:
    """Returns list of reversed words in sentence
    Args:
        sentence (str): sentence to reverse
    Returns:
        string: reversed sentence
    """
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

reversed_sentence = get_reversed_words(sentence)
 
print("Vārdi apgrieztā formā:", reversed_sentence)