from flask import Flask, render_template, request
from chatbot import Lucretia 


def execute():
    # execute, return a value if needed
    pass
bot = Lucretia
app = Flask(__name__)
userdata= {"tan" :{
    "name":"",
    "dateofbirth" :""
}}

@app.route("/") #, methods = ['GET', 'POST'])
def index():    
    execute()
    return render_template('index.html')


@app.route("/get",  methods=["POST"])
def get_bot_response():
    userText = request.form['msg'] #get data from input, we write js to index.tml
    username = request.form['username'] #get data from input, we write js to index.tml
    curentuser = userdata.get(username)
    if not curentuser :
        userdata.setdefault(username, {"name": username})
        curentuser = userdata.get(username)
    if not userText and username :
        return "Hello {}, how can I help you?".format(curentuser.get('name'))
        #return f"hi , {curentuser.get('name')}"
    while not Lucretia.make_exit(userText):
            userText = Lucretia.respond(userText)
            return userText
 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9696, debug=True)