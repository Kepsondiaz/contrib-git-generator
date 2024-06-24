def generate_contributing_guide(output_file="CONTRIBUTING.md"):
    content = """
    # Contribution Guide

    Thank you for considering contributing to our project!

    ## Bug Reports

    Please use the GitHub issue tracker to report bugs.

    ## Pull Requests

    1. Fork the repository.
    2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`).
    3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
    4. Push to the branch (`git push origin feature/AmazingFeature`).
    5. Open a pull request.

    ## Coding Standards

    Ensure your code adheres to our coding standards.

    ## Tests

    Run all tests to ensure they pass before submitting a pull request.
    """
    with open(output_file, "w") as f:
        f.write(content)
    print(f"Contribution guide generated: {output_file}")
