# Digital Surveillance: Vigilante Inteligente

![Capa do Projeto](https://github.com/ViniciusKanh/Digital-Surveillance-Vigilante-Inteligente/blob/main/assets/img/Capa.png)

## :mag: Sobre o Projeto

O projeto "Digital Surveillance: Vigilante Inteligente" é uma iniciativa tecnológica avançada focada em segurança e monitoramento através de Inteligência Artificial (IA). Desenvolvido por Vinicius de Souza Santos, o projeto utiliza algoritmos de aprendizado de máquina para detectar e diferenciar situações de violência e não violência em tempo real, utilizando uma webcam.

Este projeto não é apenas uma aplicação tecnológica, mas também uma ferramenta de segurança crucial, destinada a melhorar a vigilância e a resposta a incidentes em diversos ambientes, desde espaços públicos até residências particulares.

## :wrench: Metodologia e Desenvolvimento

### Estrutura do Projeto

O núcleo deste projeto é um modelo de classificação de imagens, treinado em um conjunto de dados contendo mais de 11.000 imagens, categorizadas em "Violência" e "Não Violência". O modelo é capaz de processar imagens em tempo real e identificar a presença de violência com alta precisão.

### Tecnologias Utilizadas

- **TensorFlow e Keras**: Para o desenvolvimento e treinamento do modelo de IA.
- **OpenCV (cv2)**: Para captura e processamento de vídeo em tempo real.
- **Python**: Linguagem de programação usada para o desenvolvimento do projeto.
- **PyInstaller**: Para a criação de um executável do script Python.

### Processo de Desenvolvimento

1. **Preparação dos Dados**: O conjunto de dados foi dividido em categorias de "Violência" e "Não Violência", com redimensionamento e pré-processamento das imagens para adequá-las ao modelo.

2. **Treinamento do Modelo**: Utilizou-se o modelo pré-treinado MobileNetV3Small, escolhido por sua eficiência e adequação para tarefas de classificação de imagens em dispositivos com recursos limitados. O modelo foi ajustado e treinado com os dados específicos do projeto.

3. **Desenvolvimento do Script**: Um script Python foi criado para utilizar a webcam, processar os quadros em tempo real e aplicar o modelo para detectar violência.

4. **Compilação com PyInstaller**: O script foi convertido em um executável standalone, permitindo seu uso em qualquer sistema Windows sem a necessidade de instalar dependências adicionais.

### Código do Projeto

O script principal do projeto realiza a captura de vídeo, processamento de imagem e aplicação do modelo para detecção de violência. O código abaixo demonstra a lógica central do aplicativo:

```python
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Carrega o modelo
model = load_model('caminho/para/MobileNetV3Small.h5')

# Inicializa a webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Processamento do frame
    # ...

    # Aplica o modelo e exibe o resultado
    # ...

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
### Por que MobileNetV3Small?

O modelo MobileNetV3Small foi escolhido por sua eficiência em termos de computação e memória, tornando-o ideal para aplicativos em tempo real e dispositivos com recursos limitados. Este modelo é conhecido por sua alta precisão em tarefas de classificação de imagens, mantendo uma arquitetura leve.

## :link: Contatos e Referências

- **Desenvolvedor**: Vinicius de Souza Santos
- **GitHub**: [ViniciusKanh](https://github.com/ViniciusKanh)
- **LinkedIn**: [Perfil no LinkedIn](https://www.linkedin.com/notifications/?filter=all)
- **E-mail**: [vinnyciussouza@outlook.com](mailto:vinnyciussouza@outlook.com)
