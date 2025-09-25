from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
<head>
    <title>SHA256 Hasher</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h2>SHA256 Hash Generator</h2>
    <form method="POST">
        <label for="password">Password gir:</label><br>
        <input type="text" id="password" name="password" style="width: 300px; padding: 5px;" required>
        <br><br>
        <input type="submit" value="Hash">
    </form>

    {% if password %}
        <p><b>Password:</b> {{ password }}</p>
        <p><b>SHA256 Hash:</b> {{ hashed }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    hashed_password = None

    if request.method == 'POST':
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return render_template_string(template, password=password, hashed=hashed_password)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)