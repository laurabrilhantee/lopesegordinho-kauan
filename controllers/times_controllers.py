from models.times_models import Times
from db import db
import json
from flask import make_response

def get_times():
    times = Times.query.all()
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de times.',
            'dados': [times.json() for times in Times]
        }, ensure_ascíí=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def create_times(times_data):
    if not all(key in times_data for key in ['Título', 'Gênero', 'Desenvolvidor', 'Plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Título, Gênero, Desenvolvidor e Plataforma são obrigatórios.'}, ensure_ascíí=False),
            400
        )
        response.headers['Content.Type']= 'application/json'
        return response
    
    novo_times = Times(
        id =times_data['id'],  
        Titulo=times_data['Titulo'],  
        Genero=times_data['Genero'],    
        Desenvolvidor=times_data['Duracao'],
        Plataforma=times_data['lancamento'],
    )
    db.session.add(novo_times)
    db.session.commit()
    response = make_response(
        json.dumps({  
            'mensagem': 'Time cadastrado com sucesso.',  
            'times': novo_times.json()  
        },ensure_ascii=False, sort_keys=False)  
    )
    response.headers['content-Type'] = 'application/json'
    return response

def get_time_by_id(times_id):
    time = Times.query.get(times_id)  # Busca o carro pelo ID

    if time:  # Verifica se o carro foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'Time encontrado.',
                'dados': time.json()  # Converte os dados do carro para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        # Se o carro não for encontrado, retorna erro com código 404
        response = make_response(
            json.dumps({'mensagem': 'Time não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

# Função para criar um novo carro
def create_time(time_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in time_data for key in ['Titulo', 'Genero', 'desenvolvedor', 'Plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, genero, desenvolvedore plataforma são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    # Se os dados forem válidos, cria o novo carro
    novo_times = Times(
        id =time_data['id'],  
        Titulo=time_data['Titulo'],  
        Genero=time_data['Genero'],    
        Desenvolvedor=time_data['Desenvolvedor'],
        Plataforma=time_data['plataforma']
    )
    
    db.session.add(novo_times)  # Adiciona o novo carro ao banco de dados
    db.session.commit()  # Confirma a transação no banco

    # Resposta de sucesso com os dados do novo carro
    response = make_response(
        json.dumps({
            'mensagem': 'Time cadastrado com sucesso.',
            'carro': novo_times.json()  # Retorna os dados do carro cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

def update_times(time_id, time_data):
    time = time.query.get(time_id)

    if not time:
        response = make_response(
            json.dumps({'mensegem': 'Time não encontrado'}, ensure_ascii=False),
            404
        )
        response.headerst['Ccontent-Type'] = 'applicattion/json'
        return response
    
    if not all(key in time_data for key in ['titulo', 'genero', 'desenvolvidor', 'Plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, genero, desenvolvidor e plataforma são obrigatórios'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response 
    
    time.titulo = time_data['titulo']
    time.genero = time_data['genero']
    time.desenvoldor = time_data['desenvolvedor']
    time.plataform = time_data['plataforma']


    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Time atualizado com sucesso.',
            'Times': time.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response
