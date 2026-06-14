#!/usr/bin/env python3
"""
Helper script: split_okf_context.py

Takes output from code2prompt (especially when using okf-context.j2 template)
and creates an initial OKF skeleton bundle with directories and .md files
containing YAML frontmatter stubs + basic structure.

This accelerates the pipeline by turning the single context file into
a ready-to-enrich OKF directory tree.

Usage:
    python scripts/split_okf_context.py /tmp/repo_okf_context.md /home/workdir/artifacts/my-repo-okf-skeleton/
"""

import re
import sys
from pathlib import Path
from datetime import datetime

def parse_frontmatter_hints(content: str) -> dict:
    """Extract suggested type and tags from the simulated/hinted sections."""
    type_match = re.search(r'\*\*Suggested OKF Type\*\*:\s*(.+)', content)
    tags_match = re.search(r'\*\*Suggested Tags\*\*:\s*\[([^\]]+)\]', content)
    
    return {
        "type": type_match.group(1).strip() if type_match else "Source File",
        "tags": [t.strip() for t in tags_match.group(1).split(",")] if tags_match else ["repository-analysis"]
    }

def create_skeleton(context_path: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    
    content = context_path.read_text(encoding="utf-8")
    
    # Split by FILE: markers (our template uses this)
    file_sections = re.split(r'\n### FILE: ', content)
    
    created_files = []
    
    for section in file_sections[1:]:  # Skip header
        lines = section.strip().split('\n')
        if not lines:
            continue
            
        file_path = lines[0].strip()
        if not file_path:
            continue
            
        # Determine output path
        rel_path = Path(file_path)
        target_dir = output_dir / rel_path.parent
        target_dir.mkdir(parents=True, exist_ok=True)
        
        target_file = target_dir / (rel_path.stem + ".md")
        
        hints = parse_frontmatter_hints(section)
        
        frontmatter = f"""---
type: "{hints['type']}"
title: "{rel_path.name}"
description: "Auto-generated skeleton from code2prompt context. Enrich with summaries, relationships, and details."
resource: "{file_path}"
tags: {hints['tags']}
timestamp: "{datetime.now().isoformat()}"
okf_version: "0.1"
---

# {rel_path.name}

## Purpose
[To be filled by OKF enrichment step]

## Key Content
[Extracted from code2prompt context - see original file for full code/content]

## Relationships
[Add links to related concepts, e.g. [Architecture](../architecture.md)]

"""
        target_file.write_text(frontmatter, encoding="utf-8")
        created_files.append(str(target_file.relative_to(output_dir)))
    
    # Create basic root files if they don't exist
    root_files = {
        "overview.md": "Repository Overview",
        "architecture.md": "Architecture",
        "tech-stack.md": "Tech Stack",
        "log.md": "Generation Log"
    }
    
    for fname, title in root_files.items():
        fpath = output_dir / fname
        if not fpath.exists():
            fpath.write_text(f"""---
type: "{title}"
title: "{title}"
description: "Auto-generated skeleton. Enrich with content from code2prompt context and deeper analysis."
timestamp: "{datetime.now().isoformat()}"
okf_version: "0.1"
---

# {title}

[Content to be enriched]
""", encoding="utf-8")
            created_files.append(fname)
    
    print(f"Created {len(created_files)} skeleton files in {output_dir}")
    print("Next step: Run okf-repo-knowledge-generator to enrich these skeletons into a full OKF bundle.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    
    context_file = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    
    if not context_file.exists():
        print(f"Error: Context file not found: {context_file}")
        sys.exit(1)
    
    create_skeleton(context_file, out_dir)
