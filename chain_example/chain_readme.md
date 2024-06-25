# Minimal Prompt Chainable
> Sequential prompt chaining in one method with context and output back-referencing.

## Files
- `main.py` - start here - full example using `MinimalChainable` from `chain.py` to build a sequential prompt chian
- `chain.py` - contains zero library minimal prompt chain class
- `chain_test.py` - tests for `chain.py`, you can ignore this
- `requirements.py` - python requirements

## Setup
- Create `.env` with `ANTHROPIC_API_KEY=` 
  - (or export `export ANTHROPIC_API_KEY=`)
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python main.py`

## Test
- `pytest chain_test.py`

## Watch
[When to use Prompt Chains. Ditching LangChain. ALL HAIL Claude 3.5 Sonnet](https://youtu.be/UOcYsrnSNok)

## Four guiding questions for When to Prompt Chain

### 1. Your tasks are complex for a single prompt
- Am I asking my LLM to accomplish 2 or more tasks that are distantly related in one prompt? If Yes → Build a prompt chain?
    - *Why: Prompt chaining can help break down complex tasks into manageable chunks, improving clarity and accuracy.*

### 2. Increase prompt performance and reduce errors
- Do I want to increase prompt performance to the max, and reduce errors to the minimum? If Yes → Build a prompt chain?
    - *Why: Prompt chaining allows you to guide the LLM's reasoning process, reducing the likelihood of irrelevant or nonsensical responses.*

### 3. Use output of previous prompt as input
- Do I need the output of a previous prompt to be the input (variable) of this prompt? If Yes → Build a prompt chain?
    - *Why: Prompt chaining is essential for tasks where subsequent prompts need to use information generated in previous steps.*

### 4. Adaptive workflow based on prompt flow
- Do I need an adaptive workflow that changes based on the flow of the prompt? If yes → Build a prompt chain
    - *Why: Prompt chaining allowed you to interject and respond to the flow of your 

### Summary
1. you find yourself solving two or more tasks in a single prompt.
2. need maximum error reduction and increased output quality.
3. you have subsequent prompts that rely on the output of previous prompts.
4. you need to take different actions based on evolving steps.

## Problems with LLM libraries (Langchain, Autogen, others)
- Unnecessary abstractions & premature abstractions!
- Easy to start - hard to finish!
- Rough Docs - rough debugging!

### Solution?
> STAY CLOSE TO THE METAL (the prompt)
> 
> The prompt is EVERYTHING, don't let any library take hide or abstract it from you unless you KNOW what's happening under the hood.
> 
> Build minimal abstracts with raw code that do ONE thing well. Outside of data collection, it's unlikely you NEED a library for the prompts, prompt chains and AI Agents of your tools and products.