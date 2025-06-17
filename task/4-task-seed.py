from task.app.main import run

# TODO:
#  Try the `seed` parameter:
#       It allows us to reduce entropy by making the model's output more deterministic.
#       There's no universally "best" seed - any integer works fine. Common approaches:
#            - For testing: Use simple values like 42, 123, or 1000
#       Default: None or random unless specified on the LLM side
#  User massage: Name a random animal

run(
    deployment_name='anthropic.claude-v3-5-sonnet-v1',
    # TODO:
    #  1. Provide your `api_key`
    #  2. Use `seed` parameter with value 42 (or whatever you want)
    #  3. Use `n` parameter with value 5
)

# Check the content in choices. The expected result is that in almost all choices the result will be the same.
# If you restart the app and retry, it should be mostly the same.
# Also, try it without `seed` parameter.