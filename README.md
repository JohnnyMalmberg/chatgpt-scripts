A few simple python scripts for making use of the ChatGPT API.

askgpt.py starts a new conversation with ChatGPT, typically for the purpose of asking a quick question. It prints out the first response by ChatGPT and then exits.

pygpt.py produces a python script to accomplish the task specified in the command line arguments, and can then be used to iteratively revise the script before executing or saving it.

Usage: python pygpt <prompt>
Example: python pygpt rename every file in the current directory so that there are no upper-case characters
The prompt does not need to include any mention of producing a python script; the text you input will be inserted into a pre-made prompt, along the lines of "Write a short & efficient python script that will <prompt>."

