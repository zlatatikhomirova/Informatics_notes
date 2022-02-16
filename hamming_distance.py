def hamming_distance(seq_1: str, seq_2: str) -> int: 
    distance = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            distance += 1
    return distance

def hamming_distance_unique(seq_1: str, seq_2: str, seq_3: str) -> int:
	def hamming_distance_how_diffs(seq_1: str, seq_2: str) -> int:
	    distance_how = [0, []]
	    for i in range(len(seq_1)):
	        if seq_1[i] != seq_2[i]:
	            distance_how[0] += 1
	            distance_how[1] += [(i, seq_1[i], seq_2[i])]
	    return distance_how
	distance_how_seq_2 = hamming_distance_how_diffs(seq_1, seq_2)
	distance_how_seq_3 = hamming_distance_how_diffs(seq_1, seq_3)
	n = max( len(distance_how_seq_2[1]), len(distance_how_seq_3[1]) )
	cnt = 0
	for i in range(n):
	    try:
	        if distance_how_seq_2[1][i] == distance_how_seq_3[1][i]:
	            cnt += 1
	    except IndexError:
	        break
	return distance_how_seq_2[0] + distance_how_seq_3[0] - cnt

def hamming_distance_triplet(seq_1: list, seq_2: list) -> int: 
    distance = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            distance += 1
    return distance

def hamming_distance_triplet_unique(seq_1: list, seq_2: list, seq_3: list) -> int:
	def hamming_distance_how_diffs(seq_1: list, seq_2: list) -> int:
	    distance_how = [0, []]
	    for i in range(len(seq_1)):
	        if seq_1[i] != seq_2[i]:
	            distance_how[0] += 1
	            distance_how[1] += [(i, seq_1[i], seq_2[i])]
	    return distance_how
	distance_how_seq_2 = hamming_distance_how_diffs(seq_1, seq_2)
	distance_how_seq_3 = hamming_distance_how_diffs(seq_1, seq_3)
	n = max( len(distance_how_seq_2[1]), len(distance_how_seq_3[1]) )
	cnt = 0
	for i in range(n):
	    try:
	        if distance_how_seq_2[1][i] == distance_how_seq_3[1][i]:
	            cnt += 1
	    except IndexError:
	        break
	return distance_how_seq_2[0] + distance_how_seq_3[0] - cnt


triplet_like_1_seq = "АТЦ АЦА ГТА ГТА ГТТ ГЦТ ГГА ААГ АГА ААТ АТЦ АЦА"
triplet_like_2_seq = "АТЦ ЦАТ ГТА ГТА АТА ГЦТ ГГА АТГ АГА АЦТ АТЦ ЦАТ"
triplet_like_3_seq = "АЦТ АЦТ ГТГ ГАА ГТА ГЦТ ГГЦ ААГ АГА ААТ АЦТ АЦТ"
	
first_seq = "".join(triplet_like_1_seq.split())
second_seq = "".join(triplet_like_1_seq.split())
third_seq = "".join(triplet_like_1_seq.split())
print(first_seq, second_seq, trird_seq, sep='\n')
print("Всего мутаций (подсчет по нуклеотидам): ", hamming_distance(first_seq, second_seq) + hamming_distance(first_seq, third_seq))
print("Уникальных мутаций (подсчет по нуклеотидам): ", hamming_distance(first_seq, second_seq, third_seq))
print("Всего мутаций (подсчет по триплетам): ", hamming_distance(triplet_like_1_seq.split(),
								 triplet_like_2_seq.split()) + hamming_distance(triplet_like_1_seq.split(),
														triplet_like_3_seq.split()))
print("Уникальных мутаций (подсчет по триплетам): ", hamming_distance(triplet_like_1_seq.split(), triplet_like_2_seq.split(), triplet_like_3_seq.split()))

# Вариант функции hamming_distance_unique не являющийся эффективным:
# def hamming_distance_unique(seq_1: str, seq_2: str, seq_3: str) -> int:
# 	def hamming_distance_how_diffs(seq_1: str, seq_2: str) -> int:
# 	    distance_how = []
# 	    for i in range(len(seq_1)):
# 	        if seq_1[i] != seq_2[i]:
# 	            distance_how += [(i, seq_1[i], seq_2[i])]
# 	    return distance_how
# 	distance_how_seq_2 = hamming_distance_how_diffs(seq_1, seq_2)
# 	distance_how_seq_3 = hamming_distance_how_diffs(seq_1, seq_3)
# 	n = max( len(distance_how_seq_2), len(distance_how_seq_3) )
# 	cnt = 0
# 	for i in range(n):
# 	    try:
# 	        if distance_how_seq_2[i] != distance_how_seq_3[i]:
# 	            cnt += 2
# 	        else:
# 	            cnt += 1
# 	    except IndexError:
# 	        cnt += n-i-1
# 	        break
# 	return (cnt, distance_how_seq_2[0], distance_how_seq_3[0])
