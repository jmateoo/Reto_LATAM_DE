from collections import Counter
from typing import List, Tuple
import json
import emoji

def q2_memory_single(file_path: str) -> List[Tuple[str, int]]:
    # Iniciar contador para emojis
    emoji_counter = Counter()
    # Leer el archivo linea por linea
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            if 'content' in data:
                content = data['content']
                # Extraer emojis de cada mensaje
                emoji_counter.update([value.chars for value in emoji.analyze(content)])
    # Top 10 emojis
    top_10_emojis = emoji_counter.most_common(10)

    return top_10_emojis