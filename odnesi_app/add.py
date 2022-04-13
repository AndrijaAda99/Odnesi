import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from odnesi_app.db import get_db

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/add_company', methods=('GET', 'POST'))
def add_company():
    return render_template('add/add_company.html')

@bp.route('/add_waste', methods=('GET', 'POST'))
def add_waste():
    return render_template('add/add_waste.html')


