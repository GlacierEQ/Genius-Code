# Evidence Receipt: ev-property-sort-001

| Field | Value |
|-------|-------|
| Claim | `code-testing-property-001` |
| Challenge | `ch-property-sort-001` |
| Kind | property_test |
| Result | **pass** |
| Timestamp | 2026-08-29T20:50:00Z |
| Reproducible | true |

## Command

```bash
python3 -m pytest verification/properties/test_sort_properties.py -q
```

## Environment

- Python 3.12.3
- Hypothesis 6.165.10
- Linux x86_64 (glibc 2.39)

## Artifacts

- `verification/properties/test_sort_properties.py` sha256 `2957a805c6c2af65e51c2d91bfdbdd6e0c0f3bf39f135f62d9b9f5231e72a932`
- `implementations/reference/sorts.py` sha256 `80b65f396bb9d47bf043ffec044e0a0c6886cbb4723592e0cb4b5562311f4590`

## Outcome

- Correct implementation: properties hold.
- Broken implementation (`broken_sort_drop_last`): properties fail as required by the challenge success criteria.
- This advances the claim from pure mapping toward adversarial verification of the *method* (property testing finds the bug class).
