from sqlmodel import create_engine

connection_string = "postgresql://postgres:postgres@postgres:5432/postgres"

engine = create_engine(connection_string)
