from langgraph.graph import StateGraph
from typing import TypedDict, Optional


class ThemeState(TypedDict):
    theme: Optional[str]
    sessionSummary: str
    counter: int

def propose_theme(state: ThemeState) -> ThemeState:
    user_input = state.get("user_input", "")
    counter = state["counter"] + 1

    if "悩み" in user_input or "困って" in user_input:
        theme = user_input
        is_confirmed = True
    else:
        theme = None
        is_confirmed = False

    return {
        **state,
        "theme": theme,
        "counter": counter,
        "is_confirmed": is_confirmed
    }

def is_theme_confirmed(state: ThemeState) -> bool:
    return state["theme"] is not None

def build_theme_graph():
    sg = StateGraph(ThemeState)

    sg.add_node("propose_theme", propose_theme)

    sg.set_entry_point("propose_theme")
    sg.add_conditional_edges(
        "propose_theme",
        is_theme_confirmed,
        {
            True: "__end__",
            False: "propose_theme",
        }
    )

    return sg.compile()
