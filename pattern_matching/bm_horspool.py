text = 'manofbanbananaam'
pattern = 'banana'

def skip_table(pattern):

  alphabet, table = set(pattern), {}
  pat_rev = pattern[::-1]

  # Originally, the number of skips is:
    # length of pattern - first occurence of symbol from end of pattern - 1
  # Which is equivalent to:
    # reversing the pattern and
    # finding the index of the next to last symbol and + 1

  for symbol in alphabet:
    skips = pat_rev[1:].index(symbol) + 1
    table[symbol] = skips
  
  return table


def bm_horspool(table, text, pattern):
  j = len(pattern) - 1
  i = j
  alphabet = table.keys()

  while i < len(text):
    
    if j is 0:
      return 'Found {} between {}-{}'.format(pattern, i, i+len(pattern)-1)
    elif text[i] is pattern[j]:
      i -= 1
      j -= 1
    else:
      if not text[i] in alphabet:
        i += len(pattern) 
      else: 
        i += table[text[i]] - 1

  return '\'{}\' not found'.format(pattern)

if __name__ == '__main__':
  skip_table = skip_table(pattern)
  found = bm_horspool(skip_table, text, pattern)
  print(found)