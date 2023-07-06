"""Start the server and handle the request"""
import os

from fastapi import FastAPI
from agent import Agent

app = FastAPI()

for config in os.listdir('./agents'):
    if not config.endswith('.toml'):
        continue
    agent = Agent.build_from_toml(os.path.join('./agents', config))
    app.add_api_route(agent.router, agent.handle, methods=['POST'])
