# Plan: Desensamblado Bottom-Up de Tzar WASM a Python

## Objetivo

Convertir el WASM del juego Tzar a código Python legible, procesando desde las hojas (funciones más simples) hacia arriba, respetando dependencias.

## Estructura de Salida

```
tzar/
├── _tree.json              # Árbol de dependencias ordenado
├── _progress.json          # Estado del desensamblado
├── _symbols.json           # Mapeo de nombres
│
├── memory/                 # Funciones de memoria
│   ├── alloc.py           # $func26
│   └── free.py            # $af
│
├── math/                   # Funciones matemáticas
│   └── ...
│
├── webp/                   # Decoder WebP
│   └── ...
│
├── terrain/                # Sistema de terreno
│   └── ...
│
├── units/                  # Sistema de unidades
│   └── ...
│
├── buildings/              # Sistema de edificios
│   └── ...
│
├── ai/                     # Inteligencia artificial
│   └── ...
│
├── render/                 # Renderizado
│   └── ...
│
├── game/                   # Loop principal
│   └── ...
│
└── _unprocessed/           # Funciones sin categorizar
    └── ...
```

## Fases

### Fase 1: Análisis de Dependencias

1. **Cargar el callgraph existente**
   - Usar `output/graphs/callgraph.json`

2. **Detectar ciclos (SCCs)**
   - Encontrar Strongly Connected Components
   - Marcarlos como "grupos atómicos" (se procesan juntos)

3. **Ordenamiento topológico**
   - Ordenar funciones de hojas → raíces
   - Respetar dependencias: si A llama a B, B va antes que A

4. **Generar árbol de procesamiento**
   - `_tree.json` con orden exacto de procesamiento

### Fase 2: Scaffolding

1. **Crear estructura de directorios**
   - Crear `tzar/` con subdirectorios por categoría

2. **Generar stubs para todas las funciones**
   - Cada función como archivo `.py` con firma pero sin implementación
   - Incluir metadatos en docstring

3. **Crear archivo de estado**
   - `_progress.json` con estado de cada función:
     - `pending`: no procesada
     - `stub`: solo firma
     - `wip`: en proceso
     - `done`: completada
     - `verified`: testeada

### Fase 3: Desensamblado Incremental

Para cada función en orden topológico (hojas primero):

```
┌─────────────────────────────────────────────────────────────┐
│  PROCESO POR FUNCIÓN                                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. VERIFICAR DEPENDENCIAS                                  │
│     └─ ¿Todas las funciones que llama están "done"?        │
│        ├─ SÍ → Continuar                                   │
│        └─ NO → Procesar dependencia primero (recursivo)    │
│                                                             │
│  2. EXTRAER FUNCIÓN WAT                                     │
│     └─ Leer del archivo original o output/functions/       │
│                                                             │
│  3. ANALIZAR                                                │
│     ├─ Parámetros y tipos                                  │
│     ├─ Variables locales                                   │
│     ├─ Operaciones (loads, stores, calls)                  │
│     └─ Control flow (if, loop, block, br)                  │
│                                                             │
│  4. TRADUCIR A PYTHON                                       │
│     ├─ Convertir stack machine → expresiones               │
│     ├─ Reemplazar calls con imports Python                 │
│     ├─ Convertir memory ops → array access                 │
│     └─ Convertir control flow → if/while/for               │
│                                                             │
│  5. NOMBRAR                                                 │
│     └─ Usar contexto de callees para inferir nombre        │
│                                                             │
│  6. GUARDAR                                                 │
│     ├─ Escribir archivo .py                                │
│     └─ Actualizar _progress.json                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Fase 4: Traducción WAT → Python

#### 4.1 Mapeo de Tipos

| WAT | Python |
|-----|--------|
| i32 | int |
| i64 | int |
| f32 | float |
| f64 | float |
| funcref | Callable |

#### 4.2 Mapeo de Memoria

```python
# WAT
# i32.load offset=4
# local.get $ptr

# Python
memory[ptr + 4]  # usando array/memoryview

# O con struct
struct.unpack_from('<i', memory, ptr + 4)[0]
```

#### 4.3 Mapeo de Control Flow

```python
# WAT: block/br_if
block $label0
  ...
  br_if $label0
end

# Python
while True:
    ...
    if condition:
        break
```

```python
# WAT: if/else
if
  ...
else
  ...
end

# Python
if condition:
    ...
else:
    ...
```

#### 4.4 Mapeo de Stack Machine

```python
# WAT (stack machine)
local.get $var0
i32.const 4
i32.add
i32.load

# Python (expresión)
memory[var0 + 4]
```

### Fase 5: Validación

1. **Tests unitarios**
   - Comparar comportamiento WAT vs Python

2. **Tests de integración**
   - Ejecutar secuencias de funciones

3. **Verificación de memoria**
   - Comparar estado de memoria después de operaciones

## Orden de Procesamiento Sugerido

```
Nivel 0 (Hojas puras - 120 funciones):
├── Imports del sistema ($a.*)
├── Funciones matemáticas simples
├── Helpers pequeños
└── Constantes/getters

Nivel 1 (Llaman solo a hojas - ~200 funciones):
├── Memory alloc/free ($func26, $af)
├── Math helpers
└── Utilidades básicas

Nivel 2-5 (Sistemas - ~400 funciones):
├── WebP decoder
├── Terrain system
├── Unit/Building logic
└── Resource management

Nivel 6+ (Managers - ~200 funciones):
├── AI system
├── Game loop
├── Render pipeline
└── Entry points
```

## Herramientas a Crear

### 1. `tools/generate_tree.py`
Genera el árbol de dependencias ordenado

### 2. `tools/scaffold.py`
Crea la estructura de directorios y stubs

### 3. `tools/wat2py.py`
Traduce una función WAT a Python

### 4. `tools/process_next.py`
Procesa la siguiente función pendiente

### 5. `tools/verify.py`
Verifica una función traducida

## Estado de Progreso

```json
{
  "total": 1124,
  "pending": 1124,
  "stub": 0,
  "wip": 0,
  "done": 0,
  "verified": 0,
  "current_depth": 0,
  "processing_order": ["$func_leaf1", "$func_leaf2", ...]
}
```

## Comandos del Makefile

```makefile
# Generar árbol de dependencias
make tree

# Crear scaffolding
make scaffold

# Procesar siguiente función
make next

# Procesar todas las hojas (depth 0)
make process-depth-0

# Ver progreso
make progress

# Verificar función específica
make verify f=func26
```

## Notas Importantes

1. **Ciclos**: Las funciones en ciclos se procesan como grupo
2. **Imports**: Los imports ($a.*) se mockean con funciones Python
3. **Memoria**: Usamos un array compartido `memory = bytearray(880 * 65536)`
4. **Globals**: Se convierten en variables de módulo Python
5. **call_indirect**: Requiere tabla de funciones Python

## Ejemplo de Traducción

### Input (WAT)
```wat
(func $func26 (param $var0 i32) (result i32)
  (local $var1 i32)
  i32.const 1
  local.get $var0
  local.get $var0
  i32.const 1
  i32.le_u
  select
  local.set $var0
  block $label0
    loop $label1
      local.get $var0
      call $$e
      local.tee $var1
      br_if $label0
      ...
    end
  end
  local.get $var1
)
```

### Output (Python)
```python
# tzar/memory/alloc.py
"""
Memory allocator for Tzar engine.

Original: $func26
Depth: 1
Calls: [$_e]
Called by: 170 functions
"""

from tzar._runtime import memory, call_e

def alloc(size: int) -> int:
    """Allocate memory block of given size."""
    var1 = 0

    # Ensure minimum size of 1
    size = 1 if size <= 1 else size

    while True:
        var1 = call_e(size)
        if var1:
            break
        # ... rest of logic

    return var1
```

## Siguiente Paso

¿Procedo con la implementación de la Fase 1 (Análisis de Dependencias)?
