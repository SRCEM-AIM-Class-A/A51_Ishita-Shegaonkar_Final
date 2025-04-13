from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Route 1: Home page
@app.route('/')
def home():
    return '''
        <h1>Hello, World!</h1>
        <p>Click <a href="/form">here</a> to enter your name and age.</p>
    '''

# Route 2: Form page
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        # Basic error handling
        if not name or not age:
            return "Error: Please provide both name and age."
        try:
            age = int(age)
            if age < 0:
                return "Error: Age cannot be negative."
        except ValueError:
            return "Error: Age must be a number."

        return f"Hello, {name}! You are {age} years old."

    # Form Template
    return render_template_string('''
        <h2>Enter your Name and Age</h2>
        <form method="POST">
            Name: <input type="text" name="name"><br><br>
            Age: <input type="text" name="age"><br><br>
            <input type="submit" value="Submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
