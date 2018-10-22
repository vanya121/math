#!user/bin/python


def parse_color(color):
    color = ''.join(color.split())
    answer = {}
    if color[0] == '#':
        color = color.lower()
        for i in range(3):
            r = ord(color[2 * i + 2]) - ord('a') + 10
            value = (ord(color[2 * i + 1]) - ord('a') + 10) * 16 + r
            if value > 255:
                print('None')
                return
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
        for i in range(3):
            if color[i + 1][len(color[i + 1]) - 1] == '%':
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
    return total_answer


if __name__ == "__main__":
    parse_color('#AAaaaa')
    parse_color('1, 2, 30')
    parse_color('bgr(100, 22, 13)')
    parse_color('rgb(4%, 5%, 6%)')
    parse_color('rgb(1, 2, 3)')
