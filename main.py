from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.usuario import Base
from models.cita import Base
from models.cita_sin_tratamiento import Base
from models.factura import Base
from models.paciente import Base
from models.pago import Base
from models.tratamiento import Base
from config.database import engine
from routes import usuario, pacientes, cita_sin_tratamiento, cita, tratamiento, factura, token, admin, contrasena

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(usuario.router)
app.include_router(pacientes.router)
app.include_router(cita_sin_tratamiento.router)
app.include_router(cita.router)
app.include_router(tratamiento.router)
app.include_router(factura.router)
app.include_router(token.router)
app.include_router(admin.router)
app.include_router(contrasena.router)