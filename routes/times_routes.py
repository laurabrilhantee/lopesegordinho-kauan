from flask import Blueprint, request  
from controllers.times_controllers import get_times, create_times, update_times, get_time_by_id 

# Define um Blueprint para as rotas de "Carro"
times_routes = Blueprint('time_routes', __name__)  

# Rota para listar todos os carros (GET)
@times_routes.route('/Time', methods=['GET'])
def times_get():
    return get_times()

# Rota para buscar um carro pelo ID (GET)
@times_routes.route('/Time/<int:time_id>', methods=['GET'])
def time_get_by_id(time_id):
    return get_time_by_id(time_id)

# Rota para criar um novo carro (POST)
@times_routes.route('/Time', methods=['POST'])
def times_post():
    return create_times(request.json)

@times_routes.route('/Time/<int:time_id>', methods=['PUT'])
def times_put(times_id):
    times_data = request.json 
    return update_times(times_id, times_data)