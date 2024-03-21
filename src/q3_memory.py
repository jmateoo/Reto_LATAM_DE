from collections import Counter
from typing import List, Tuple
import re
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar un contador para almacenar el numero de veces que aparece cada nombre de usuario
    username_counts = Counter()
    # Cargar el archivo y extraer los nombres de usuario del campo content
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line.strip())
            if 'content' in data:
                content = data['content']
                # Usar regex para extraer los nombres de usuario
                usernames_in_content = re.findall(r'@(\w+)', content)
                # Actualizar el contador con los nombres de usuario
                username_counts.update(usernames_in_content)
    # Top 10 nombres de usuario
    top_10_usernames = username_counts.most_common(10)

    return top_10_usernames