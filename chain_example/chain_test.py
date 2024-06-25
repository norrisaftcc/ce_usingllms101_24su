from chain import MinimalChainable


def test_chainable_solo():
    # Mock model and callable function
    class MockModel:
        pass

    def mock_callable_prompt(model, prompt):
        return f"Solo response: {prompt}"

    # Test context and single chain
    context = {"variable": "Test"}
    chains = ["Single prompt: {{variable}}"]

    # Run the Chainable
    result, _ = MinimalChainable.run(context, MockModel(), mock_callable_prompt, chains)

    # Assert the results
    assert len(result) == 1
    assert result[0] == "Solo response: Single prompt: Test"


def test_chainable_run():
    # Mock model and callable function
    class MockModel:
        pass

    def mock_callable_prompt(model, prompt):
        return f"Response to: {prompt}"

    # Test context and chains
    context = {"var1": "Hello", "var2": "World"}
    chains = ["First prompt: {{var1}}", "Second prompt: {{var2}} and {{var1}}"]

    # Run the Chainable
    result, _ = MinimalChainable.run(context, MockModel(), mock_callable_prompt, chains)

    # Assert the results
    assert len(result) == 2
    assert result[0] == "Response to: First prompt: Hello"
    assert result[1] == "Response to: Second prompt: World and Hello"


def test_chainable_with_output():
    # Mock model and callable function
    class MockModel:
        pass

    def mock_callable_prompt(model, prompt):
        return f"Response to: {prompt}"

    # Test context and chains
    context = {"var1": "Hello", "var2": "World"}
    chains = ["First prompt: {{var1}}", "Second prompt: {{var2}} and {{output[-1]}}"]

    # Run the Chainable
    result, _ = MinimalChainable.run(context, MockModel(), mock_callable_prompt, chains)

    # Assert the results
    assert len(result) == 2
    assert result[0] == "Response to: First prompt: Hello"
    assert (
        result[1]
        == "Response to: Second prompt: World and Response to: First prompt: Hello"
    )


def test_chainable_json_output():
    # Mock model and callable function
    class MockModel:
        pass

    def mock_callable_prompt(model, prompt):
        if "Output JSON" in prompt:
            return '{"key": "value"}'
        return prompt

    # Test context and chains
    context = {"test": "JSON"}
    chains = ["Output JSON: {{test}}", "Reference JSON: {{output[-1].key}}"]

    # Run the Chainable
    result, _ = MinimalChainable.run(context, MockModel(), mock_callable_prompt, chains)

    # Assert the results
    assert len(result) == 2
    assert isinstance(result[0], dict)
    print("result", result)
    assert result[0] == {"key": "value"}
    assert result[1] == "Reference JSON: value"  # Remove quotes around "value"


def test_chainable_reference_entire_json_output():
    # Mock model and callable function
    class MockModel:
        pass

    def mock_callable_prompt(model, prompt):
        if "Output JSON" in prompt:
            return '{"key": "value"}'
        return prompt

    context = {"test": "JSON"}
    chains = ["Output JSON: {{test}}", "Reference JSON: {{output[-1]}}"]

    # Run the Chainable
    result, _ = MinimalChainable.run(context, MockModel(), mock_callable_prompt, chains)

    assert len(result) == 2
    assert isinstance(result[0], dict)
    assert result[0] == {"key": "value"}
    assert result[1] == 'Reference JSON: {"key": "value"}'


def test_chainable_reference_long_output_value():
    # Mock model and callable function
    class MockModel:
        pass

    def mock_callable_prompt(model, prompt):
        return prompt

    context = {"test": "JSON"}
    chains = [
        "Output JSON: {{test}}",
        "1 Reference JSON: {{output[-1]}}",
        "2 Reference JSON: {{output[-2]}}",
        "3 Reference JSON: {{output[-1]}}",
    ]

    # Run the Chainable
    result, _ = MinimalChainable.run(context, MockModel(), mock_callable_prompt, chains)

    assert len(result) == 4
    assert result[0] == "Output JSON: JSON"
    assert result[1] == "1 Reference JSON: Output JSON: JSON"
    assert result[2] == "2 Reference JSON: Output JSON: JSON"
    assert result[3] == "3 Reference JSON: 2 Reference JSON: Output JSON: JSON"


def test_chainable_empty_context():
    # Mock model and callable function
    class MockModel:
        pass

    def mock_callable_prompt(model, prompt):
        return prompt

    # Test with empty context
    context = {}
    chains = ["Simple prompt"]

    # Run the Chainable
    result, _ = MinimalChainable.run(context, MockModel(), mock_callable_prompt, chains)

    # Assert the results
    assert len(result) == 1
    assert result[0] == "Simple prompt"


def test_chainable_json_output_with_markdown():
    # Mock model and callable function
    class MockModel:
        pass

    def mock_callable_prompt(model, prompt):
        return """
        Here's a JSON response wrapped in markdown:
        ```json
        {
            "key": "value",
            "number": 42,
            "nested": {
                "inner": "content"
            }
        }
        ```
        """

    context = {}
    chains = ["Test JSON parsing"]

    # Run the Chainable
    result, _ = MinimalChainable.run(context, MockModel(), mock_callable_prompt, chains)

    # Assert the results
    assert len(result) == 1
    assert isinstance(result[0], dict)
    assert result[0] == {"key": "value", "number": 42, "nested": {"inner": "content"}}
