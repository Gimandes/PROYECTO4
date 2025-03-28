from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://productos_ur68_user:69BokNJojw26p6mOriu66QJ09RAFBG4E@dpg-cvibd9qdbo4c73atmpog-a.oregon-postgres.render.com/productos_ur68"
    SECRET_KEY = 'tu_clave_secreta'

