"""
#@title Copyright 2023 Diarra Yacouba (Diarray). Double-click for license information.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
global var
var = "hello"

# Definissons une fonction qui peut nous dire si oui ou non un nombre donné est paire
def is_pair(nombre: int | float) -> bool: # Depuis la version 3.10 de python cette syntax peut être utilisé pour préciser le type d'une variable quand cette dernière peut en avoir plusieurs
  if nombre % 2:
    # si nombre % 2 est différent de zéro cette condition sera vrai et donc on pourra en conclure que le nombre est impaire
    return False
  return True # Si le block précédent est executé celle ci ne le sera pas, donc pas vraiment besoin de faire un "else"

def are_pair(*nombres) -> list[bool]:
    # Example de syntax qui crée un générateur implicitement
    # Cette syntax aussi appélée "list compression" va crée un générateur qui va retourner si le nombre est pair pour chaque nombre dans l'iterable "nombres"
    # Jusqu'au dernier nombre et il en fera une liste  
    response = [is_pair(num) for num in nombres]
    return response