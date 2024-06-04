# Project Name
VITA (test example, using Autogen)

## Description

This project is a sample project generated using LLM (Language Model) and Autogen. It serves as a starting point for developing LLM-based applications.

the wrapper is only needed for Claude, LMStudio connects to Autogen fine.

## Steps

each agent will have a model and a prompt (we can swap these out individually)
We'll A/B test with different models/prompts and get instructor and student feedback on which is working the best

## Features

- Explain why code doesn't work
- Explain what my code is doing
- Explain concepts (by explaining instructor-provided sample code)

## Installation

pip install autogenstudio
#todo: get API key
autogenstudio ui
- click "forward port"
- from web ui:
    - go into agent workflow
- go to models
    - set the model and base url
- go to agents
    - create new agents (example was line numberer, error explainer)
- go to workflow
    - three dots "..." -> Group Chat (this used to be default i think)
    - summary method: last = last response from each agent, llm = model will summarize
    - userproxy: stands in for the human (system prompt: "You are a python programming student...")
- playground, choose workflow -> new session
question: how do we do rag with this?
also run an example with local LMStudio for comparison?



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).