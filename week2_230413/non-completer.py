# non-completer with hash
def solution(participant, completion):
    # create participant as a hash table
    hash_table = {}
    
    for p in participant:
        if p in hash_table:
            hash_table[p] += 1
        # create new key if p doesn't exist in hash_table
        else:
            hash_table[p] = 1
            
    # remove completion list from the hash table
    for c in completion:
        hash_table[c] -= 1
        
    # non-completer has a value of 1 in the hash table
    for answer, value in hash_table.items():
        if value == 1:
            return answer
