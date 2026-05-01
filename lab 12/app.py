from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    if request.method == 'POST':
        user_id = int(request.form.get('id'))

        # check duplicate ID
        if any(u['id'] == user_id for u in users):
            error = f"ID {user_id} already exists!"
        else:
            users.append({
                "id": user_id,
                "name": request.form.get('name'),
                "surname": request.form.get('surname'),
                "email": request.form.get('email')
            })
            return redirect(url_for('index'))

    return render_template('index.html', users=users, page_type='home', error=error)


@app.route('/student/<int:student_id>')
def student_page(student_id):
    user = next((u for u in users if u['id'] == student_id), None)

    if user:
        return render_template('index.html', user=user, page_type='student')

    return "Student not found", 404


if __name__ == '__main__':
    app.run(debug=True)