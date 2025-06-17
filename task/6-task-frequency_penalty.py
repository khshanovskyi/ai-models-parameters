from task.app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children

run(
    deployment_name='gemini-2.5-pro-preview-03-25',
    print_only_content=True,
    # TODO:
    #  1. Provide your `api_key`
    #  2. Use `frequency_penalty` parameter with different range (-2.0 to 2.0).
)

# Pay attention that when we set for `gpt-4o-2024-05-13` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# With Gemini or Anthropic, we don't have such an issue.
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.