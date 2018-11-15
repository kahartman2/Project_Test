from sqlalchemy import create_engine, func
from db_models import Restaurant, TripAdvisor, Infatuation
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

engine = create_engine('sqlite:///nyc_restaurants.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def rating_comparison(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    q = session.query(Restaurant.name, Infatuation.rating, TripAdvisor.rating).join(TripAdvisor).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()
    return {'text': [i[0] for i in q], 'x':[i[1] for i in q], 'y':[i[2] for i in q]}
