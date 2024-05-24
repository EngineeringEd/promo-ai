## Promo AI

A little POC for using AI to build an admin tool that does something on an internal API

### All instructions are Linux and Mac specific

## Requirements

Ollama needs to be installed on the machine. The models used are:
* llama3
* codellama

Run `ollama pull [MODEL_NAME]` to get the model on to your machine. Then, run `ollama serve` to start the local server.


### Installation

This repo uses Poetry. If you have it installed, running `poetry install` will install dependencies inside of a virtual environment. Depending on how your system is set up, it may be in the directory, it may not.

If you do nothave Poetry installed:
1. Create a Virtual Environment `python3 -m venv .venv` (arg to venv can be any name you want)
2. Activate the virtual environment `source ./venv/bin/activate`
3. Run `pip install -e .` to install all dependencies


### Usage
Use main if you want to play with the JSON generation.
Poetry script `poetry run main`
Python script `python promo_ai/main.py` (ignore the Streamlit error.)

### Chat app
The chat app uses a ReAct agent to handle stuff. The terminal outputs reasoning and actions taken.

Run `streamlit run promo_ai/chat_app.py` to start the chat. The browser should automatically open the window.

> N.B. Generations can take a little while depending on your hardware. With an NVidia GPU installed (Ollama will tell you if it detects one), things should happen within about 5 seconds or less. 

