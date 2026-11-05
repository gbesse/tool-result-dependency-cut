# tool-result-dependency-cut

## Français

Trouver les résultats contaminés par un appel invalide.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m tool_result_dependency_cut examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Propagation d’invalidation sur DAG explicite ; un résultat localement valide reste bloqué si une donnée en amont est inconnue. Aucun modèle appelé.

### Limites

Dépendances déclarées uniquement. Les sources d’invalidation ne sont pas un ensemble minimal de réparations garanti ; aucune réexécution d’outil.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find results contaminated by an invalid tool call.

Synthetic data; no network access or secret required.

```sh
python -m tool_result_dependency_cut examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Invalidation propagation over an explicit DAG; locally valid output remains blocked when an upstream input is unknown. No model calls.

### Limits

Declared dependencies only. Invalidation sources are not a guaranteed minimal repair set; no tool reexecution.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar resultados contaminados por una llamada inválida.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m tool_result_dependency_cut examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Propaga invalidación sobre DAG explícito; salida localmente válida sigue bloqueada si una entrada previa es desconocida. Sin llamadas a modelos.

### Límites

Solo dependencias declaradas. Las fuentes de invalidación no garantizan reparación mínima; no reejecuta herramientas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.w3.org/TR/prov-dm/
