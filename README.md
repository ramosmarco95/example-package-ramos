# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

📦 GitHub Actions Workflow for Packaging and Deployment
This project includes a fully automated GitHub Actions workflow that tests, builds, and publishes the package to TestPyPI upon each push to the main branch.

🔧 Workflow Features
✅ Automated Testing: Runs unit tests using pytest to ensure code reliability before deployment.

🏗️ Package Building: Uses Python’s build module to create source and wheel distributions.

🚀 Publishing: Securely deploys the package to TestPyPI using a GitHub Actions workflow and a trusted publisher configuration.

🔐 Secure Credentials: Publishes using a GitHub secret (TEST_PYPI_API_TOKEN) to avoid exposing sensitive information.

🧪 Test Example
A unit test is included for the add_one() function:

python
Copy
Edit
from src.example_package_ramos import example

def test_add_one():
    assert example.add_one(1) == 2
⚙️ CI/CD Trigger
The workflow is triggered automatically on every push to the main branch, streamlining the release process and ensuring consistent deployment.
