# import sys
# sys.path.append("c:/Users/PDITA303.PDITA3112W/OneDrive/Documentos/PD - Curso/Python_Semestre02/modulo1/personalizador_python")


import argparse
# from personalizador import personalizador as ps
from personalizador.layout import print_layout, print_title
from personalizador.painel import print_panel, print_panel_title
from personalizador.progresso import print_progress, print_progress_file
from personalizador.estilo import print_styled, print_error

# O restante do seu código aqui




def main():
    parser = argparse.ArgumentParser(description="Personalizador de formatações com Rich")

    parser.add_argument('texto', help="Texto ou caminho do arquivo")
    parser.add_argument('-a', '--arquivo', action='store_true', help="Indica se o argumento é um arquivo")
    parser.add_argument('-m', '--modulo', choices=['layout', 'painel', 'progresso', 'estilo'], help="Escolha o módulo")
    parser.add_argument('-f', '--funcao', choices=['print_layout', 'print_title', 'print_panel', 'print_panel_title', 'print_progresso', 'print_progress_file', 'print_styled', 'print_error'], help="Escolha a função")

    args = parser.parse_args()

    if args.modulo == 'layout':
        if args.funcao == 'print_layout':
           print_layout(args.texto, args.arquivo)
        elif args.funcao == 'print_title':
            print_title(args.texto, args.arquivo)

    elif args.modulo == 'painel':
        if args.funcao == 'print_panel':
            print_panel(args.texto, args.arquivo)
        elif args.funcao == 'print_panel_title':
            print_panel_title(args.texto, args.arquivo)

    elif args.modulo == 'progresso':
        if args.funcao == 'print_progresso':
            print_progress(args.texto, args.arquivo)
        elif args.funcao == 'print_progress_file':
            print_progress_file(args.texto, args.arquivo)

    elif args.modulo == 'estilo':
        if args.funcao == 'print_styled':
            print_styled(args.texto, args.arquivo)
        elif args.funcao == 'print_error':
            print_error(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
