import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from odnesi_app.db import get_db

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/add_company', methods=('GET', 'POST'))
def add_company():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone_number = request.form['phone_number']
        email = request.form['email']

        db = get_db()
        error = None

        if not name:
            error = 'Name is required.'
        elif not address:
            error = 'Address is required.'
        elif not phone_number:
            error = 'Phone number is required.'
        elif not email:
            error = 'Email is required.'

        if error is None:
            try:
                db.execute(
                        "INSERT INTO company (name, location, phone_number, email) VALUES (?, ?, ?, ?)",
                        (name, address, phone_number, email),
                        )
                db.commit()
            except db.IntegrityError:
                error = f"Company {name} is already registered."
            else:
                return redirect(url_for("add.add_company"))

    return render_template('add/add_company.html')

@bp.route('/add_waste', methods=('GET', 'POST'))
def add_waste():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        location = request.form['location']
        phone_number = request.form['phone_number']
        culture = request.form['culture']

        db = get_db()
        error = None

        if not name:
            error = 'Name is required.'
        elif not phone_number:
            error = 'Phone number is required.'
        elif not location:
            error = 'Location is required.'
        elif not culture:
            error = 'Culture is required.'
        elif not amount:
            error = 'Amount is required.'

        if error is None:
            try:
                db.execute(
                        "INSERT INTO waste (name, phone_number, location, culture, amount) VALUES (?, ?, ?, ?, ?)",
                        (name, phone_number, location, culture, amount),
                        )
                db.commit()
            except db.DatabaseError:
                error = f"Databas error!"
            else:
                return redirect(url_for("add.add_waste"))

    return render_template('add/add_waste.html')


