import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import sys  # Importa sys

# Determina o diretório onde o executável está rodando
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Caminho do modelo no diretório do executável
model_path = os.path.join(base_path, 'MobileNetV3Small.h5')

# Carrega o modelo
model = load_model(model_path)

# Inicializa a webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura frame-a-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensiona o frame para o tamanho de entrada do modelo
    resized_frame = cv2.resize(frame, (224, 224))

    # Pré-processa o frame
    img_array = image.img_to_array(resized_frame)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v3.preprocess_input(img_array)

    # Faz a previsão
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Exibe o resultado no frame
    if predicted_class == 0:
        label = 'Non-Violence'
        color = (0, 255, 0)  # Verde
    else:
        label = 'Violence'
        color = (0, 0, 255)  # Vermelho
        # Adiciona uma moldura vermelha ao redor do vídeo para alerta de violência
        frame = cv2.copyMakeBorder(frame, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 0, 255])
    
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Exibe o frame resultante
    cv2.imshow('Violence detection', frame)

    # Fecha a janela com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Quando tudo estiver feito, libera a captura
cap.release()
cv2.destroyAllWindows()
