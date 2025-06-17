from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o-2024-05-13
# - anthropic.claude-v3-5-sonnet-v1
# - gemini-2.5-pro-preview-03-25

run(
    deployment_name='INSERT_DEPLOYMENT_NAME',
    api_key='YOUR_API_KEY',
    print_request=False, # Switch to False if you do not want to see the request in console
    print_only_content=False, # Switch to True if you want to see only content from response
)

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API