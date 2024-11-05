class Project:
    def __init__(self, name, description, license1, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license1
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_stuff(self, stuff):
        return "\n".join(f'- {thing}' for thing in stuff) if stuff else "-"


    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n\nAuthors:\n{self._stringify_stuff(self.authors)}"
            f"\n\nDependencies:\n{self._stringify_stuff(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n{self._stringify_stuff(self.dev_dependencies)}"
        )
