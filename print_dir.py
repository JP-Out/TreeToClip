import os
import pyperclip
import io

def print_tree(dir_path, indent='', is_root=True, output=None):
    """
    Imprime a estrutura de diretórios e arquivos a partir do diretório especificado.
    Ignora arquivos e diretórios ocultos e lista diretórios antes dos arquivos.

    :param dir_path: Caminho do diretório a ser listado
    :param indent: Indentação para visualização hierárquica
    :param is_root: Se é o diretório raiz que está sendo listado
    :param output: Objeto StringIO para capturar a saída
    """
    if output is None:
        output = io.StringIO()

    if not os.path.isdir(dir_path):
        output.write(f"{dir_path} não é um diretório válido ou não é acessível.\n")
        return output.getvalue()

    try:
        items = os.listdir(dir_path)
        items.sort()  # Ordena para uma exibição mais consistente

        directories = []
        files = []

        # Separa diretórios e arquivos
        for item in items:
            if item.startswith('.') or item == 'dist':
                continue  # Ignora diretórios ocultos e 'dist'
            
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                directories.append(item)
            else:
                files.append(item)
        
        # Se for o diretório raiz, imprima apenas uma vez
        if is_root:
            output.write(f"{os.path.basename(dir_path)}/\n")
        
        # Imprime diretórios
        for directory in directories:
            directory_path = os.path.join(dir_path, directory)
            try:
                output.write(f"{indent}{directory}/\n")
                print_tree(directory_path, indent + '    ', is_root=False, output=output)
            except PermissionError:
                output.write(f"{indent}{directory}/ (acesso negado)\n")
            except OSError as e:
                output.write(f"{indent}{directory}/ (erro: {e})\n")

        # Imprime arquivos
        for file in files:
            try:
                output.write(f"{indent}{file}\n")
            except PermissionError:
                output.write(f"{indent}{file} (acesso negado)\n")
            except OSError as e:
                output.write(f"{indent}{file} (erro: {e})\n")

    except PermissionError:
        output.write(f"Não é possível acessar o diretório {dir_path} (acesso negado)\n")
    except OSError as e:
        output.write(f"Erro ao acessar o diretório {dir_path} (erro: {e})\n")
    
    return output.getvalue()

# Caminho do diretório que você deseja listar
diretorio = input("Digite o caminho do diretório: ")
output = io.StringIO()
print_tree(diretorio, output=output)

# Copiar a saída para a área de transferência
pyperclip.copy(output.getvalue())

print("Estrutura copiada\nCole aqui: tree.nathanfriend.io")
