from rich.console import Console
from rich.layout import Layout

console = Console()


def print_layout(text: str, isArquivo: bool = False):
    ''' Imprime o texto em um layout formatado.

    isArquivo: Se True, considera text como um caminho para um arquivo.'''

    if isArquivo: # Se isArquivo: True...
        with open(text, 'r') as file: # Abra o arquivo no modo 'r'(Apenas leitura)
            text = file.read()

    Layout = Layout() # Assim como console = Console(), esta afirmando a criação de um layout
    Layout.split_row(Layout(name='main'))  # Criação de uma linha horizontal (split_row) com o nome 'main'
    Layout["main"].update(text) # Adição do arquivo para a estrutura principal
    
    console.print(Layout)   



def print_title(text: str, isArquivo: bool = False):
    '''Imprime o texto como título formatado.
    
    isArquivo: Se True, considera text como um caminho para um arquivo.'''

    if isArquivo: # Se isArquivo: True...
        with open(text, 'r') as file: # Abra o arquivo no modo 'r'(Apenas leitura)
            text = file.read()

    console.print(text, style="bold magenta")

    

