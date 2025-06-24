# server/controllers/episode_controller.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models import db

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([ep.to_dict() for ep in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    ep = Episode.query.get_or_404(id)
    return jsonify(ep.to_dict(with_appearances=True)), 200
    @episode_bp.route('/episodes', methods=['POST'])
@jwt_required()
def create_episode():
    data = request.get_json()
    new_episode = Episode(date=data['date'], number=data['number'])
    db.session.add(new_episode)
    db.session.commit()
    return jsonify(new_episode.to_dict()), 201


@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get_or_404(id)
    db.session.delete(ep)
    db.session.commit()
    return jsonify({'message': 'Episode deleted'}), 200

