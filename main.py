import json
from flask import Flask, jsonify,request, render_template,redirect,flash
app = Flask(__name__)
app.secret_key = "super_secret_key_123123"
jsnfile = 'userlist.json'
### List User Details ###########
@app.route('/')
def main():
    with open(jsnfile) as usr:
        users = json.load(usr)
    return render_template("userlist.html", user_details = users)
### Add User Detail #############
@app.route('/addUser',methods=['GET', 'POST'])
def addUser():
    if request.method == 'GET':
        return render_template("adduser.html", user = {})
    if request.method == 'POST':
        id = request.form["id"]
        user = request.form["user"]
        number = request.form["number"]
        with open(jsnfile) as cr:
            user_info = json.load(cr)
        user_info.append({"id": id, "user": user, "number": number})
        with open(jsnfile, 'w') as cw:
            json.dump(user_info, cw)
        flash("Saved the user details !!!")
        return redirect('/addUser')

### Edit User Number #############
@app.route('/updateuser/<string:id>',methods = ['GET','POST'])
def updateuser(id):
    with open(jsnfile) as ur:
        users = json.load(ur)
    if request.method == 'GET':
        user = [x for x in users if x['id'] == id][0]
        return render_template("adduser.html", user = user)
    if request.method == 'POST':
        for user in users:
            if(user['id'] == id):
                user['user'] = request.form["user"]
                user['number'] = request.form["number"]
                break
        with open(jsnfile, 'w') as cw:
            json.dump(users, cw)
        flash("Success!!!")
        return redirect(request.referrer)

if __name__ == "__main__":

	app.run()

