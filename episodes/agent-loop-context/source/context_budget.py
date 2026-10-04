"""Small, deterministic context-selection example for the episode."""

from __future__ import annotations


def select_context(question: str, budget: int, *, include_tests: bool = True) -> dict[str, object]:
    """Return the bounded context selected for a synthetic status question."""
    candidates = ["status_view.py", "status_service.py"]
    if include_tests:
        candidates.append("test_status_service.py")
    selected = candidates[:budget]
    return {
        "question": question,
        "budget": budget,
        "selected": selected,
        "omitted": [name for name in candidates if name not in selected],
    }


if __name__ == "__main__":
    print(select_context("Why is the dashboard status stale?", 2))
