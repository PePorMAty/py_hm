""" 20 """
rus = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЁЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ШЭЮ',
    10: 'ФЩЪ'
}
eng = {
	1: 'AEIOULNSTR',
  2: 'DG',
  3: 'BCMP',
  4: 'FHVWY',
  5: 'K',
  8: 'JZ',
  10: 'QZ'
}

n = int(input('Введите 0 для игры на русской раскладке или 1 для английской: '))
word = input('Введите слово: ').upper()
if n == 1:
	print('За это слово вы получаете', sum(
		[k for i in word for k, v in eng.items() if i in v]), 'очков')
elif n == 0:
	print('За это слово вы получаете', sum(
		[k for i in word for k, v in rus.items() if i in v]), 'очков')
else:
    print('Ой, похоже вы играете не по правилам, попробуйте еще раз!')
