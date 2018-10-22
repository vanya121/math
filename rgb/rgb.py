#!user/bin/python


def parse_color(color):
    try:
        color = ''.join(color.split())
        answer = {}
        if color[0] == r'#':
            color = color.lower()
            for i in range(6):
                if color[i + 1] > 'f' or color[i + 1] < 'a':
                    return None
            for i in range(3):
                r = ord(color[2 * i + 2]) - ord('a') + 10
                value = (ord(color[2 * i + 1]) - ord('a') + 10) * 16 + r
                if value > 255:
                    return None
                if i == 0:
                    answer['r'] = value
                if i == 1:
                    answer['g'] = value
                if i == 2:
                    answer['b'] = value
        elif '0' <= color[0] and '9' >= color[0]:
                color = color.split(',')
                color = list(map(int, color))
                answer['r'] = color[0]
                answer['g'] = color[1]
                answer['b'] = color[2]
        else:
            color = ''.join(color.split(')'))
            color = ','.join(color.split('('))
            color = color.split(',')
            ans = []
            kl = 0
            for i in range(3):
                if color[i + 1][len(color[i + 1]) - 1] == r'%':
                    kl = 1
            if kl == 1:
                if color[1][len(color[1]) - 1] != r'%':
                    return None
                if color[2][len(color[2]) - 1] != r'%':
                    return None
                if color[3][len(color[3]) - 1] != r'%':
                    return None
            for i in range(3):
                if color[i + 1][len(color[i + 1]) - 1] == r'%':
                    color[i + 1] = color[i + 1][:-1]
                    ans.append(int(color[i + 1]) * 255 // 100)
                else:
                    ans.append(int(color[i + 1]))
            answer[color[0][0]] = ans[0]
            answer[color[0][1]] = ans[1]
            answer[color[0][2]] = ans[2]
        total_answer = []
        total_answer.append(answer['r'])
        total_answer.append(answer['g'])
        total_answer.append(answer['b'])
        for i in range(3):
            if total_answer[i] < 0 or total_answer[i] > 255:
                return None
        return total_answer
    except Exception:
        return None


if __name__ == "__main__":
    print([parse_color('#Abaaaa'),
    parse_color('1as, 2, 30'),
    parse_color('bgr(-1, 22, 13)'),
    parse_color('rgb(4%, 5%, 100)'),
    parse_color('rgb(1, 2, 3)')])
