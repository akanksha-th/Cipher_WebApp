# Violet Evergarden Cipher 
[https://cipher-violet-evergarden-anime.streamlit.app/](https://cipher-anime-violet-evergarden.streamlit.app/)

A creative cipher that converts English text into the unique alphabet used in the Violet Evergarden anime.
Features:

    🖌️ Custom Alphabets: Created the alphabet images from scratch.
    💻 Streamlit Integration: A sleek and interactive web app built with Streamlit.
    🌐 Live Demo: Check out the deployed project here. -> https://cipher-anime-violet-evergarden.streamlit.app/

Inspiration:
This project merges creativity and tech, blending inspiration from anime, languages, and design into a fun and functional application.


## Project Structure

    cipher-webapp
    │   .gitignore
    │   LICENSE
    │   README.md
    │   requirements.txt
    │   trial_nb.ipynb
    │   
    ├───.devcontainer
    │       devcontainer.json
    │       
    ├───configs/
    │       config.yaml
    │       
    ├───data/
    │       alphabets in png format
    │
    ├───datasets/
    │       data_loader.py
    │       transforms.py
    │
    ├───inference/
    │       pipeline.py
    │       predict.py
    │
    ├───outputs/
    │       output.png
    │       Screenshot 2024-12-18 173140.png
    │       Screenshot 2024-12-18 173450.png
    │       Screenshot 2024-12-18 175328.png
    │
    ├───training/
    │       evaluate.py
    │       train.py
    │       utils.py
    │
    └───ui/
        │   app.py
        │   
        └───app_utils
                violet-evergarden-violets-letter-to-major-gilbert.jpg