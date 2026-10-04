from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

urlBanco = "postgresql://kopke:848561@localhost:5432/rodrigokopke"
nova_urlBanco = "postgresql://kopke:848561@localhost:5432/rodrigokopke"

engine = create_engine(urlBanco)
_engine = create_engine(urlBanco)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def conexao():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def testeConexao():
    try:
        gen = conexao()
        db = next(gen)
        db.execute(text("SELECT 1"))
        print("Conexão funcionando!")
    except Exception as e:
        print(f"Erro ao conectar: {e}")

testeConexao()

