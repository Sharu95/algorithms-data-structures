text = 'abbbaabaabaaabab'
pattern = 'aabaabaaa'
pattern_skip = [0,1,0,1,2,3,4,5,2]
pattern_long = 'acacabacacabacacac'
pattern_long_skip = [0,0,1,2,3,0,1,2,3,4,5,6,7,8,9,10,11,4]

def skip_table(pattern):
  # Create prefix/suffix table
  lookup = len(pattern)*[0]
  j, i = 0, 1

  while i < len(pattern):

    if pattern[i] is pattern[j]:
      lookup[i] = j + 1
      j += 1
      i += 1
    else: 
      nxt_j = lookup[j-1]
      
      if j is 0:
        lookup[i] = 0
        i += 1
      else:
        j = nxt_j

  return lookup

def kmp(table, text, pattern):
  j, i = 0, 0

  while i < len(text):
    
    if j is len(pattern):
      return i-j
    elif pattern[j] is text[i]:
      i += 1
      j += 1
    else:
      skip = table[j-1]
      j = skip


if __name__ == '__main__':
  lookup_table = skip_table(pattern)
  found = kmp(lookup_table, text, pattern)
  print(found)