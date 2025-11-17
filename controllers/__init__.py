from flask import Blueprint

api_blueprint = Blueprint('api', __name__)

from.trainer_controller import trainer_bp
from.service_controller import service_bp
from.client_controller import client_bp
from.workout_program_controller import workout_program_bp
from.trainer_schedule_controller import trainer_schedule_bp
from.equipment_controller import equipment_bp
from.exercise_controller import exercise_bp
from.exercise_equipment_controller import exercise_equipment_bp
from.schedule_controller import schedule_bp
from.membership_controller import membership_bp
from.procedure_controller import procedure_bp

api_blueprint.register_blueprint(trainer_bp, url_prefix='/trainers')
api_blueprint.register_blueprint(service_bp, url_prefix='/services')
api_blueprint.register_blueprint(client_bp, url_prefix='/clients')
api_blueprint.register_blueprint(workout_program_bp, url_prefix='/workout-programs')
api_blueprint.register_blueprint(trainer_schedule_bp, url_prefix='/trainer-schedules')
api_blueprint.register_blueprint(equipment_bp, url_prefix='/equipment')
api_blueprint.register_blueprint(exercise_bp, url_prefix='/exercises')
api_blueprint.register_blueprint(exercise_equipment_bp, url_prefix='/exercise-equipment')
api_blueprint.register_blueprint(schedule_bp, url_prefix='/schedules')
api_blueprint.register_blueprint(membership_bp, url_prefix='/memberships')
api_blueprint.register_blueprint(procedure_bp, url_prefix='/procedures')