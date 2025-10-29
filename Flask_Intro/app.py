from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/circle", methods=["GET", "POST"])
def circle():
    area = None
    if request.method == "POST":
        radius = float(request.form["radius"])
        area = 3.14159 * radius * radius
    return render_template("circle.html", area=area)

@app.route("/triangle", methods=["GET", "POST"])
def triangle():
    area = None
    if request.method == "POST":
        base = float(request.form["base"])
        height = float(request.form["height"])
        area = 0.5 * base * height
    return render_template("triangle.html", area=area)

def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return " ".join(output)

@app.route("/infixpostfix", methods=["GET", "POST"])
def infixpostfix():
    result = None
    if request.method == "POST":
        infix_expr = request.form.get("infixExpr", "")
        result = infix_to_postfix(infix_expr.replace(" ", ""))  # remove spaces
    return render_template("infixpostfix.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
