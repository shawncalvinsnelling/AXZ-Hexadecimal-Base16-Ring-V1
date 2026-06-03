from pathlib import Path
import json
from axz_hexadecimal_base16_ring_v1.core import compute_certificate

ROOT = Path(__file__).resolve().parents[1]

def main():
    cert = compute_certificate()
    out = ROOT / "certificates" / "generated_certificate.check.json"
    out.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    print("PASS: GENERATED_CERTIFICATE")
    print(out)

if __name__ == "__main__":
    main()
