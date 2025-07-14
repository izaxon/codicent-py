#!/usr/bin/env python3
"""
Build and publish script for codicent-py package.

Usage:
    python publish.py build    # Build the package
    python publish.py test     # Upload to TestPyPI
    python publish.py prod     # Upload to PyPI
"""

import subprocess
import sys
import os
import shutil

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"Error: {e.stderr}")
        return False

def clean_build():
    """Clean previous build artifacts."""
    print("🧹 Cleaning previous build artifacts...")
    dirs_to_clean = ['build', 'dist', 'codicent_py.egg-info']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"  Removed {dir_name}")

def build_package():
    """Build the package."""
    clean_build()
    
    # Install build dependencies
    if not run_command("pip install --upgrade build twine", "Installing build dependencies"):
        return False
    
    # Build the package
    if not run_command("python -m build", "Building package"):
        return False
    
    print("\n📦 Package built successfully!")
    print("  Check the 'dist/' directory for the built files.")
    return True

def upload_to_testpypi():
    """Upload package to TestPyPI."""
    if not os.path.exists('dist'):
        print("❌ No dist directory found. Run 'build' first.")
        return False
    
    print("\n🚀 Uploading to TestPyPI...")
    print("You'll need to enter your TestPyPI credentials.")
    return run_command("python -m twine upload --repository testpypi dist/*", "Uploading to TestPyPI")

def upload_to_pypi():
    """Upload package to PyPI."""
    if not os.path.exists('dist'):
        print("❌ No dist directory found. Run 'build' first.")
        return False
    
    print("\n🚀 Uploading to PyPI...")
    print("You'll need to enter your PyPI credentials.")
    return run_command("python -m twine upload dist/*", "Uploading to PyPI")

def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "build":
        if build_package():
            print("\n✅ Build completed successfully!")
            print("\nNext steps:")
            print("  1. Test upload: python publish.py test")
            print("  2. Test install: pip install -i https://test.pypi.org/simple/ codicent-py")
            print("  3. Production upload: python publish.py prod")
        else:
            print("\n❌ Build failed!")
            sys.exit(1)
    
    elif command == "test":
        if upload_to_testpypi():
            print("\n✅ Test upload completed!")
            print("\nTo test the package:")
            print("  pip install -i https://test.pypi.org/simple/ codicent-py")
        else:
            print("\n❌ Test upload failed!")
            sys.exit(1)
    
    elif command == "prod":
        print("⚠️  You are about to upload to the production PyPI!")
        confirm = input("Are you sure? (yes/no): ")
        if confirm.lower() == "yes":
            if upload_to_pypi():
                print("\n🎉 Package published to PyPI successfully!")
                print("  Users can now install with: pip install codicent-py")
            else:
                print("\n❌ Production upload failed!")
                sys.exit(1)
        else:
            print("❌ Upload cancelled.")
    
    else:
        print(f"❌ Unknown command: {command}")
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
