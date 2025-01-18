import os

MONGO_URI = f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PWD')}@cluster.mongodb.net/controle_despesas"
SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

n