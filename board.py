import piece

class Board():

    def __init__(self):


        self.board = []


        # Board set-up
        for i in range(9):
            self.board.append([None] * 9)
        # White
        self.board[8][0] = piece.a(True)
        self.board[8][1] = piece.b(True)
        self.board[8][2] = piece.c(True)
        self.board[8][3] = piece.d(True)
        self.board[8][4] = piece.e(True)
        self.board[8][5] = piece.f(True)
        self.board[8][6] = piece.g(True)
        self.board[8][7] = piece.h(True)
        self.board[0][8] = piece.a8(True)
        self.board[1][8] = piece.a7(True)
        self.board[2][8] = piece.a6(True)
        self.board[3][8] = piece.a5(True)
        self.board[4][8] = piece.a4(True)
        self.board[5][8] = piece.a3(True)
        self.board[6][8] = piece.a2(True)
        self.board[7][8] = piece.a1(True)
        self.board[7][0] = piece.Rook(True)
        self.board[7][1] = piece.Knight(True)
        self.board[7][2] = piece.Bishop(True)
        self.board[7][3] = piece.Queen(True)
        self.board[7][4] = piece.King(True)
        self.board[7][5] = piece.Bishop(True)
        self.board[7][6] = piece.Knight(True)
        self.board[7][7] = piece.Rook(True)
        #self.board[0][8] = piece.a1(True)

        for i in range(8):
            self.board[6][i] = piece.Pawn(True)

        # Black

        self.board[0][0] = piece.Rook(False)
        self.board[0][1] = piece.Knight(False)
        self.board[0][2] = piece.Bishop(False)
        self.board[0][3] = piece.Queen(False)
        self.board[0][4] = piece.King(False)
        self.board[0][5] = piece.Bishop(False)
        self.board[0][6] = piece.Knight(False)
        self.board[0][7] = piece.Rook(False)

        for i in range(8):
            self.board[1][i] = piece.Pawn(False)


    def print_board(self):

        #print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")

        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)
        for i in range(len(self.board)):
            tmp_str = "|"
            for j in self.board[i]:
                if j == None or j.name == 'GP':
                    tmp_str += "   |"
                elif len(j.name) == 2:
                    tmp_str += (" " + str(j) + "|")
                else:
                    tmp_str += (" " + str(j) + " |")
            print(tmp_str)
        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)


