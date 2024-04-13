from openai import OpenAI
from flask import Flask, render_template

app = Flask(__name__)

client = OpenAI(api_key="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")

model = "gpt-3.5-turbo"

chatLog = [{"role": "system", "content": "You are a helpful therapist versed in techniques for anxiety, depression, and other mental health disorders. You are kind and helpful, using supportive language only. You should be soothing and creative. Your purpose is to suggest coping techniques and situational advice."},]

def ask_ai(
    prompt_str: str,
) -> str :

    chatLog.append({"role": "user", "content": prompt_str}) # add user input to chatlog

    response = client.chat.completions.create(
        model=model,
        messages=chatLog
    )

    response_text = response.choices[0].message.content
    chatLog.append({"role": "assistant", "content": response})

    return response_text  # returns the string message from AI


# write code here
print("Hello! I am MyMind!  How are you doing today?")

@app.route("/jsonGetInput/<prompt>")
def get_input(prompt): # gets input
    response_message = ask_ai(prompt)
    return response_message

@app.route("/jsonGetInput/")
def get_input2(): # gets input
    return "You need to provide a prompt! :("

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/script.js')
def script():
    return open("script.js").read()
"""
@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'
"""

if (__name__ == '__main__'):
    app.run()