from flask import Flask, render_template, request

# Flask instance
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

@app.route('/register', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        return f"Registered: {username} with password {password}"
    return render_template("register.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)