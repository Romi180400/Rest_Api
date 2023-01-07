from flask import Flask

from db_connector import getUserName

app = Flask(__name__)

@app.route('/api/users/getUser/<user_id>', methods=['GET'])
def get_user_name(user_id): 
    user_name = getUserName(user_id)    
    if user_name == None:
        return f"<H1 id='Error'> User ID not exist {user_id} </H1>"
    return f"<H1 id={user_id}>" + user_name + "</H1>"

app.run(host='127.0.0.1', debug=True, port=5001)