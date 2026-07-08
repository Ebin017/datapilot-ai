# Milestone 0 - Project Foundation

## Learned

- A professional project starts with structure before code.
- `pyproject.toml` stores project metadata and configuration.
- Semantic Versioning follows `MAJOR.MINOR.PATCH`.
- Git tracks files, not empty folders.
- A Git commit should represent one meaningful milestone.
- Build for today's requirements, but design for tomorrow's.

## Questions

- How does pip use `pyproject.toml`?
- When should dependencies be added?

# Milestone 1 - Dataset Module

## Learned

- Domain models represent the core business objects of an application.
- Dictionaries are flexible but become difficult to maintain in large projects.
- Pydantic provides validation, serialization, and type safety.
- Dependencies should be added only when they are needed.

## Questions

- Should DatasetInfo be one model or multiple smaller models?

## Learned

- Keep one domain model per file.
- Smaller files are easier to maintain and navigate.
- Organize files around business concepts rather than convenience.

# Milestone 1 - Dataset Module

## Learned

- Use Pydantic `BaseModel` for domain models.
- Use `Field(default_factory=...)` for dynamic default values like timestamps.
- Use the correct data type (`datetime`) instead of strings.
- Add docstrings to domain models.
- Prefer concise but meaningful field names (`rows` instead of `num_rows`).

## Questions

- How does Pydantic validate data automatically?

## Learned

- `__init__.py` marks a folder as a Python package and can define its public API.
- `__all__` controls which objects are intended to be publicly exported.
- Prefer instance-based services over static utility classes for better extensibility.

## Learned

- A service contains business logic, not UI logic.
- DatasetService is responsible only for loading datasets and extracting metadata.
- Use `pathlib.Path` instead of raw file paths.
- Return both the DataFrame and DatasetInfo because they serve different purposes.
- Read the dataset only once and reuse it throughout the pipeline.

## Learned

- Example scripts are useful for validating business logic before building a UI.
- Use a `main()` function to organize executable scripts.
- `if __name__ == "__main__"` ensures code runs only when the file is executed directly.
- Domain models should store data, not handle presentation or formatting.

## Learned

- Running a file directly changes how Python resolves imports.
- Avoid modifying `sys.path` to fix imports.
- Professional Python projects are installed in editable mode using `pip install -e .`.
- Project packaging becomes important as applications grow.

## Learned

- Catch only expected exceptions.
- Never use `except Exception` unless absolutely necessary.
- Private helper methods (`_method_name`) hide implementation details.

## Learned

- User choices (like the target column) are not metadata.
