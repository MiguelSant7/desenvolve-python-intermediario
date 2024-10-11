## Blibiotecas
from rich.console import Console
from rich.panel import Panel

console = Console()

def print_panel(text: str, isArquivo: bool=False):
    ''' 
    Imprime o texto em um layout formatado.

    isArquivo: Se True, considera text como um caminho para um arquivo.
    text: Arquivo a ser lido '''
    
    if isArquivo:
        with open(text, 'r') as file:
            text = file.read

    panel = Panel(text)
    console.print(panel)

def print_panel_title(text: str, isArquivo: bool=False):
    ''' 
    Imprime o texto em um layout formatado.

    isArquivo: Se True, considera text como um caminho para um arquivo.
    Text: arquivo a ser lido '''

    if isArquivo:
        with open(text, 'r') as file:
            text = file.read()

    console.print(text, title='Título...')
