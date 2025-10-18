# fiscalcode-utils

🇮🇹 **fiscalcode-utils** is a Python project that lets you generate and verify Italian *Codice Fiscale* codes.

The generation logic is based on the official rules used in Italy:
- Surname and name consonants
- Birth date and gender
- Encoded birth municipality (Codice Catastale)

The validator checks whether a given fiscal code is syntactically correct based on these rules.

---

## What you can do with it

- **Generate** a codice fiscale from your personal information (name, surname, gender, date of birth, and city of birth)
- **Validate** an existing codice fiscale and confirm if it is syntactically correct
- Works with real Italian municipality codes (loaded from CSV)

---

