from app import db

# Association Table
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20), nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    hero = db.relationship("Hero", back_populates="hero_powers")
    power = db.relationship("Power", back_populates="hero_powers")

    def validate(self):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if self.strength not in valid_strengths:
            return [f"Strength must be one of {valid_strengths}"]
        return []

    def to_dict(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id
        }


class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String(50), nullable=False)

    hero_powers = db.relationship("HeroPower", back_populates="hero", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    hero_powers = db.relationship("HeroPower", back_populates="power", cascade="all, delete")

    def validate(self):
        if not self.description or len(self.description) < 20:
            return ["Description must be at least 20 characters long"]
        return []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
