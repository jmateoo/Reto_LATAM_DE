from collections import Counter
from typing import List, Tuple
import re
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar una lista vacia para almacenar los nombres de usuario
    usernames = []
    # Cargar el archivo y extraer los nombres de usuario del campo content
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line.strip())
            if 'content' in data:
                content = data['content']
                # Usar regex para extraer los nombres de usuario
                usernames_in_content = re.findall(r'@(\w+)', content)
                # Agregar nombres de usuario a la lista
                usernames.extend(usernames_in_content)
    # Contar el numero de veces que aparece cada nombre de usuario
    username_counts = Counter(usernames)
    # Top 10 nombres de usuario
    top_10_usernames = username_counts.most_common(10)

    return top_10_usernames