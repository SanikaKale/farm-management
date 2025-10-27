"""
Test Execution Script
Runs all tests and generates reports
"""
import pytest
import os
import sys

def main():
    """Run all tests and generate reports"""
    
    # Test directory
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    
    # Coverage report HTML directory
    coverage_html = os.path.join(os.path.dirname(__file__), 'coverage_html')
    
    # Ensure coverage directory exists
    os.makedirs(coverage_html, exist_ok=True)
    
    # Run tests with coverage
    exit_code = pytest.main([
        test_dir,
        '-v',                    # Verbose output
        '--tb=short',            # Short traceback format
        '--cov=main',            # Coverage for main.py
        '--cov-report=html:' + coverage_html,  # HTML coverage report
        '--cov-report=term',     # Terminal coverage report
        '--cov-report=xml',      # XML coverage report (for CI)
        '--cov-branch',          # Branch coverage
        '--junit-xml=test-results.xml',  # JUnit XML for CI
        '-p', 'no:warnings',     # Suppress warnings
        '--color=yes'            # Colored output
    ])
    
    print("\n" + "="*70)
    print("TEST EXECUTION COMPLETED")
    print("="*70)
    print(f"\nCoverage HTML report: {coverage_html}/index.html")
    print(f"Test results XML: test-results.xml")
    print("\n" + "="*70)
    
    return exit_code

if __name__ == '__main__':
    sys.exit(main())
