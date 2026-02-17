import os
from pathlib import Path

# --- Configuration ---
SYLLABUS = [
    # Módulo 1: Fundamentos do Design e Figma
    {"id": 1, "module": "Módulo 1 – Fundamentos", "title": "Introdução ao Design de Interfaces e Instalação"},
    {"id": 2, "module": "Módulo 1 – Fundamentos", "title": "Explorando a Interface do Figma"},
    {"id": 3, "module": "Módulo 1 – Fundamentos", "title": "Ferramentas Básicas: Formas e Vetores"},
    {"id": 4, "module": "Módulo 1 – Fundamentos", "title": "Manipulação de Textos e Tipografia"},
    
    # Módulo 2: Cores e Estilos
    {"id": 5, "module": "Módulo 2 – Cores e Estilos", "title": "Teoria das Cores e Aplicação no Figma"},
    {"id": 6, "module": "Módulo 2 – Cores e Estilos", "title": "Gerenciamento de Estilos (Styles)"},
    {"id": 7, "module": "Módulo 2 – Cores e Estilos", "title": "Trabalhando com Imagens e Máscaras"},
    
    # Módulo 3: Layout e Estrutura
    {"id": 8, "module": "Módulo 3 – Layout e Estrutura", "title": "Auto Layout: Fundamentos"},
    {"id": 9, "module": "Módulo 3 – Layout e Estrutura", "title": "Auto Layout: Avançado e Responsividade"},
    {"id": 10, "module": "Módulo 3 – Layout e Estrutura", "title": "Constraints e Grids"},
    
    # Módulo 4: Componentes e Sistemas
    {"id": 11, "module": "Módulo 4 – Componentes e Sistemas", "title": "Componentes Básicos e Instâncias"},
    {"id": 12, "module": "Módulo 4 – Componentes e Sistemas", "title": "Variantes e Propriedades de Componentes"},
    {"id": 13, "module": "Módulo 4 – Componentes e Sistemas", "title": "Bibliotecas e Design Systems"},
    
    # Módulo 5: Prototipagem e Finalização
    {"id": 14, "module": "Módulo 5 – Prototipagem", "title": "Prototipagem: Navegação e Interações"},
    {"id": 15, "module": "Módulo 5 – Prototipagem", "title": "Animações (Smart Animate) e Microinterações"},
    {"id": 16, "module": "Módulo 5 – Prototipagem", "title": "Hand-off para Desenvolvedores e Exportação"},
]

DIRS = [
    "docs/aulas",
    "docs/slides/.src",  # Atualizado para .src
    "docs/quizzes/.src", # Atualizado para .src
    "docs/exercicios",
    "docs/projetos",
    "docs/assets/images"
]

# --- Templates ---

TEMPLATE_AULA = """# {title}

## Objetivos da Aula
- [ ] Compreender os conceitos de {title}.
- [ ] Praticar as ferramentas relacionadas no Figma.
- [ ] Criar um exemplo prático.

## Conteúdo Teórico

### O que é?
Explicação teórica sobre o tema da aula...

### Como funciona no Figma?
Passo a passo de como utilizar a ferramenta ou técnica...

1.  Passo 1...
2.  Passo 2...
3.  Passo 3...

!!! tip "Dica de Pro"
    Utilize atalhos de teclado para agilizar seu fluxo de trabalho.

## Em Prática
Vamos aplicar o que aprendemos criando...

## Resumo
Nesta aula aprendemos sobre:
- Conceito A
- Conceito B
- Conceito C

---
## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :material-presentation: **Acessar Slides**
    -   [Ver Slides da Aula](../slides/slide-{id:02d}.html)

-   :material-school: **Quiz**
    -   [Responder Quiz](../quizzes/quiz-{id:02d}.html)

-   :material-dumbbell: **Exercícios**
    -   [Lista de Exercícios](../exercicios/exercicio-{id:02d}.md)

-   :material-rocket: **Projeto**
    -   [Mini Projeto](../projetos/projeto-{id:02d}.md)

</div>
"""

TEMPLATE_SLIDE = """---
theme: material
---

# {title}
## Aula {id:02d}

---

## Objetivos
- Entender {title}
- Dominar as ferramentas do Figma
- Aplicar em projetos reais

---

## Conceito Principal
Definição do conceito...

- Ponto 1
- Ponto 2
- Ponto 3

---

## Demonstração no Figma
> [!NOTE]
> Acompanhe a demonstração prática.

1. Selecione a ferramenta
2. Aplique a propriedade
3. Veja o resultado

---

## Resumo
- Recapitulando ponto A
- Recapitulando ponto B

---

<!-- _class: lead -->
# Próxima Aula: ...
"""

TEMPLATE_QUIZ = """# Quiz {id:02d}: {title}

**Teste seus conhecimentos.**

1. Qual a principal função de {title}?
    - [ ] Função incorreta A
    - [x] Função correta
    - [ ] Função incorreta B

2. Qual atalho é usado para esta ferramenta?
    - [ ] Ctrl + A
    - [x] Tecla correta
    - [ ] Alt + F4
"""

TEMPLATE_EXERCICIO = """# Exercícios Aula {id:02d}

## Nível: Fácil
1. Crie um arquivo novo no Figma e...
2. Desenhe formas básicas...

## Nível: Médio
3. Utilizando o que aprendeu, recrie a interface...
4. Organize suas camadas...

## Nível: Difícil
5. Crie um componente completo com...
"""

TEMPLATE_PROJETO = """# Projeto Aula {id:02d}

## Descrição
Desenvolva uma tela de aplicativo que utilize {title}...

## Requisitos
- [ ] Usar Frames corretos (ex: iPhone 14)
- [ ] Aplicar Grids
- [ ] Utilizar os estilos definidos

## Desafio
Tente adicionar uma interação avançada de...
"""

TEMPLATE_INDEX = """# Curso Profissional de Design de Interfaces com Figma

## O Curso
Domine o Figma do zero ao avançado e crie interfaces modernas e profissionais.

## Estrutura
- **16 Módulos Práticos**
- **16 Projetos Reais**
- **Certificado de Conclusão** (Simulado)

## Conteúdo Programático

<div class="grid cards" markdown>

-   :material-rocket: **Começar Agora**
    -   [Ir para Aula 01](aulas/aula-01.md)

</div>
"""

# --- Execution ---

def create_files():
    # 1. Ensure Directories
    for d in DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    # 2. Create Index if missing
    # Always recreate/overwrite index for this migration
    Path("docs/index.md").write_text(TEMPLATE_INDEX, encoding="utf-8")
    print("Created index.md")

    # 3. Generate Content
    for lesson in SYLLABUS:
        lid = lesson["id"]
        title = lesson["title"]
        
        # Paths
        p_aula = Path(f"docs/aulas/aula-{lid:02d}.md")
        p_slide = Path(f"docs/slides/.src/slide-{lid:02d}.md") # .src
        p_quiz = Path(f"docs/quizzes/.src/quiz-{lid:02d}.md")  # .src
        p_exerc = Path(f"docs/exercicios/exercicio-{lid:02d}.md")
        p_proj = Path(f"docs/projetos/projeto-{lid:02d}.md")
        
        # Write Files (Overwrite if exists to ensure updates)
        p_aula.write_text(TEMPLATE_AULA.format(id=lid, title=title), encoding="utf-8")
        p_slide.write_text(TEMPLATE_SLIDE.format(id=lid, title=title), encoding="utf-8")
        p_quiz.write_text(TEMPLATE_QUIZ.format(id=lid, title=title), encoding="utf-8")
        p_exerc.write_text(TEMPLATE_EXERCICIO.format(id=lid, title=title), encoding="utf-8")
        p_proj.write_text(TEMPLATE_PROJETO.format(id=lid, title=title), encoding="utf-8")
            
        print(f"Generated Lesson {lid:02d}: {title}")

def generate_nav_yaml():
    nav = ["nav:", "  - Home: index.md"]
    
    nav.append("  - Aulas:")
    nav.append("      - aulas/index.md")
    
    current_module = None
    
    for lesson in SYLLABUS:
        module = lesson["module"]
        title = lesson["title"]
        lid = lesson["id"]
        filename = f"aulas/aula-{lid:02d}.md"
        
        if module != current_module:
            nav.append(f"      - {module}:")
            current_module = module
        
        nav.append(f"        - 'Aula {lid:02d} - {title}': {filename}")
    
    nav.append("  - Materiais:")
    nav.append("      - materiais.md")
    nav.append("      - Slides: slides/index.md")
    nav.append("      - Exercícios: exercicios/index.md")
    nav.append("      - Quizzes:")
    nav.append("          - quizzes/index.md") 
    
    nav.append("      - Projetos: projetos/")
    nav.append("      - Setups: setups/index.md")
    nav.append("  - Impressão: print_page.md")
    
    return "\n".join(nav)

def update_mkdocs():
    mkdocs_path = Path("mkdocs.yml")
    if not mkdocs_path.exists():
        print("mkdocs.yml not found!")
        return

    content = mkdocs_path.read_text(encoding="utf-8")
    
    # Simple replace of nav section
    if "nav:" in content:
        content = content.split("nav:")[0]
    
    new_nav = generate_nav_yaml()
    
    final_content = content.strip() + "\n\n" + new_nav + "\n"
    mkdocs_path.write_text(final_content, encoding="utf-8")
    print("Updated mkdocs.yml navigation")

if __name__ == "__main__":
    create_files()
    update_mkdocs()
