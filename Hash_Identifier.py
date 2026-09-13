import re

HASH_SIGNATURES = [
    {
        "match_type": "length",
        "value": 32,
        "algorithms": ["MD5", "NTLM", "MD4"],
        "note": "32 hex chars is the most ambiguous length.",
    },
    {
        "match_type": "prefix",
        "value": "$2b$",
        "algorithms": ["bcrypt"],
        "note": "bcrypt, current version identifier.",
    },
]


def normalize_input(raw_hash: str) -> str:
    return raw_hash.strip()


def is_hex(value: str) -> bool:
    return bool(re.fullmatch(r"[0-9a-fA-F]+", value))


def identify_hash(raw_hash: str) -> list:
    cleaned = normalize_input(raw_hash)
    matches = []

    for signature in HASH_SIGNATURES:
        if signature["match_type"] == "prefix" and cleaned.startswith(signature["value"]):
            matches.append(signature)
    if matches:
        return matches

    if is_hex(cleaned):
        for signature in HASH_SIGNATURES:
            if signature["match_type"] == "length" and len(cleaned) == signature["value"]:
                matches.append(signature)

    return matches


def print_results(raw_hash: str, matches: list) -> None:
    cleaned = normalize_input(raw_hash)
    print(f"Input: {cleaned}")
    print(f"Length: {len(cleaned)} characters")

    if not matches:
        print("Result: No known format matched.")
        return

    for signature in matches:
        algo_list = ", ".join(signature["algorithms"])
        confidence = "High" if len(signature["algorithms"]) == 1 else "Low (ambiguous)"
        print(f"Possible algorithm(s): {algo_list}")
        print(f"Confidence: {confidence}")
        print(f"Note: {signature['note']}")


def main() -> None:
    while True:
        user_input = input("Hash> ")
        if user_input.strip().lower() == "exit":
            break
        if not user_input.strip():
            print("No input detected")
            continue
        matches = identify_hash(user_input)
        print_results(user_input, matches)


if __name__ == "__main__":
    main()