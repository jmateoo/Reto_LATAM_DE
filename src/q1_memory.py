from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    # Cargar JSON linea por linea directamente a un DataFrame de pandas es mas optimo
    df = pd.read_json(file_path, lines=True)
    # Extraer campos necesarios
    df = df[['date', 'user', 'id']]
    df['user'] = df['user'].apply(lambda x: x['username'])    
    df['date'] = pd.DatetimeIndex(df['date']).date
    # Traer las 10 fechas con mas tweets
    top_10_dates = df['date'].value_counts().nlargest(10).index
    # Filtar el dataframe para solo incluir las 10 fechas con mas tweets
    df_top_10 = df[df['date'].isin(top_10_dates)]
    # Encontrar el usuario con mas tweets por fecha
    top_users = df_top_10.groupby('date')['user'].agg(lambda x: x.value_counts().index[0])
    # Convertir el resultado en una lista de tuplas
    result = [(date, user) for date, user in zip(top_10_dates, top_users)]
    
    return result