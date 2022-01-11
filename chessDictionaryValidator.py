# chessDictionaryValidator.py 
# write a function nameed isValidChessBoard() that takes a dictionary argument and returns True or False if board is valid
# valid board: 
# 	exactly one black king and one white king
#	each player will have at most 16 pieces, at most 8 pawns, all pieces must be on valid space from 
#   	'1a' to '8h'; that is, a piece can't be on space '9z' etc.
# 	piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn','knight',
#		'bishop', 'rook', 'queen', or 'king'
#	function should detect when a bug has resulted in an improper chess board

def isValidChessBoard(board, standardBoard, standardPieces):
	valid = True
	wPieceCounter = 0
	bPieceCounter = 0
	piecesAmount = [] # i need to get the amount of values in the board dictionary
	pawnPiecesAmount = []
	# go through all the keys/values of dict and determine if they adhere to game rules
	for k,v in board.items():
		if k not in standardBoard.keys():
			valid = False
		elif v not in standardPieces:
			valid = False
		elif v == '':
			pawnPiecesAmount.append(v)
		elif v != '':
			piecesAmount.append(v)
		elif v[0] == w:
			wPieceCounter += 1
		elif v[0] == b:
			bPieceCounter += 1

	# check the amount of pieces on the board
	for i in range(len(piecesAmount)):
		if i > 32 or i < 0:
			valid = False
	
	for j in range(len(pawnPiecesAmount)):
		if j > 16 or j < 0:
			valid = False

	# check the amount of pieces per player
	if wPieceCounter>8 or wPieceCounter<0:
		valid = False
	elif bPieceCounter>8 or bPieceCounter<0:
		valid = False

	return valid

def createChessBoard():
	chessBoard = {}

	pieces = []
	piecesAmount = 16
	pawnsAmount = 8
	pieceNames = ['king','queen','bishop','knight','rook','pawn']
	pieceColors = ['w','b']

	tiles = []
	tileLetters = ['a','b','c','d','e','f','g','h']
	tileNumbers = ['1','2','3','4','5','6','7','8']

	# create the spaces where the pieces will be
	for x in tileLetters:
		for y in tileNumbers:
			tiles.append(y+x)

	# create the chess board for the pieces to lie on 
	for i in tiles:
		chessBoard.setdefault(i,'')
		
	# create the pieces for the chessboard
	for pc in pieceColors:
		for pn in pieceNames:
			pieces.append(pc+pn)
	pieces.append('') # to account for pawns

	return chessBoard,pieces

chessBoard,pieces = createChessBoard()
testChessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '5c':'wrook', '2d':'wpawn','3d':'wpawn','4d':'wpawn','5d':'wpawn','6d':'wpawn','7d':'wpawn','7d':'wpawn','7d':'wpawn','7d':'wpawn'}
result = isValidChessBoard(testChessBoard,chessBoard,pieces)
print(result)

# lets create a dictionary so that we have a base one to compare to, to validate the new dictionary
# 	(if new dictionary has values outside of base chess dicitionary, the board is wrong)