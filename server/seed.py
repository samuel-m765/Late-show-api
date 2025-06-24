from server.app import app  # Relative import since app.py is in the same directory
from server.models import db, User, Guest, Episode, Appearance
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create users
    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    # Create guests
    guest1 = Guest(name="John Doe", occupation="Actor")
    guest2 = Guest(name="Jane Smith", occupation="Comedian")
    db.session.add_all([guest1, guest2])

    # Create episodes
    episode1 = Episode(date=date(2025, 6, 1), number=101)
    episode2 = Episode(date=date(2025, 6, 2), number=102)
    db.session.add_all([episode1, episode2])

    # Create appearances
    appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
    appearance2 = Appearance(rating=5, guest_id=2, episode_id=1)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()