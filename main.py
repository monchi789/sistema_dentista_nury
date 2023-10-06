from fastapi import FastAPI
from models.usuario import Base
from models.cita import Base
from models.cita_sin_tratamiento import Base
from models.factura import Base
from models.paciente import Base
from models.pago import Base
from models.tratamiento import Base
from config.database import engine
from routes import usuario, pacientes, cita_sin_tratamiento, cita, tratamiento

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(usuario.router)
app.include_router(pacientes.router)
app.include_router(cita_sin_tratamiento.router)
app.include_router(cita.router)
app.include_router(tratamiento.router)