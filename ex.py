from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

trainer = ChatBot('MyChatBot')
trainer.train(ListTrainer)

conversation = open('chats.txt', 'r').readlines()

trainer.train(conversation)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = trainer.get_response(message)
    print('ChatBot:', reply)
    if message.strip() == 'Bye':
        print('ChatBot:Bye')
        break



'''trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")'''