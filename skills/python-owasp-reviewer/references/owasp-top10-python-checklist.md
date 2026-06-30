# OWASP Top 10 — Python Web Application Checklist

Use during Step 5 of the review workflow. Mark each item **Pass**, **Fail**, or **N/A** with evidence.

## A01 — Broken Access Control

- [ ] Every mutating endpoint requires authentication
- [ ] Object-level authorization: user can only access own resources (IDOR tested)
- [ ] Admin/privileged routes gated by role, not just authentication
- [ ] Directory traversal blocked on file download endpoints
- [ ] CORS does not replace server-side authorization
- [ ] JWT/session cannot be swapped across tenants

## A02 — Cryptographic Failures

- [ ] No secrets, API keys, or passwords in source or git history
- [ ] Passwords hashed with bcrypt/argon2/scrypt (not MD5/SHA1)
- [ ] `DEBUG=False` in production config paths
- [ ] TLS enforced; no `verify=False` on outbound HTTPS without justification
- [ ] Sensitive data encrypted at rest where required
- [ ] Cookies: `HttpOnly`, `Secure`, `SameSite` set appropriately

## A03 — Injection

- [ ] All SQL uses parameterized queries or ORM (no f-strings in SQL)
- [ ] No `os.system`, `eval`, `exec` on user input
- [ ] `subprocess` uses list args, `shell=False`
- [ ] Templates auto-escape; no `|safe` on user content
- [ ] `yaml.safe_load` only (never `yaml.load`)
- [ ] No `pickle.loads` on untrusted bytes

## A04 — Insecure Design

- [ ] Rate limiting on auth and expensive endpoints
- [ ] Account enumeration mitigated on login/register
- [ ] Threat model documented for sensitive flows
- [ ] Multi-step actions use anti-replay (nonce, idempotency keys)

## A05 — Security Misconfiguration

- [ ] CORS `allow_origins` is explicit (not `*` with credentials)
- [ ] Default framework accounts disabled
- [ ] Error responses do not leak stack traces in production
- [ ] OpenAPI/Swagger admin UIs disabled or protected in prod
- [ ] Security headers present (CSP, X-Frame-Options, etc.)

## A06 — Vulnerable and Outdated Components

- [ ] Dependencies pinned in lockfile
- [ ] No known critical CVEs in direct dependencies (`pip-audit` / `safety`)
- [ ] Python runtime version supported and patched

## A07 — Identification and Authentication Failures

- [ ] Session timeout and secure session storage
- [ ] JWT: short expiry, proper `aud`/`iss`, strong signing key
- [ ] Password policy enforced server-side
- [ ] MFA available for privileged operations (if applicable)
- [ ] Logout invalidates server-side session

## A08 — Software and Data Integrity Failures

- [ ] Webhooks verified with HMAC/signatures
- [ ] CI/CD artifacts signed or checksum-verified
- [ ] Deserialization limited to safe formats (JSON, not pickle)

## A09 — Security Logging and Monitoring Failures

- [ ] Failed logins and privilege changes logged
- [ ] Logs exclude passwords and tokens
- [ ] Alerting on anomaly patterns (optional but note gap)

## A10 — Server-Side Request Forgery (SSRF)

- [ ] Outbound HTTP clients block private IP ranges and metadata URLs
- [ ] URL fetch features use allowlists where possible
- [ ] Redirect following disabled or restricted on user-supplied URLs