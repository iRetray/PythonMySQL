from PyQt5 import QtWidgets
from database.connection import connect
from modelo.actividades import actividades


class ActivitiesController:
    def __init__(self):
        self.activities = actividades()
