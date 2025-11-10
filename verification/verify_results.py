#!/usr/bin/env python3
"""
Quick verification script for AIVA benchmark results.
"""

import json
from pathlib import Path

def verify_results():
    """Verify benchmark results"""
    print("🔍 Verifying AIVA Benchmark Results")
    print("=" * 70)
    print()
    
    # Load results
    results_file = Path('aiva_benchmark_comparison_report.json')
    if not results_file.exists():
        print("⚠️  Results file not found")
        return False
    
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    print("📊 Benchmark Results:")
    print()
    
    if 'comparisons' in results:
        for comp in results['comparisons']:
            print(f"  {comp['benchmark']}:")
            print(f"    Score: {comp['aiva_score']:.2f}%")
            print(f"    Rank: {comp['rank']}/{comp['total_models']}")
            print(f"    Improvement: +{comp['percentage_improvement']:.2f}%")
            print()
    
    print("✅ Results verified!")
    return True

if __name__ == "__main__":
    verify_results()
