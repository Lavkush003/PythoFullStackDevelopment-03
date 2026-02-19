
from flask import Blueprint, render_template, redirect, url_for, flash
from .models import db, Todo
from .forms import TodoForm

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    form = TodoForm()

    if form.validate_on_submit():
        new_task = Todo(task=form.task.data)
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect(url_for("main.index"))

    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template("index.html", todos=todos, form=form)


@main.route("/delete/<int:id>")
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted!", "danger")
    return redirect(url_for("main.index"))


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    task = Todo.query.get_or_404(id)
    form = TodoForm(obj=task)

    if form.validate_on_submit():
        task.task = form.task.data
        db.session.commit()
        flash("Task updated!", "info")
        return redirect(url_for("main.index"))

    return render_template("edit.html", form=form)


@main.route("/toggle/<int:id>")
def toggle(id):
    task = Todo.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    flash("Task status updated!", "warning")
    return redirect(url_for("main.index"))
