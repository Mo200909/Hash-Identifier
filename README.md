# Hash-Identifier
r

Terminal tool that guesses which hashing algorithm produced a given hash, based on its length and format.

## Usage

```bash
python hash_identifier.py
```

Paste a hash when prompted. Type `exit` to quit.

## Example

```
Hash> 5f4dcc3b5aa765d61d8327deb882cf99
Possible algorithm(s): MD5, NTLM, MD4
Confidence: Low (ambiguous)
```

## What it detects

- 32 hex chars → MD5 / NTLM / MD4 (ambiguous)
- 40 hex chars → SHA-1
- 64 hex chars → SHA-256
- `$2b$` prefix → bcrypt

## Limitations

Identifies format only — does not crack or verify hashes.

## Requirements

Python 3.8+, no external dependencies.
