from flask import Blueprint, request, jsonify
from app import db
from app.models import Hero, Power, HeroPower

bp = Blueprint('bp', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "API is working!"}), 200

@bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_list = [hero.to_dict() for hero in heroes]
    return jsonify(heroes_list), 200

@bp.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    hero_data = hero.to_dict()
    hero_data['hero_powers'] = [
        {
            "id": hp.id,
            "hero_id": hp.hero_id,
            "power_id": hp.power_id,
            "strength": hp.strength,
            "power": hp.power.to_dict()
        }
        for hp in hero.hero_powers
    ]

    return jsonify(hero_data), 200

@bp.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_list = [power.to_dict() for power in powers]
    return jsonify(powers_list), 200

@bp.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

@bp.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    power.description = data.get('description', power.description)
    errors = power.validate()

    if errors:
        return jsonify({"errors": errors}), 400

    db.session.commit()
    return jsonify(power.to_dict()), 200

@bp.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["Invalid hero_id or power_id"]}), 400

    hero_power = HeroPower(strength=strength, hero=hero, power=power)
    errors = hero_power.validate()

    if errors:
        return jsonify({"errors": errors}), 400

    db.session.add(hero_power)
    db.session.commit()

    response_data = {
        "id": hero_power.id,
        "hero_id": hero_power.hero_id,
        "power_id": hero_power.power_id,
        "strength": hero_power.strength,
        "hero": hero.to_dict(),
        "power": power.to_dict()
    }

    return jsonify(response_data), 201
