text = 'some_text'
pattern = 'aabaabaaa'

def main():
  # Create prefix/suffix table
  lookup = len(pattern)*[0]
  lookup[0] = 0
  j, i = 0, 1

  while i < len(pattern):

    if pattern[i] is pattern[j]:
      lookup[i] = lookup[j] + 1
      j += 1
      i += 1
    else: 
      prev = lookup[j-1]
      if prev is 0:
        j = j-1
        lookup[i] = 0
        i += 1
      else:
        j = prev

    print('{} | i at: {} | j at: {}'.format(lookup, i, j))

  # print(lookup)



if __name__ == '__main__':
  main()