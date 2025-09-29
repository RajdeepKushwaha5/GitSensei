"""
Simple test runner for the GitSensei project.
Runs unit tests for all modules.
"""

import sys
import traceback
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def run_test_module(module_name, test_class):
    """Run tests for a specific module"""
    print(f"\n🧪 Running tests for {module_name}")
    print("=" * 50)

    try:
        # Import the test module directly from the tests directory
        import importlib.util
        import sys
        from pathlib import Path

        # Add the project root to the path
        project_root = Path(__file__).parent.parent
        sys.path.insert(0, str(project_root))
        sys.path.insert(0, str(project_root / "src"))

        # Import the test module
        test_file = project_root / "tests" / f"{module_name}.py"
        spec = importlib.util.spec_from_file_location(module_name, test_file)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)

        # Get the test class
        test_cls = getattr(test_module, test_class)

        # Create instance and run tests
        test_instance = test_cls()

        # Get all test methods
        test_methods = [
            method for method in dir(test_instance) if method.startswith("test_")
        ]

        passed = 0
        failed = 0

        for method_name in test_methods:
            try:
                print(f"  Running {method_name}...", end=" ")
                method = getattr(test_instance, method_name)
                method()
                print("✅ PASSED")
                passed += 1
            except Exception as e:
                print(f"❌ FAILED: {str(e)}")
                failed += 1

        print(f"\n📊 Results for {module_name}: {passed} passed, {failed} failed")
        return passed, failed

    except ImportError as e:
        print(f"❌ Could not import {module_name}: {e}")
        return 0, 1
    except Exception as e:
        print(f"❌ Error running {module_name}: {e}")
        traceback.print_exc()
        return 0, 1


def main():
    """Main test runner function"""
    print("🚀 GitSensei - Test Suite")
    print("=" * 60)

    test_modules = [
        ("test_logging_utils", "TestLoggingUtils"),
        ("test_agent_logic", "TestAgent"),
        ("test_evaluation", "TestEvaluationFunctions"),
    ]

    total_passed = 0
    total_failed = 0

    for module_name, test_class in test_modules:
        passed, failed = run_test_module(module_name, test_class)
        total_passed += passed
        total_failed += failed

    print("\n" + "=" * 60)
    print("📈 FINAL RESULTS")
    print(f"   Total Tests: {total_passed + total_failed}")
    print(f"   Passed: {total_passed}")
    print(f"   Failed: {total_failed}")
    print(
        f"   Success Rate: {(total_passed / (total_passed + total_failed) * 100):.1f}%"
    )

    if total_failed == 0:
        print("🎉 All tests passed!")
        return 0
    else:
        print(f"⚠️  {total_failed} tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
