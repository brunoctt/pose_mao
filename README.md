# Reconhecimento de Pose de Mão
Reconhecimento de Pose de Mão para controle de barra de volume.

O reconhecimento de pose de mão foi realizado utilizando o [módulo de Detecção de Mãos](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/python) do framework MediaPipe.

A aplicação pode ser dividida em duas partes:

## Módulo de Detecção

Este é o módulo que implementa os métodos do MediaPipe para reconhecimento das poses de mão. Este módulo busca as posições do dedão e do dedo indicador.

## Módulo de Controle de Volume

Este módulo captura imagens de uma webcam para serem processadas pelo módulo de detecção, e da distância entre as posições dos dedos, ajusta a barra de volume.

## Exemplo de Uso

![Alt text](docs/example.gif)

## Como usar

### Preparar ambiente

Utilizando Python 3.11
1. Criar um ambiente virtual: `python -m venv venv`
2. Ativar o ambiente virtual: `venv\Scripts\activate.bat` (No Windows)
3. Instalar as bibliotecas: `pip install -r requirements.txt`

### Rodar o programa
1. Ativar o ambiente virtual: `venv\Scripts\activate.bat` (Caso não esteja)
2. Executar o arquivo [main](main.py): `python main.py`
3. Para finalizar a execução, basta fechar a janela aberta ou apertar ESC com a mesma seleciona

