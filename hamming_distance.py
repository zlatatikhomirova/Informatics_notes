def hamming_distance(seq_1: str, seq_2: str) -> int: 
    distance = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            distance += 1
    return distance
  
  first_seq = ""
  second_seq = ""
  third_seq = ""
  print(hamming_distance(first_seq, second_seq) + hamming_distance(first_seq, third_seq))
  
  # если же важно то, сколько уникальных мутаций, то
  
  
