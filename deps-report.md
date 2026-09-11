# Dependency Report

Scope: `src/orders/api.py` (plus the modules it pulls in transitively)
Generated: 2026-09-11
Environment: `.venv` — CPython 3.11.16 (project requires `>=3.10`)

## 1. Dependencies of `src/orders/api.py`

### Standard library
| Module | Notes |
| --- | --- |
| `logging` | Module-level `logger`; used for the refund failure path. |

### Internal (first-party)
| Module | Imported as | Pulls in |
| --- | --- | --- |
| `orders.store` | `from orders import store` | `orders.models` |
| `orders.service` | `from orders.service import cancel_order, refund_order` | `logging`, `orders.store`, `orders.models` |

Transitive closure from `api.py`:

```
orders/api.py
├── logging                (stdlib)
├── orders/store.py
│   └── orders/models.py
│       └── dataclasses    (stdlib)
└── orders/service.py
    ├── logging            (stdlib)
    ├── orders/store.py
    └── orders/models.py
```

### Third-party
**None.** `api.py` and its entire internal import closure use only the standard
library. Nothing in `src/orders/` imports a third-party package.

## 2. Declared project dependencies

| Source | Declaration | Constraint |
| --- | --- | --- |
| `pyproject.toml` → `[project].dependencies` | *(empty list)* | — |
| `pyproject.toml` → `[project.optional-dependencies].dev` | `pytest` | unpinned |
| `pyproject.toml` → `[build-system].requires` | `setuptools>=61` | lower bound only |
| `requirements.txt` | `-e .[dev]` | delegates to `pyproject.toml` |

The only declared dependency reachable at runtime is *nothing*; `pytest` is
test-only and is imported solely by `tests/test_service.py`.

## 3. Installed packages vs. latest

| Package | Installed | Latest | Status | Role |
| --- | --- | --- | --- | --- |
| pytest | 9.1.1 | 9.1.1 | current | dev / declared |
| pluggy | 1.6.0 | 1.6.0 | current | transitive (pytest) |
| iniconfig | 2.3.0 | 2.3.0 | current | transitive (pytest) |
| packaging | 26.3 | 26.3 | current | transitive (pytest) |
| Pygments | 2.21.0 | 2.21.0 | current | transitive (pytest) |
| keysoft-sample-project | 0.1.0 | — | local editable install | this project |
| setuptools | 79.0.1 | 84.0.0 | **outdated** | build/tooling |
| pip | 24.0 | 26.2.1 | **outdated** | tooling |

## 4. Outdated dependencies

Two findings, both in the toolchain rather than in the project's own dependency
set — no application or test dependency is behind.

1. **setuptools 79.0.1 → 84.0.0** (build backend, `[build-system].requires`)
   - Impact: low. The build is a plain `setuptools.build_meta` src-layout build;
     the declared floor is `>=61`, so 79 already satisfies it.
   - Recommendation: refresh at the next environment rebuild. No source changes
     needed.

2. **pip 24.0 → 26.2.1** (environment tooling, not a project dependency)
   - Impact: low, but 24.0 predates several resolver and metadata fixes.
   - Recommendation: `.venv/bin/python -m pip install --upgrade pip`.

## 5. Other observations

- **`pytest` is unpinned.** `dev = ["pytest"]` accepts any version, including a
  future major that changes fixture or assertion behaviour. Consider a compatible
  bound such as `pytest>=9,<10` so CI stays reproducible.
- **No lockfile.** `requirements.txt` only forwards to `pyproject.toml`
  (`-e .[dev]`), so the exact transitive set (pluggy, iniconfig, packaging,
  Pygments) is resolved fresh on every install. If reproducible test runs matter,
  add a compiled lock (`requirements.lock` / `uv.lock`).
- **Zero-dependency runtime is a strength.** `src/orders/` is pure stdlib, so the
  order service currently carries no third-party supply-chain surface. Worth
  preserving deliberately when adding an HTTP layer.
- **`.venv/` is present in the working tree** but is correctly ignored
  (`.gitignore` line 153), so installed packages are not committed.
