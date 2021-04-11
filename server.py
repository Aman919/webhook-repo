from flask import Flask, request, json, render_template
from flask_pymongo import PyMongo

from util import Update

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyscretkey'
app.config['MONGO_URI'] = "mongodb+srv://user:admin@cluster0.iao2g.mongodb.net/Sample?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
def api_root():
    return render_template('ui.html')

@app.route('/get_update')
def get_update():
    my_db = mongo.db.mydb
    data = my_db.find().limit(1).sort([("timestamp", -1)]) # It's fetch the latest data pushed to our mongoDB
    # print(data[0])
    data = Update(data[0])

    # data = {
    #     "msg": "This is just a message from the server"
    # }
    return json.dumps(data.data, default=str)

@app.route('/pull_github', methods=['POST'])
def api_gh_message():
    value = {}
    if request.headers['Content_Type'] == 'application/json':
        my_info = json.dumps(request.json)
        my_info = json.loads(my_info)
        if 'pull_request' in my_info.keys():
            value['author'] = my_info['sender']['login']
            value['timestamp'] = my_info['repository']['created_at']
            value['to_branch'] = my_info['repository']['default_branch']
            value['action'] = 'pull_request'
            print(my_info)

        elif 'pusher' in my_info.keys():
            value['author'] = my_info['sender']['login']
            value['timestamp'] = my_info['repository']['created_at']
            value['to_branch'] = my_info['repository']['default_branch']
            value['action'] = 'push_request'
     
        my_db = mongo.db.mydb
    return value


if __name__ == '__main__':
    app.run(debug=True)
