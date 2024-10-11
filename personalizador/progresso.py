## Blibiotecas
from rich.console import Console
from rich.progress import Progress

console = Console()


def print_progress(total: int):
    '''
    Imprime uma barra de progresso
    
    total: inteiro
    formatado para cor 'ciano'
    '''

    with Progress() as progress:
        task = progress.add_task("[cyan]progresso...", total=total)
    while not progress.finished:
        progress.update(task, advance=1)

    

def print_progress_file(file_path: str):
    ''' 
    Imprime uma barra de progresso enquanto lê os arquivos

    file_path (caminho para o arquivo) definido como string

    '''

    with open(file_path, 'rb') as file:
        file_content = file.read()
        total = len(file_content)

        with Progress() as progress:
            task = progress.add_task("[Cyan]Lendo arquivo..", total=total)
            for _ in file_content:
                progress.update(task, advance=1)