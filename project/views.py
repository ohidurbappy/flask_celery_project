from flask import Blueprint, render_template, redirect, request

from .forms import MyForm
from .tasks import add_user

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def create_user():
    form = MyForm()

    if form.validate_on_submit():
        task = add_user.delay(form.data)
        return render_template("cancel.html", task=task)

    return render_template('form.html', form=form)

@main.route("/cancel/<task_id>")
def cancel(task_id):
    task = add_user.AsyncResult(task_id)
    task.abort()
    return "CANCELED!"

@main.route("/users")
def users():
    from .models import User
    return render_template("users.html", users=User.query.all())