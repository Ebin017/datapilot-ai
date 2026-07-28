from context.project_context import ProjectContext


class ProjectContextManager:
    """
    Stores the current ProjectContext during a CrewAI execution.
    """

    _context: ProjectContext | None = None

    @classmethod
    def set_context(cls, context: ProjectContext):
        cls._context = context

    @classmethod
    def get_context(cls) -> ProjectContext:
        if cls._context is None:
            raise ValueError(
                "ProjectContext has not been initialized."
            )
        return cls._context

    @classmethod
    def clear(cls):
        cls._context = None