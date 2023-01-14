from fastapi import FastAPI
from cryptography.fernet import Fernet

app = FastAPI()

users = {'juliane':{'senha': 'juliane123','email':'julyane.almeida77@gmail.com'},
        'jacqueline':{'senha':'jacqueline123','email': 'jacquelinealmeida472@gmail.com'},
        'pedro':{'senha':'pedro123','email':'pedrovictorpina@gmail.com'}}

@app.get('/', description='Essa é a nossa primeira rota.')
async def root():
    return {'mensagem':'oi'}

@app.get('/users', description='Lista de usuarios')
async def listaUsuarios():
    return {'Total de usuarios': len(users),'usuarios': users}

@app.get('/users')
async def get_user(user_id: str, description='Lista de dados de um usuario'):
    if user_id not in users:
        return 'Usuário não encontrado'
    else:
        return {f'Dados do usuario {user_id}': users[f'{user_id}']}


@app.post('/users/new', description='Cadastro de novo usuario')
async def cadastroNovoUsuario(user_id, senha, email):
    if user_id in users:
        return "Usuário já existente"
    else: 
        users[f'{user_id}'] = {'senha':senha,'email':email}
        return {f'Usuário {user_id} cadastrado com sucesso!': users[f'{user_id}']}


