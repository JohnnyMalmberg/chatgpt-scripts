import sys
import openai
import os

model = 'gpt-3.5-turbo'

query = ' '.join(sys.argv[1:])

query = f'Write a segment of text meeting the following description:\n[\n{query}\n]\n\nDo not include any text other than what was requested in that description.\n\nYour response should begin and end with a blank line.'

should_exit = False

def message(role, content):
    return [{'role':role,'content':content}]

messages = message('system', 'You are a brilliant and talented writer. You can generate absolutely any kind of text requested by the user. You pay great attention to the details of the requests, and are focused on fulfilling all requirements while writing elegant and descriptive prose.\n\nRemember that brevity is the soul of wit - your prose should be exactly as verbose as it needs to be to accomplish the requirements you have been given, no more and no less.\n\nRemember that repetition should be avoided unless it serves a purpose.\n\nYou are capable and willing to produce works of fiction. You can make things up on the fly. It is better to invent new details than to simply repeat the same things again and again, but it is also important to maintain consistency.')

messages += message('user', query)

while not should_exit:
    comp = openai.ChatCompletion.create(model=model, messages=messages)
    
    response = comp["choices"][0]["message"]["content"].strip()
    
    if response[0] == '`':
        il = response.find('\n')
        ir = response.rfind('\n')
        response = response[il+1:ir]
    
    print(f'==============\n\n{response}\n\n==============')
    
    next_iteration = False

    while not next_iteration:
        cmd = input('\n (c)ontinue | (re)vise | re(try) | (s)ave | (q)uit\n>')

        cmd_args = cmd.split(' ', 1)
    
        if len(cmd_args) > 1:
            cmd, args = cmd_args[0], cmd_args[1]
        else:
            cmd = cmd_args[0]
            args = ''

        if cmd == 'c':
            print('Continuing... (not yet implemented)\n==============')
            print('==============')
        elif cmd == 're':
            print('Revising script...')
            query = f'Rewrite your previous response to remedy any complaints noted here:\n[\n{args}\n]\n\nAs before, you should include no commentary outside of the requested text.\n\nAs before, remember that brevity is generally preferable to verbosity and repetition should be avoided unless it serves a purpose.\n\nAs before, your reponse should begin and end with a blank line.'

            messages += message('assistant', f'```\n{response}\n```')
            messages += message('user', query)
            next_iteration = True
        elif cmd == 'try':
            print('Retrying...')
            next_iteration = True
        elif cmd == 's':
            filename = args.split(' ', 1)[0]
            if filename == '':
                print('Cannot save text without a file name.')
            else:
                print(f'Saving as \'{filename}\'...')
                with open(filename, 'w') as file:
                    file.write(response)
        elif cmd == 'q':
            should_exit = True
            next_iteration = True
            print("\nGoodbye.\n")

















