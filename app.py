import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# --- ESTILO VISUAL (FONDO AZUL CLARO) ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #a6d8ff, #e0f2ff);
        color: #003366;
    }
    h1, h2, h3 {
        color: #003366;
        text-align: center;
    }
    p {
        color: #003366;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- INFO SISTEMA ---
st.write("💻 Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):
    print("El dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write("📩 Mensaje recibido:", message_received)

broker="157.230.214.127"
port=1883
client1= paho.Client("Controlsalo")
client1.on_message = on_message

# --- TITULO ---
st.title("🚀 Panel de Control MQTT")
st.subheader("🎛️ Controla tus dispositivos en tiempo real")

# --- BOTONES ON/OFF ---
if st.button('🟢 Encender'):
    act1="ON"
    client1= paho.Client("Controlsalo")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s", message)
else:
    st.write('')

if st.button('🔴 Apagar'):
    act1="OFF"
    client1= paho.Client("Controlsalo")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_s", message)
else:
    st.write('')

# --- SLIDER ---
st.subheader("🎚️ Control analógico")
values = st.slider('Selecciona el rango de valores',0.0, 100.0)
st.write('📊 Valor actual:', values)

# --- ENVIO ANALOGICO ---
if st.button('📡 Enviar valor'):
    client1= paho.Client("Controlsalo")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    ret= client1.publish("cmqtt_a", message)
else:
    st.write('')
