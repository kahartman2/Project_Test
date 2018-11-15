from flask import render_template
from __init__ import server, app

@server.route('/nyc_restaurants')
def render_restaurants():
    return "Hello world"

# '''
#     nycrestaurant = Restaurant.query.get(1)
#     return 'nycrestaurant.name'
# '''
