import logging
import os
from datetime import datetime
import pwd


def setup_logging():
    '''Jeśli nie ma katalogu logs to go tworzymy'''
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir, mode=0o700)

    user = pwd.getpwuid(os.getuid()).pw_name
    '''Tworzenie numeru i nazwy pliku'''
    existing_logs = [f for f in os.listdir(logs_dir)
                     if f.startswith('log') and f.endswith('.txt')]
    next_num = len(existing_logs) + 1
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = f'{logs_dir}/log{next_num}_{timestamp}.txt'

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] - %(message)s',
        handlers=[
            logging.FileHandler(log_filename, mode='w'),
            logging.StreamHandler()
        ]
    )

    '''Informacje o wywołaniu'''
    logging.info('=== Rozpoczęcie logowania ===')
    logging.info(f'Użytkownik: {user}')
    logging.info(f'PID procesu: {os.getpid()}')
    logging.info(f'Katalog roboczy: {os.getcwd()}')
    logging.info(f'Plik logowania: {log_filename}')

    '''uprawnienia dla pliku logów'''
    os.chmod(log_filename, 0o600)

    return log_filename