from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")
trainer = ListTrainer(english_bot)

trainer.train([
    "Hi",
    "hi",
    "Are you looking to vote",
    "<a href=\"https://www.w3schools.com\">Visit W3Schools.com!</a>",
    "Do you want the status of the candidate: ",
    "Y",
    "please enter the candidate adhar number",
    "no",
    "thankyou"

])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
