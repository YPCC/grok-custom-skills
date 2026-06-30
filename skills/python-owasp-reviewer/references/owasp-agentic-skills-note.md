# OWASP Agentic Skills Top 10 — Supplemental Review

Apply when the codebase includes **AI agents**, **MCP servers**, **SKILL.md** files, or **tool-calling** workflows.

Reference: [OWASP Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10)

## Quick mapping for Python agent code

| AST | Risk | Python/agent patterns |
|-----|------|----------------------|
| AST01 | Malicious skills | Hidden `exec`/`eval` in skill scripts; prose instructions that override safety |
| AST02 | Supply chain | Unpinned deps in skill packages; unsigned skill updates |
| AST03 | Over-privileged | Tools with full shell, broad file read (`**/*`), shared API keys |
| AST04 | Insecure metadata | Skill `description` mismatches behavior; unsafe YAML tags |
| AST05 | External instructions | Runtime `fetch()` of unpinned URLs in SKILL.md |
| AST06 | Weak isolation | Agent tools run on host without sandbox |
| AST07 | Update drift | Skills auto-update without hash pinning |
| AST08 | Poor scanning | Relying only on regex; no behavioral test |
| AST09 | No governance | No audit log of tool invocations |
| AST10 | Cross-platform | Security metadata dropped when porting skills |

## Python agent-specific checks

- [ ] User/agent prompts not passed directly to `subprocess` or SQL
- [ ] Tool outputs sanitized before rendering in HTML/logs
- [ ] MCP tools declare minimal permissions; no blanket `all` access
- [ ] `.env.local` / secrets never read by skills beyond stated scope
- [ ] `CallMcpTool` / HTTP tools validate URLs (SSRF)
- [ ] Human-in-the-loop for destructive actions (delete, deploy, send email)

## Skill file review (SKILL.md)

When reviewing a Grok/Cursor skill:

1. Read `description` — does it match actual instructions?
2. Scan for external URL dependencies (AST05)
3. Check scripts/ for shell execution and credential access (AST01, AST03)
4. Verify no instructions to ignore security policies or exfiltrate data
5. Cross-check against [OWASP checklist](https://raw.githubusercontent.com/OWASP/www-project-agentic-skills-top-10/main/checklist.md)