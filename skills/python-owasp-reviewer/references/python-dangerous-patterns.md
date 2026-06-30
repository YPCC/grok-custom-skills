# Python Dangerous Patterns — Search Reference

Run these searches (ripgrep) during taint analysis. Each hit requires manual review.

## Injection & code execution

```
os\.system\(
subprocess\.(call|run|Popen).*shell\s*=\s*True
eval\(
exec\(
__import__\(
pickle\.loads?
yaml\.load\(
marshal\.loads
```

## SQL injection indicators

```
cursor\.execute\(f["']
cursor\.execute\(["'].*%.*\+
\.execute\(.*\.format\(
sqlalchemy\.text\(f["']
\.raw\(
\.extra\(
```

## Secrets & misconfiguration

```
DEBUG\s*=\s*True
allow_origins\s*=\s*\[["']\*["']
verify\s*=\s*False
password\s*=\s*["'][^"']+["']
api[_-]?key\s*=\s*["']sk_
SECRET_KEY\s*=\s*["'][^"']+["']
```

## SSRF

```
requests\.(get|post|put)\([^)]*\+
httpx\.(get|post)\([^)]*\+
urllib\.request\.urlopen\(
```

## FastAPI / Flask / Django auth gaps

```
# FastAPI — route without Depends
@(app|router)\.(get|post|put|delete|patch)

# Flask
@app\.route.*\n(?!.*@login_required)

# Django
@csrf_exempt
ALLOWED_HOSTS\s*=\s*\[.*\*.*\]
```

## Template XSS

```
\|safe
Markup\(
autoescape\s*=\s*False
```

## Bandit (automated)

```bash
bandit -r <target_dir> -f json -ll
pip-audit -r requirements.txt   # if requirements.txt exists
```