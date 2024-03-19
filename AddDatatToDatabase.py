import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://listaasistencia-254d9-default-rtdb.firebaseio.com/'
})

ref = db.reference('Estudiantes')
data = {
    "JuanBorjas":
        {
            "nombre": "Juan Borjas",
            "carrera": "Ingenieria en Sistemas",
            "anio": 2021,
            "asistencia_total": 7,
            "standing": "G",
            "anio_actual": 4,
            "ultima_asistencia": "2024-03-11 00:54:34"
        },
    "EmilioCantarero":
        {
            "nombre": "Emilio Cantarero",
            "carrera": "Ingenieria en Sistemas",
            "anio": 2021,
            "asistencia_total": 7,
            "standing": "G",
            "anio_actual": 4,
            "ultima_asistencia": "2024-03-11 00:54:34"
        },
    "MarcelaRivera":
        {
            "nombre": "Marcela Rivera",
            "carrera": "Ingenieria en Sistemas",
            "anio": 2019,
            "asistencia_total": 7,
            "standing": "G",
            "anio_actual": 4,
            "ultima_asistencia": "2024-03-11 00:54:34"
        },
    "JafetMorel":
        {
            "nombre": "Jafet Morel",
            "carrera": "Ingenieria en Sistemas",
            "anio": 2020,
            "asistencia_total": 7,
            "standing": "G",
            "anio_actual": 4,
            "ultima_asistencia": "2024-03-11 00:54:34"
        },
    "AbbyBorjas":
        {
            "nombre": "Abby Borjas",
            "carrera": "Licenciatura en Enfermeria",
            "anio": 2020,
            "asistencia_total": 7,
            "standing": "G",
            "anio_actual": 4,
            "ultima_asistencia": "2024-03-11 00:54:34"
        },
"GeovannyFortin":
        {
            "nombre": "Geovanny Fortin",
            "carrera": "Ingenieria en sistemas ",
            "anio": 2020,
            "asistencia_total": 7,
            "standing": "G",
            "anio_actual": 4,
            "ultima_asistencia": "2024-03-11 00:54:34"
        },
"EdgarCruz":
        {
            "nombre": "Edgar Membreno",
            "carrera": "Ingenieria en sistemas ",
            "anio": 2020,
            "asistencia_total": 7,
            "standing": "G",
            "anio_actual": 4,
            "ultima_asistencia": "2024-03-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)