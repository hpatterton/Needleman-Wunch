# Needleman-Wunch
Calculate the Needleman-Wunch scoring and direction matrix

This program takes 2 sequences (protein or DNA), and applies the Needleman-Wunch algorithm to them to calculate the optimal alignment.

The two sequences are specified in the code, for example:

seq1='FMDTPLNE'

seq2='FKHMEDPLE'

The program outputs the score matrix, direction of movement matrix, and the alignment:

[0, -2, -4, -6, -8, -10, -12, -14, -16]

[-2, 1, -1, -3, -5, -7, -9, -11, -13]

[-4, -1, -1, -3, -5, -7, -9, -11, -13]

[-6, -3, -3, -3, -5, -7, -9, -11, -13]

[-8, -5, -2, -4, -5, -7, -9, -11, -13]

[-10, -7, -4, -4, -6, -7, -9, -11, -10]

[-12, -9, -6, -3, -5, -7, -9, -11, -12]

[-14, -11, -8, -5, -5, -4, -6, -8, -10]

[-16, -13, -10, -7, -7, -6, -3, -5, -7]

[-18, -15, -12, -9, -9, -8, -5, -5, -4]


['D', 'H', 'H', 'H', 'H', 'H', 'H', 'H']

['V', 'D', 'D', 'D', 'D', 'D', 'D', 'D']

['V', 'D', 'D', 'D', 'D', 'D', 'D', 'D']

['V', 'D', 'H', 'D', 'D', 'D', 'D', 'D']

['V', 'V', 'D', 'D', 'D', 'D', 'D', 'D']

['V', 'V', 'D', 'H', 'H', 'D', 'D', 'V']

['V', 'V', 'V', 'D', 'D', 'H', 'H', 'H']

['V', 'V', 'V', 'D', 'V', 'D', 'H', 'H']

['V', 'V', 'V', 'D', 'V', 'V', 'D', 'D']


F--M-DTPLNE

FKHMED-PL-E
