import unittest
from fastapi import status, Path
from models.usuario import Usuarios
from config.database import db_dependency
from routes.admin import get_all_usuarios, delete_usuario

class TestAdminRouter(unittest.TestCase):

    def test_get_all_usuarios(self):
        # Arrange
        usuario = {'rol': 'admin'}
        db = db_dependency()
        db.query(Usuarios).insert_one({'id': 1, 'nombre': 'Juan'})
        db.query(Usuarios).insert_one({'id': 2, 'nombre': 'Pedro'})

        # Act
        response = get_all_usuarios(usuario, db)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['nombre'], 'Juan')
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['nombre'], 'Pedro')

    def test_delete_usuario(self):
        # Arrange
        usuario = {'rol': 'admin'}
        db = db_dependency()
        db.query(Usuarios).insert_one({'id': 1, 'nombre': 'Juan'})

        # Act
        response = delete_usuario(usuario, db, 1)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(db.query(Usuarios).count(), 0)
