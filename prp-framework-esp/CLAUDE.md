# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **PRP Framework Spanish Translation Infrastructure** - a comprehensive system for translating and localizing the PRP Framework ecosystem to Spanish. The project uses Python automation tools to ensure translation quality, consistency, and maintainability.

## Architecture

### Key Components

- **`herramientas/`** - Python automation scripts for translation workflow
- **`repositorios/`** - Translated content organized by framework
- **`configuracion/`** - System configuration and terminology management
- **`metadatos/`** - Project state tracking and metrics
- **`flujos-trabajo/`** - Process documentation and workflows

### Translation Tools

**Core Scripts**:
- `sincronizador-versiones.py` - Syncs with original repositories and tracks changes
- `validador-terminologia.py` - Validates terminology consistency using master glossary
- Configuration files in `configuracion/` define translation rules and mappings

## Development Commands

### Translation Workflow
```bash
# Sync with original repositories
python herramientas/sincronizador-versiones.py --update

# Check system status
python herramientas/sincronizador-versiones.py --status

# Validate terminology in translated files
python herramientas/validador-terminologia.py --archivo file-es.md

# Validate all repositories
python herramientas/validador-terminologia.py --verificar-todo

# Show glossary statistics
python herramientas/validador-terminologia.py --estadisticas
```

### Quality Control
```bash
# Generate validation report
python herramientas/validador-terminologia.py --directorio repositorios/context-engineering-intro-esp/ --reporte reporte.md

# Compare original and translated files
python herramientas/sincronizador-versiones.py --comparar README.md README-es.md
```

## Configuration System

### Master Glossary
- Located at `configuracion/glosario-maestro.json`
- Defines which terms to translate vs preserve in original language
- Used by validation tools for consistency checking

### Translation Rules
- `configuracion/reglas-traduccion.yaml` - Comprehensive translation standards
- Defines patterns for preserving code, links, and technical terms
- Specifies cultural adaptations and formatting standards

### File Mappings
- `configuracion/mapeo-archivos.json` - Maps source files to translation targets
- Tracks relationships between original and translated content

## Quality Standards

### Validation Requirements
- **Terminology consistency**: ≥95% accuracy against master glossary
- **Structure preservation**: 100% maintenance of Markdown formatting
- **Code functionality**: 100% preservation of code examples and commands
- **Link integrity**: All internal and external links must remain functional

### Translation Principles
1. **Preserve technical terms** as defined in master glossary
2. **Maintain Markdown structure** and formatting
3. **Keep code blocks unchanged** except for comments when clearly marked
4. **Adapt examples culturally** when relevant (companies, locations)
5. **Use consistent terminology** throughout all translations

## Frameworks Being Translated

1. **Context Engineering Intro** - Foundational template for context engineering
2. **PRPs Agentic Engineering** - Professional prompt collection  
3. **SuperClaude Framework** - Advanced AI command and persona system

## State Management

### Project Tracking
- `metadatos/estado-general.json` - Global project state and progress
- `metadatos/metricas-baseline.json` - Quality metrics and baselines
- State automatically updated by synchronization and validation tools

### Current Status
- **Total identified files**: 142
- **Translation progress**: In initial phase
- **Tools developed**: Core validation and sync infrastructure complete

## Development Guidelines

### Working with Translation Tools
- Always run `--status` before starting work to understand current state
- Use validation tools during translation process, not just at the end
- Update master glossary when encountering new technical terms
- Run full validation before committing translated content

### Code Contributions
- Follow existing Python code patterns in `herramientas/`
- Maintain comprehensive error handling and logging
- Use type hints and dataclasses for complex data structures
- Include CLI argument parsing for all automation scripts

### File Naming Conventions
- Original: `filename.md`
- Translated: `filename-es.md`
- Reports: Use descriptive names with timestamps
- Configuration: Use kebab-case with clear purposes

## Error Handling

### Common Issues
- **Terminology inconsistencies**: Use validation tools to identify and resolve
- **Broken links**: Check both internal references and external URLs
- **Structure changes**: Compare with original using sync tools
- **Encoding problems**: Ensure UTF-8 encoding for all Spanish content

### Troubleshooting
- Check logs for detailed error information
- Use `--estadisticas` flag to understand glossary coverage
- Validate incrementally during translation process
- Use comparison tools to identify structural differences