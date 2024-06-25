from openai import OpenAI
import os

# Set your OpenAI API key heregst 

client = OpenAI(
    api_key=os.getenv(OPENIA_API_KEY) # type: ignore
)

def get_project_details():
    print("Let's gather some details about your project to customize the contribution guide.")
    project_name = input("Project name: ")
    bug_tracking = input("Where should bugs be reported (e.g., GitHub Issues URL): ")
    code_standards = input("Briefly describe your coding standards (e.g., follow PEP8): ")
    test_instructions = input("How should contributors run tests: ")
    additional_info = input("Any additional information to include: ")
    
    return {
        "project_name": project_name,
        "bug_tracking": bug_tracking,
        "code_standards": code_standards,
        "test_instructions": test_instructions,
        "additional_info": additional_info
    }

def generate_contributing_md(details):
    prompt = f"""
    Generate a CONTRIBUTING.md file for a project with the following details:

    Project Name: {details['project_name']}
    Bug Tracking: {details['bug_tracking']}
    Coding Standards: {details['code_standards']}
    Test Instructions: {details['test_instructions']}
    Additional Information: {details['additional_info']}

    The guide should include sections for Bug Reports, Pull Requests, Coding Standards, and Tests.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[prompt]
    )

    return response.choices[0].text.strip()

def save_contributing_md(content, filename="CONTRIBUTING.md"):
    with open(filename, "w") as file:
        file.write(content)
    print(f"Contribution guide saved as {filename}")

def main():
    details = get_project_details()
    contributing_md_content = generate_contributing_md(details)
    save_contributing_md(contributing_md_content)

if __name__ == "__main__":
    main()
