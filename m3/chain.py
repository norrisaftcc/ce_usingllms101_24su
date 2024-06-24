import json
import re
from typing import List, Dict, Callable, Any, Union


class MinimalChainable:
    """
    Sequential prompt chaining with context and output back-references.
    """

    @staticmethod
    def run(
        context: Dict[str, Any], model: Any, callable: Callable, prompts: List[str]
    ) -> List[Any]:
        # Initialize an empty list to store the outputs
        output = []
        context_filled_prompts = []

        # Iterate over each prompt with its index
        for i, prompt in enumerate(prompts):
            # Iterate over each key-value pair in the context
            for key, value in context.items():
                # Check if the key is in the prompt
                if "{{" + key + "}}" in prompt:
                    # Replace the key with its value
                    prompt = prompt.replace("{{" + key + "}}", str(value))

            # Replace references to previous outputs
            # Iterate from the current index down to 1
            for j in range(i, 0, -1):
                # Get the previous output
                previous_output = output[i - j]

                # Handle JSON (dict) output references
                # Check if the previous output is a dictionary
                if isinstance(previous_output, dict):
                    # Check if the reference is in the prompt
                    if f"{{{{output[-{j}]}}}}" in prompt:
                        # Replace the reference with the JSON string
                        prompt = prompt.replace(
                            f"{{{{output[-{j}]}}}}", json.dumps(previous_output)
                        )
                    # Iterate over each key-value pair in the previous output
                    for key, value in previous_output.items():
                        # Check if the key reference is in the prompt
                        if f"{{{{output[-{j}].{key}}}}}" in prompt:
                            # Replace the key reference with its value
                            prompt = prompt.replace(
                                f"{{{{output[-{j}].{key}}}}}", str(value)
                            )
                # If not a dict, use the original string
                else:
                    # Check if the reference is in the prompt
                    if f"{{{{output[-{j}]}}}}" in prompt:
                        # Replace the reference with the previous output
                        prompt = prompt.replace(
                            f"{{{{output[-{j}]}}}}", str(previous_output)
                        )

            # Append the context filled prompt to the list
            context_filled_prompts.append(prompt)

            # Call the provided callable with the processed prompt
            # Get the result by calling the callable with the model and prompt
            result = callable(model, prompt)

            # Try to parse the result as JSON, handling markdown-wrapped JSON
            try:
                # First, attempt to extract JSON from markdown code blocks
                # Search for JSON in markdown code blocks
                json_match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", result)
                # If a match is found
                if json_match:
                    # Parse the JSON from the match
                    result = json.loads(json_match.group(1))
                else:
                    # If no markdown block found, try parsing the entire result
                    # Parse the entire result as JSON
                    result = json.loads(result)
            except json.JSONDecodeError:
                # Not JSON, keep as is
                pass

            # Append the result to the output list
            output.append(result)

        # Return the list of outputs
        return output, context_filled_prompts

    @staticmethod
    def to_delim_text_file(name: str, content: List[Union[str, dict]]) -> str:
        result_string = ""
        with open(f"{name}.txt", "w") as outfile:
            for i, item in enumerate(content, 1):
                if isinstance(item, dict):
                    item = json.dumps(item)
                if isinstance(item, list):
                    item = json.dumps(item)
                chain_text_delim = (
                    f"{'🔗' * i} -------- Prompt Chain Result #{i} -------------\n\n"
                )
                outfile.write(chain_text_delim)
                outfile.write(item)
                outfile.write("\n\n")

                result_string += chain_text_delim + item + "\n\n"

        return result_string
