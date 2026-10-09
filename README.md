# DevSecOps Security Pipeline

A starter CI quality gate for Python repositories. Runs unit tests and checks source files for selected high-risk patterns. This intentionally small scanner is not a substitute for a dedicated secret scanner, SAST, or dependency audit.

## Run
Python 3.11+; standard library only.

```bash
python app.py .
python -m unittest discover -s tests -v
```

## Safety
Do not put real credentials into test fixtures. If a secret is found, revoke it first; removing a string from Git history does not revoke the credential.

## License
MIT
