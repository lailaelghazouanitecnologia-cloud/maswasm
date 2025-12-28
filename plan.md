# Plan de Transpilación WAT → Python

## Objetivo
Transpilar automáticamente las 1098 funciones del juego Tzar de WebAssembly (WAT) a Python ejecutable.

## Arquitectura

```
tools/transpiler/
├── wat_parser.py      # Parser WAT → AST
├── analyzer.py        # Análisis estático (tipos, flujo, patrones)
├── codegen.py         # Generador de código Python
├── optimizer.py       # Optimizaciones post-generación
└── transpile.py       # CLI principal

tzar/                  # Código generado
├── _runtime.py        # Runtime (memory, globals, imports)
├── memory/            # Funciones de memoria (func26, func38, etc.)
├── entities/          # Manejo de entidades del juego
├── players/           # Lógica de jugadores
├── render/            # Renderizado
├── input/             # Input handling
├── game/              # Lógica principal del juego
└── exports.py         # Funciones exportadas

legacy/                # Código manual anterior (referencia)
```

## Fases

### Fase 1: Parser WAT (✓ En progreso)
- [x] Estructura básica del parser
- [ ] Parsing completo de instrucciones
- [ ] Manejo de bloques anidados (block, loop, if/else)
- [ ] Extracción de metadatos (exports, imports)

### Fase 2: Análisis Estático
- [ ] Inferencia de tipos para variables locales
- [ ] Análisis de flujo de control
- [ ] Detección de patrones comunes:
  - Acceso a estructuras (player[i], entity[i])
  - Operaciones SWAR
  - Loops de copia de memoria
- [ ] Grafo de dependencias entre funciones
- [ ] Categorización automática (memory, entity, player, etc.)

### Fase 3: Generador de Código
- [ ] Mapeo de instrucciones WAT → Python
- [ ] Manejo de stack virtual
- [ ] Generación de control flow (if/else, loops)
- [ ] Inlining de operaciones simples
- [ ] Generación de docstrings automáticos

### Fase 4: Transpilación en Batch
- [ ] Agrupar funciones por categoría (~2000 líneas/módulo)
- [ ] Resolver dependencias circulares
- [ ] Generar imports automáticos
- [ ] Crear estructura de proyecto

### Fase 5: Refinamiento
- [ ] Tests de equivalencia (comparar output WAT vs Python)
- [ ] Optimización de código generado
- [ ] Documentación automática
- [ ] Limpieza manual de casos edge

## Mapeo de Instrucciones WAT → Python

| WAT | Python |
|-----|--------|
| `i32.const N` | `N` |
| `local.get $var` | `var` |
| `local.set $var` | `var = ...` |
| `i32.load` | `i32_load(addr)` |
| `i32.store` | `i32_store(addr, val)` |
| `i32.add` | `a + b` |
| `i32.sub` | `a - b` |
| `i32.mul` | `a * b` |
| `i32.and` | `a & b` |
| `i32.or` | `a \| b` |
| `i32.xor` | `a ^ b` |
| `i32.shl` | `a << b` |
| `i32.shr_s` | `a >> b` |
| `i32.shr_u` | `(a & 0xFFFFFFFF) >> b` |
| `i32.eq` | `1 if a == b else 0` |
| `i32.ne` | `1 if a != b else 0` |
| `i32.lt_s` | `1 if a < b else 0` |
| `i32.eqz` | `1 if a == 0 else 0` |
| `call $func` | `func(...)` |
| `block $label` | `# block` + break handling |
| `loop $label` | `while True:` |
| `br $label` | `break` / `continue` |
| `br_if $label` | `if cond: break` |
| `return` | `return` |
| `select` | `a if cond else b` |

## Estructura de Memoria del Juego

```
Direcciones conocidas:
- 9142424: Game state base
- 9142872: Current player index
- 9142892: Player count
- 9561692: Player array base
- 9568096: Entity type table
- 9671128: Entity array base

Strides:
- Player: 286704 bytes
- Entity: 132 bytes
- Entity Type: 404 bytes
```

## Comandos

```bash
# Transpilar todo
python tools/transpiler/transpile.py mgame --output tzar/

# Transpilar una función
python tools/transpiler/transpile.py mgame --function func26

# Analizar sin generar
python tools/transpiler/transpile.py mgame --analyze-only

# Verificar equivalencia
python tools/transpiler/test.py --compare func26
```

## Timeline Estimado

1. **Parser completo**: 1-2 horas
2. **Análisis estático básico**: 1-2 horas
3. **Generador v1**: 2-3 horas
4. **Batch transpile**: 1 hora
5. **Refinamiento**: Continuo

Total para MVP funcional: ~6-8 horas de trabajo

## Notas

- Priorizar funciones exportadas (305 total)
- Las funciones de memoria (func26, func38) son críticas
- Muchas funciones son simples wrappers
- El 80% del código son patrones repetitivos
