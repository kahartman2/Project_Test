# from dash_package import app, db
# from dash_package.db_models import *
# from flask_sqlalchemy import SQLAlchemy
# from plotly import __version__
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#
# import plotly.graph_objs as go
#
# def inf_vs_ta_ratings(): #restaurant name, mich stars, trip advisor rating, infatuation rating
#     return db.session.query(Restaurant.name, TripAdvisor.rating, Infatuation.rating).join(TripAdvisor).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()
#
# def plot_ta_ratings():
#     words = [ for word in count_key_words(shortname)]
#     counts = [word[1] for word in count_key_words(shortname)]
#     return {'x': words, 'y': counts, 'type': 'bar', 'name': shortname}
