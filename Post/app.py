from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

posts = []


@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route('/create_post', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        print(title)

        if title and content:
            posts.append({"title": title, "content": content})

            return redirect(url_for('home'))
    return render_template('create_post.html')


if __name__ == "__main__":
    app.run(debug=True)
