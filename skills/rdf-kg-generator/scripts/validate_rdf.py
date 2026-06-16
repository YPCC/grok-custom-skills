#!/usr/bin/env python3
"""
Simple RDF syntax and basic compliance validator using rdflib.
Usage:
  python scripts/validate_rdf.py path/to/file.ttl
  cat file.ttl | python scripts/validate_rdf.py --stdin ttl
"""
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Validate RDF (Turtle/JSON-LD/etc) syntax and basic structure.")
    parser.add_argument("path", nargs="?", help="Path to RDF file")
    parser.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument("--format", default="auto", help="RDF format (ttl, json-ld, xml, n3, trig, auto)")
    args = parser.parse_args()

    try:
        import rdflib
    except ImportError:
        print("rdflib not installed. Install with: pip install rdflib")
        print("Then re-run this script.")
        sys.exit(2)

    g = rdflib.Graph()

    if args.stdin:
        data = sys.stdin.read()
        fmt = args.format if args.format != "auto" else "ttl"
        try:
            g.parse(data=data, format=fmt)
        except Exception as e:
            print(f"PARSE ERROR: {e}")
            sys.exit(1)
    elif args.path:
        try:
            if args.format == "auto":
                fmt = None  # let rdflib guess from extension
            else:
                fmt = args.format
            g.parse(args.path, format=fmt)
        except Exception as e:
            print(f"PARSE ERROR on {args.path}: {e}")
            sys.exit(1)
    else:
        print("Provide a file path or use --stdin")
        sys.exit(1)

    print(f"OK: Parsed successfully. {len(g)} triples.")
    # Basic checks
    types = set(g.objects(None, rdflib.RDF.type))
    print(f"Unique rdf:type values: {len(types)}")
    if len(g) == 0:
        print("WARNING: Graph is empty.")
    # Could add more checks: subjects with labels, etc.
    print("Basic validation passed.")

if __name__ == "__main__":
    main()