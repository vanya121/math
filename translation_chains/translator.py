ANS_SIMPLE = {
    "be": 1, "ceb": 1, "de": 1, "el": 1, "en": 1, "eo": 1,
    "es": 1, "et": 1, "eu": 1, "he": 1, "ne": 1, "te": 1
}  # text: 'Добро пожаловать'

ANS_COMPLEX = {'be': 2, 'ceb': 6, 'de': 'too much', 'el': 3, 'en': 3, 'eo': 'too much', 'es': 3, 'et': 'too much',
               'eu': 7, 'he': 4, 'ne': 3,
               'te': 'too much'}  # text: 'Сюда пришли люди, которым было приятнее быть друг с другом, чем порознь, которые терпеть не могли всякого рода воскресений, потому что в воскресенье им было скучно. Маги, Люди с большой буквы, и девизом их было -- "Понедельник начинается в субботу". Они были магами потому, что очень много знали, так много, что количество перешло у них наконец в качество, и они стали с миром в другие отношения, нежели обычные люди. Они работали в институте, который занимался прежде всего проблемами человеческого счастья и смысла человеческой жизни, но даже среди них никто точно не знал, что такое счастье и в чем именно смысл жизни. И они приняли рабочую гипотезу, что счастье в непрерывном познании неизвестного и смысл жизни в том же. Каждый человек -- маг в душе, но он становится магом только тогда, когда начинает меньше думать о себе и больше о других, когда работать ему становится интереснее, чем развлекаться в старинном смысле этого слова.'

# from requests import post
# ADRESS = "https://translate.yandex.net/api/v1.5/tr.json/translate"
# KEY = "trnsl.1.1.20181119T111406Z.a5b1d67a65c3dc89.40706e5909402ac9569e57e63bffcef1fbd54786"
# l = ["be", "ceb", "de", "el", "en", "eo", "es", "et", "eu", "he", "ne", "te"]
# a = {}
# import json
# for elem in l:
#     params = {
#         "key": KEY,
#         "text": 'Сюда пришли люди, которым было приятнее быть друг с другом, чем порознь, которые терпеть не могли всякого рода воскресений, потому что в воскресенье им было скучно. Маги, Люди с большой буквы, и девизом их было -- "Понедельник начинается в субботу". Они были магами потому, что очень много знали, так много, что количество перешло у них наконец в качество, и они стали с миром в другие отношения, нежели обычные люди. Они работали в институте, который занимался прежде всего проблемами человеческого счастья и смысла человеческой жизни, но даже среди них никто точно не знал, что такое счастье и в чем именно смысл жизни. И они приняли рабочую гипотезу, что счастье в непрерывном познании неизвестного и смысл жизни в том же. Каждый человек -- маг в душе, но он становится магом только тогда, когда начинает меньше думать о себе и больше о других, когда работать ему становится интереснее, чем развлекаться в старинном смысле этого слова.',
#         "lang": "ru-" + elem,
#         "format": "plain"
#      }
#     i = 0
#     prev = params["text"]
#     while i != 8:
#         i += 1
#         answer = post(ADRESS, data = params)
#         answer = answer.json()
# #         print(answer['text'][0])
#         params["lang"] = elem + "-ru"
#         params["text"] = answer["text"][0]
#         next_answer = post(ADRESS, data = params)
#         next_answer = next_answer.json()
# #         print(next_answer['text'][0])
#         if next_answer['text'][0] == prev:
#             print(prev)
#             a[elem] = i
#             i = 8
#         else:
#             if i == 8:
#                 a[elem] = 'too much'
#         params["lang"] = "ru-" + elem
#         params["text"] = next_answer["text"][0]
#         prev = next_answer['text'][0]
# print(a)