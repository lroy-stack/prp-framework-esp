# prp-framework-esp — PRP Framework ecosystem, partially translated to Spanish

No live demo. A one-day project from 19 July 2025 that was left unfinished.

## What it is

A working repository for translating three open-source AI-assisted development frameworks into Spanish, built
around the same methods it translates (Product Requirement Prompts, Context Engineering and Claude Code commands).
It holds copies of the original frameworks, a partial Spanish translation of them, and a few helper scripts. Part
of the material is a Spanish overview of how the three fit together as a learning path: Context Engineering
Intro, then PRPs Agentic Engineering, then SuperClaude.

## What is in it

- `Context-Engineering-Intro/`, `PRPs-agentic-eng/`, `SuperClaude_Framework-master/`: copies of the
  upstream projects, kept as the translation source.
- `prp-framework-esp/repositorios/`: the translated files so far, for Context Engineering Intro, PRPs Agentic
  Engineering and an MCP server example. SuperClaude has not been translated.
- `prp-framework-esp/PRPs/`: four PRPs that describe and drive the translation work.
- `prp-framework-esp/herramientas/`: two Python scripts, a terminology validator and a version synchroniser.
- `prp-framework-esp/configuracion/`: a master glossary, translation rules and a source-to-target file map.
- `prp-framework-esp/CLAUDE.md` and `uso-comandos.md`: a Spanish guide to working in the repository with Claude Code.
- `img-docs/`: diagrams used by the root README.

The progress figures and productivity claims in the earlier README were not measured, so they are not repeated here.

## Credits

The upstream material belongs to its authors and keeps their licences:

- Context Engineering Intro by Cole Medin, MIT (`Context-Engineering-Intro/LICENSE`).
- SuperClaude Framework by the SuperClaude Framework Contributors, MIT (`SuperClaude_Framework-master/LICENSE`).
- PRPs Agentic Engineering: a copy of the upstream repository of the same name; check its original licence before
  reusing it, as the copy carries no licence file.

## Use it

Open the folder with Claude Code and read `prp-framework-esp/CLAUDE.md` and `prp-framework-esp/uso-comandos.md`
for the workflow. The scripts need only Python 3 (inspect their `--help` for options).

## Layout

```
Context-Engineering-Intro/       upstream copy
PRPs-agentic-eng/                upstream copy
SuperClaude_Framework-master/    upstream copy
prp-framework-esp/               translation workspace: repositorios, PRPs, herramientas, configuracion, docs
img-docs/                        diagrams
```

---

Versión en español: repositorio de trabajo para traducir al español el ecosistema PRP (Context Engineering Intro,
PRPs Agentic Engineering, SuperClaude), con copias del original, traducción parcial, glosario y scripts de
validación. Quedó sin terminar tras un día de trabajo en julio de 2025.
