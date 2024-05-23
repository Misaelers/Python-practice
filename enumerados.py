from enum import Enum  
Semana = Enum(
    value='Semana',
    names=('LU MA MI JU VI SA DO'),
) # Enumerado
for dia in Semana:
    print(dia.name, '<->', dia.value)