from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import folium

from odnesi_app.db import get_db

bp = Blueprint('map', __name__, url_prefix='/map')

@bp.route('')
def map():
    db = get_db()
    waste = db.execute(
        'SELECT name, location, phone_number, culture, amount FROM waste;'
    ).fetchall()

    folium_map = folium.Map(location=[44.817778, 20.456944], zoom_start=10)

    for w in waste:
        n, e = w['location'].split(', ')
        folium.Marker(
            location=[n, e],
            popup=w['name'] + '; ' + w['phone_number'] + '; ' + w['culture'] + '; ' + w['amount'],
        ).add_to(folium_map)

    return folium_map._repr_html_()


