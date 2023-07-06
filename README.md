# Agent Maker
Quickly create an artificial intelligence robot.

# Requirement
install requirement
```
pip install -r requirements.txt
```

# How to make your own agent

you can see agents/robot.toml:

```
[profile]
name = 'Tom'
router = '/chat'  # The router for your agent

[llm]
name = 'openai'
api_key = '<your-openai-api-key>'  # Your OPENAI_API_KEY

[[plugins]]  # Optional
name = 'system'
prompt = "You are a robot. You must answer questions."

[[plugins]]  # Optional
name = 'domain-expert'
domain = 'law'
occupation = 'lawyer'

```

You can create any number of robots, just put them all in the agents directory, and please use different routes.


# How to run

You can run that to start the server:
```
uvicorn main:app --reload --port 5000
```

Then:

```
curl --location 'http://127.0.0.1:5000/chat' \
--header 'Content-Type: application/json' \
--data '{
    "messages": [
        "user: Hello"
    ]
}'
```

You will get the response like:
```
{"result":" Hi there! How may I help you?"}
```
