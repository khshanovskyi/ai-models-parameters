from task.app.main import run

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - anthropic.claude-v3-haiku
# - gemini-2.5-pro

run(
    # TODO:
    #  1. Provide `deployment_name` with model from the list above👆
    #  2. Use `n` parameter with value in range from 1 to 5!
)

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
