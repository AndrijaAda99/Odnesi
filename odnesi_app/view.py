from tracemalloc import start
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from odnesi_app.db import get_db


bp = Blueprint('view', __name__)

@bp.route('/')
def index():
    db = get_db()

    companies = db.execute(
        'SELECT name, location, email, phone_number FROM company;'
    ).fetchall()

    wastes = db.execute(
        'SELECT name, location, culture, amount, phone_number FROM waste;'
    ).fetchall()

    return render_template('view.html',
                           companies=companies,
                           wastes=wastes)
