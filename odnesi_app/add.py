import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/add_company', methods=('GET', 'POST'))
def add_company():
    pass

@bp.route('/add_waste', methods=('GET', 'POST'))
def add_waste():
    pass


