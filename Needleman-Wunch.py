# scoring scheme
match = 1
mismatch = -2
shift = -2

def needleman_wunch(seq1,seq2):

	matrix_size = (len(seq1)+1,len(seq2)+1)

	# make matrix and direction matrix
	rows = [0]*matrix_size[0]
	matrix=[rows.copy() for i in range(matrix_size[1])]
	direction_rows = ['']*len(seq1)
	direction_matrix = [direction_rows.copy() for i in range(len(seq2))]

	# set up first column and row
	for i in range(matrix_size[0]):
		matrix[0][i] = i*-2
	for i in range(matrix_size[1]):
		matrix[i][0] = i * -2
	# move left->right,top->bottom, calculate max score
	for i in range(1, matrix_size[1]):
		for j in range(1, matrix_size[0]):
			if seq1[j-1] == seq2[i-1]:
				match = 1
			else:
				match = -2

			score_down = matrix[i-1][j]-2
			score_left = matrix[i][j-1]-2
			score_diagonal = matrix[i-1][j-1]+match
			score = max(score_down,score_left,score_diagonal)
			matrix[i][j] = score
			# what direction did we come from?
			# L=left, D=down,S=Sideways
			direction = 'L' if score_left > score_down else 'D'
			if direction == 'L':
				direction = 'L' if score_left > score_diagonal else 'S'
			else:
				direction = 'D' if score_down > score_diagonal else 'S'
			direction_matrix[i-1][j-1] = direction
	return matrix, direction_matrix

def align_nw(seq1, seq2, direction_matrix):
	aligned_seq1 = ''
	aligned_seq2 = ''
	i=len(seq2)-1
	j=len(seq1)-1
	# Follow the direction matrix, and add symbols to
	# aligned_seq1 and aligned_seq2
	while i>= 0 and j >=0:
		if direction_matrix[i][j] == 'D':
			aligned_seq1 += '-'
			aligned_seq2 += seq2[i]
			i -= 1
		elif direction_matrix[i][j] == 'L':
			aligned_seq1 += seq1[j]
			aligned_seq2 += '-'
			j -= 1
		else:
			aligned_seq1 += seq1[j]
			aligned_seq2 += seq2[i]
			i -= 1
			j -= 1
	# We need to reverse the aligned sequences
	alignment = aligned_seq1[::-1] + '\n' + aligned_seq2[::-1]
	return alignment

#driver code
seq1='MSRTKETARTKKTITSKKSKKASKGSDAASGVKTAQRRWRPGTVALREIRQFQRSTDLLLQKAPFQRLVREVSGAQKEGLRFQSSAILAAQEATESYIVSLLADTNRACIHSGRVTIQPKDIHLALCLRGERA'
seq2='MARTKQTARKSTGGKAPRKQLATKAARKSAPATGGVKKPHRYRPGTVALREIRRYQKSTELLIRKLPFQRLVREIAQDFKTDLRFQSSAVMALQEACEAYLVGLFEDTNLCAIHAKRVTIMPKDIQLARRIRGERA'
values,direction=needleman_wunch(seq1,seq2)
for i in range(len(seq2)+1):
	print(values[i])
for i in range(len(seq2)):
	print(direction[i])
alignment = align_nw(seq1, seq2, direction)
print(alignment)