import telebot
import time
import random
places = []

placesAtrib = {'Тайланд' : {'море','жарко','кравсво','природа','зелень'},
'Швейцарию' : {'горы','холодно','кравсво','снег','природа','лыжи',},
'Болгарию' : {'море','жарко','кравсво','недорого'},
'Францию' : {'достопримечательности','жарко','кравсво','развлечения'},
'Испанию' : {'море','жарко','кравсво','зелень','природа','достопримечательности'},
'США' : {'океан','достопримечательности','кравсво','развлечения','',''},
'Италию' : {'море','жарко','кравсво','океан'},
'ЮАР' : {'океан','екстрим','кравсво','природа'},
'Канаду' : {'тепло','океан','кравсво','природа'},}

atributs = {'развле':'развлечения','мор':'море','сне':'снег','холод':'холодно','крас':'красиво','жар':'жарко','лыж':'лыжи','недорого':'недорого','дешев':'недорого','зелен':'зеленнь','тепло':'тепло','нежарко':'тепло','океан':'океан'}

randAns = ['Не понимаю о чем ты','Не знаю что и сказать','Что ты имеешь ввиду?','Всмысле?','Ты привильно написал?']
welcome = {'привет','здарова','хай','yo','здравствуйте','привет,','здарова,','хай,','yo,','здравствуйте,','/start'}
task = {'выбрать','определить','определим','определиться','мне','куда','поехать','могу','отдохнуть','путешествовать','место','страну','',}
Task = {'я','хочу','поехать','туда','где','есть','полетель','на','в','чтобы','что','бы','',}
what = {'что','ты','можешь','умеешь','help','me','','',}
item = []
Items = set()

text = ''
textCopy = ''
textTalk = []




TOKEN = '739566714:AAHxBkWwhWa_NH76DQtFkvGSTiCl9uRrGIU'




def listener(messages):
	textWords = set()
	textOut = ''
	for m in messages:
		chatid = m.chat.id
		if m.content_type == 'text':
			text = m.text
			text = text.lower()
			textTalk = text.replace('.', '').split()
			for word in textTalk:
				textWords.add(word)



			if welcome.isdisjoint(textWords) == False:
				textOut = textOut + 'Привет'
				if len(task.intersection(textWords)) >= 3:
					textOut = textOut + ', давай определим что ты хочешь'
			elif len(task.intersection(textWords)) >= 3:
				textOut = textOut + 'Давай определим что ты хочешь'
			elif len(Task.intersection(textWords)) >= 2:
				print(textWords)
				#textWords.difference(Task)
				#atributs = list(textWords.difference(Task))
				textOut = decision(text)
			elif len(what.intersection(textWords)) >= 2 or textWords == '/help':
				textOut = 'Я могу помочь вам определить место для отдыха, для этого скажите мне что вы хотите'

			else:
				textOut = random.choice(randAns)
			tb.send_message(chatid, textOut)
			textWords.clear()


def decision(textCopy):
	atr = None
	atrs = ''
	i = 0
	name = ''
	outStr = ''
	texto = ''
	for k,v in atributs.items():
		if textCopy.find(k) >= 0:
			Items.add(v)
	if len(Items) != 0:
		print('items     ', Items)
		for k,v in placesAtrib.items():
			if Items.isdisjoint(v) == False:
				if i == len(Items.intersection(v)):
					i = len(Items.intersection(v))
					atr = list(Items.intersection(v))
					name = k
					print('atr           ', atr)
					for a in atr:
						atrs += a + ', '
						print('atrs              ',atrs)
					texto += name + ': там ' + atrs + ';\n'
					atrs = ''
				elif i < len(Items.intersection(v)):
					texto = ''
					i = len(Items.intersection(v))
					atr = list(Items.intersection(v))
					name = k
					print('atr           ', atr)
					for a in atr:
						atrs += a + ', '
						print('atrs              ',atrs)
					texto += name + ': там ' + atrs + ';\n'
					atrs = ''
		outStr = 'Могу посоветовать поехать в:\n ' + texto + 'думаю вам понравиться'
		Items.clear()
	else:
		outStr = 'Что именно ты хочешь?'

	return outStr


tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
tb.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
tb.polling(interval=3)



