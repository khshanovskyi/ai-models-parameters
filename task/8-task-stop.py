from task.app.main import run

# TODO:
#  Try `stop` parameter.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

run(
    deployment_name='gpt-4o',
    print_only_content=True,
    # TODO:
    #  1. Use `stop` parameter with value "\n\n"
    #  2. Use `stop` parameter with values ["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
    #  3. Optional: Set `print_only_content` as False to see the full JSON and what is the `finish_reason`
)

# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.