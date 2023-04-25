from flask import Flask,jsonify,json
from flask_cors import CORS
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt



app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def Home():
    response = {
        "Name": "John Developer",
        "Status": "200",
    }
    return response


def Conversion(Datos):
    #  aqui haremos el entrenamiento Y conversion
    celsius = np.array([-40, -10, 0, 8, 15, 22, 38, 100], dtype=float)
    farenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4, 212], dtype=float)
    oculta1 =  tf.keras.layers.Dense(units=3 , input_shape=[1])
    oculta2 =  tf.keras.layers.Dense(units=3)
    salida =  tf.keras.layers.Dense(units=1)
    modelo = tf.keras.Sequential([oculta1,oculta2,salida])

    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )
    
    print('Comenzando el train...')
    modelo.fit(celsius,farenheit, epochs=1000, verbose=False)
    print('modelo entrenado')
    resultado = modelo.predict([Datos])
    

    return resultado

def ConversionINT(Datos):
    celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=int)
    farenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=int)
    oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
    oculta2 = tf.keras.layers.Dense(units=3)
    salida = tf.keras.layers.Dense(units=1)
    modelo = tf.keras.Sequential([oculta1, oculta2, salida])

    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )

    print('Comenzando el entrenamiento...')
    modelo.fit(celsius, farenheit, epochs=1000, verbose=False)
    print('Modelo entrenado')
    resultado = modelo.predict([Datos])

    return resultado


@app.route('/api/transform/<float:Grados>', methods=['POST','GET'])
def CelsiusDecimal(Grados):
    # Obtener la temperatura en Fahrenheit
    fahrenheit = Conversion(float(Grados))

    # Crear un diccionario con el resultado
    resultado_dict = {'resultado': fahrenheit.item()}

    # Convertir el diccionario en una cadena JSON
    resultado_json = json.dumps(resultado_dict)

    # Devolver el resultado de la conversión en formato JSON al cliente
    return resultado_json

@app.route('/api/transform/<int:Grados>', methods=['POST','GET'])
def CelsiusEntero(Grados):
    # Obtener la temperatura en Fahrenheit
    fahrenheit = ConversionINT(int(Grados))

    # Crear un diccionario con el resultado
    resultado_dict = {'resultado': fahrenheit.item()}

    # Convertir el diccionario en una cadena JSON
    resultado_json = json.dumps(resultado_dict)

    # Devolver el resultado de la conversión en formato JSON al cliente
    return resultado_json









if __name__ == '__main__':
    app.run(debug=True)