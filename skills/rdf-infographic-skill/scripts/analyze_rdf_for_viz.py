#!/usr/bin/env python3
"""
Quick RDF analysis helper for rdf-infographic-skill.
Extracts key stats, main entities, classes present, and suggests visualization focus areas.
Usage: python scripts/analyze_rdf_for_viz.py path/to/file.ttl [--format ttl]
"""
import sys
import argparse
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to RDF file")
    parser.add_argument("--format", default="auto", help="RDF format (ttl, json-ld, xml, auto)")
    args = parser.parse_args()

    try:
        import rdflib
        from rdflib.namespace import RDF, RDFS, SCHEMA
    except ImportError:
        print("rdflib not installed. Run: pip install rdflib")
        sys.exit(2)

    g = rdflib.Graph()
    try:
        if args.format == "auto":
            g.parse(args.path)
        else:
            g.parse(args.path, format=args.format)
    except Exception as e:
        print(f"Failed to parse RDF: {e}")
        sys.exit(1)

    print(f"Parsed {len(g)} triples from {args.path}")

    # Count classes
    class_counts = defaultdict(int)
    for s, p, o in g.triples((None, RDF.type, None)):
        class_counts[str(o)] += 1

    print("\nTop classes:")
    for cls, cnt in sorted(class_counts.items(), key=lambda x: -x[1])[:15]:
        print(f"  {cnt:4d}  {cls}")

    # Find primary subjects (high degree or explicit mainEntity)
    subjects = set(g.subjects())
    print(f"\nTotal unique subjects: {len(subjects)}")

    # Look for schema:mainEntity or high out-degree subjects
    main_entities = []
    for s in list(subjects)[:50]:
        out_degree = len(list(g.triples((s, None, None))))
        label = g.value(s, RDFS.label) or g.value(s, SCHEMA.name) or str(s).split("#")[-1][:60]
        if out_degree > 3:
            main_entities.append((out_degree, str(s), label))

    if main_entities:
        print("\nHigh-degree / potential primary entities:")
        for deg, iri, label in sorted(main_entities, reverse=True)[:8]:
            print(f"  {deg:3d}  {label}  ({iri[:80]})")

    # Healthcare signal
    medical_keywords = ["MedicalCondition", "Drug", "ClinicalTrial", "PatientEvent", "MedicalEvent", "Comorbidity"]
    has_medical = any(kw in str(c) for c in class_counts for kw in medical_keywords)
    print(f"\nHealthcare / clinical signal detected: {has_medical}")

    print("\nSuggested visualization focus:")
    if has_medical:
        print("  - Enable healthcare color coding and timeline rendering")
        print("  - Prioritize MedicalCondition + Drug + PatientEvent filters")
        print("  - Offer Core view centered on primary condition + comorbidities")
    else:
        print("  - Standard KG Explorer with class filters")
        print("  - Focus on high-degree entities and HowTo/FAQ sections if present")

if __name__ == "__main__":
    main()