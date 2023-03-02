import sys
import openai
import os

model = 'gpt-3.5-turbo'

query = ' '.join(sys.argv[1:])

query = f'Write a short and efficient python script to accomplish this task:\n[\n{query}\n]\n\nInclude comments only for code with a non-obvious purpose.\n\nAside from comments within the code, do not inlude any text other than the python script in your response.\n\nYour response should begin and end with a line containing only "```".'

should_exit = False

def message(role, content):
    return [{'role':role,'content':content}]

messages = message('system', 'You are a brilliant python script writer. You respond to requests only by writing python scripts. You pay great attention to details, and are focused on correctness, clarity, and performance. Include as many comments as are needed to make the purpose of your code clear, but do not explain things that would be obvious to a moderately-experienced python programmer.')

messages += message('user', query)

while not should_exit:
    comp = openai.ChatCompletion.create(model=model, messages=messages)
    
    response = comp["choices"][0]["message"]["content"].strip()
    
    if response[0] == '`':
        il = response.find('\n')
        ir = response.rfind('\n')
        response = response[il+1:ir]
    
    print(f'=== Script ===\n\n{response}\n\n==============')
    
    next_iteration = False

    while not next_iteration:
        cmd = input('\n(ex)ecute | (re)vise | re(try) | (s)ave | (q)uit\n>')

        cmd_args = cmd.split(' ', 1)
    
        if len(cmd_args) > 1:
            cmd, args = cmd_args[0], cmd_args[1]
        else:
            cmd = cmd_args[0]
            args = ''

        if cmd == 'ex':
            print('Executing script...\n==============')
            try:
                exec(response)
            except Exception as e:
                print(e)
            print('==============')
        elif cmd == 're':
            print('Revising script...')
            query = f'Rewrite the script you wrote, to remedy any issues, bugs, or other complaints noted here:\n[\n{args}\n]\n\nAs before, include comments to explain any non-obvious code, and aside from the comments you write, do not produce any commentary.\n\nAs before, your reponse should begin and end with a line containing only "```"'

            messages += message('assistant', f'```\n{response}\n```')
            messages += message('user', query)
            next_iteration = True
        elif cmd == 'try':
            print('Retrying...')
            next_iteration = True
        elif cmd == 's':
            filename = args.split(' ', 1)[0]
            if filename == '':
                print('Cannot save script without a file name.')
            else:
                print(f'Saving script as \'{filename}\'...')
                with open(filename, 'w') as file:
                    file.write(response)
        elif cmd == 'q':
            should_exit = True
            next_iteration = True
            print("\nGoodbye.\n")

















