#!usr/bin/python


class LifeGame(object):
    def __init__(self, data=[[]]):
        self.data = data

    def _get_neighbours(self, i, j):
        a = [0, 0, 0, 0]
        for k in range(i - 1, i + 2):
            for p in range(j - 1, j + 2):
                if k >= 0 and p >= 0 and k < len(self.data) and p < len(self.data[0]):
                    if k != i or p != j:
                        a[self.data[k][p]] += 1
        return a

    def get_next_generation(self):
        answer = []
        for q in range(len(self.data)):
            tmp = []
            for w in range(len(self.data[0])):
                tmp = tmp + [0]
            answer.append(tmp)
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                e = self._get_neighbours(i, j)
                if self.data[i][j] == 0:
                    if e[2] == 3:
                        answer[i][j] = 2
                    elif e[3] == 3:
                        answer[i][j] = 3
                    else:
                        answer[i][j] = 0
                if self.data[i][j] == 1:
                    answer[i][j] = 1
                if self.data[i][j] == 2:
                    if e[2] > 3 or e[2] < 2:
                        answer[i][j] = 0
                    else:
                        answer[i][j] = 2
                if self.data[i][j] == 3:
                    if e[3] > 3 or e[3] < 2:
                        answer[i][j] = 0
                    else:
                        answer[i][j] = 3
        self.data = answer
        return self.data


if __name__ == "__main__":
    board = LifeGame([[0, 2, 0], [0, 2, 0], [0, 2, 0]])
    print(board.get_next_generation())
