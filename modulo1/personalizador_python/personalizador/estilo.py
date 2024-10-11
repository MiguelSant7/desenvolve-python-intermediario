## Blibioteca

from rich.console import Console 


console = Console()

def print_styled(text: str, isArquivo: bool = False, style: str = 'bold green'):
    '''
    Imprime o texto com estilos

    text definido como string
    isArquivo: Se True, considera text como um caminho para um arquivo.
    style definido como bold green
    '''

    if isArquivo:
        with open(text, 'r') as file:
            text = file.read
    
    console.print(text, style=style)


def print_error(text: str, isArquivo: bool = False):
    '''
    imprime o texto com estilo de erro formatado

    text definido como string
    isArquivo: Se True, considera text como um caminho para um arquivo.

    '''

    if isArquivo:
        with open(text, 'r') as file:
            text = file.read
    
    console.print(text, style='bold green')