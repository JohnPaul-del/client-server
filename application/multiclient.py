import subprocess

from application.common.variables import ACTION

process_list = []

while True:
    ACTION = input('Choose action: q - quit, s - start server and client, x - close')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        process_list.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))

        for el in range(2):
            process_list.append(subprocess.Popen('python client.py -m send',
                                                 creationflags=subprocess.CREATE_NEW_CONSOLE))
        for el in range(5):
            process_list.append(subprocess.Popen('python client.py -m listen',
                                                 creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        while process_list:
            VICTIM = process_list.pop()
            VICTIM.kill()