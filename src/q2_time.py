from collections import Counter
from typing import List, Tuple
import emoji
import json

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path, 'r') as file_data:
        data = [json.loads(line)["content"] for line in file_data]
    # Concatenar todos los emojis
    differents_emojis = [value.chars for text in data for value in emoji.analyze(text)]
    # Contar cada emoji
    emoji_counter = Counter(differents_emojis)
    # Top 10 emojis mas usados
    top_10_emojis = emoji_counter.most_common(10)
    # Convertir el resultado a una lista de tuplas
    emoji_tuple = [(emoji, count) for emoji, count in top_10_emojis]
    return emoji_tuple