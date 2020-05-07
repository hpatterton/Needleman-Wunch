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

#driver code
seq1='FMDTPLNE'
seq2='FKHMEDPLE'
values,direction=needleman_wunch(seq1,seq2)
for i in range(len(seq2)+1):
	print(values[i])
for i in range(len(seq2)):
	print(direction[i])