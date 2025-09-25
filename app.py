from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Welcome App</title>
<h2>Enter your name:</h2>
<form method="post">
  <input type="text" name="username" required>
  <input type="submit" value="Submit">
</form>
{% if name %}
  <h3>Welcome, {{ name }}!</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(HTML, name=name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)