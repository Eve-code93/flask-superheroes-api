from app import create_app, db
from app.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")

    p1 = Power(name="super strength", description="gives the wielder super-human strengths")
    p2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")

    hp1 = HeroPower(strength="Strong", hero=h1, power=p1)
    hp2 = HeroPower(strength="Weak", hero=h2, power=p2)

    db.session.add_all([h1, h2, p1, p2, hp1, hp2])
    db.session.commit()
