from langgraph.graph import StateGraph
from typing import TypedDict, Optional
from states.state_theme import build_theme_graph
from states.state_reflection import build_reflection_graph
from states.state_insight import build_insight_graph
from states.state_action import build_action_graph

class SessionState(TypedDict):
    theme: Optional[str]
    themeSessionSummary: str
    reflection: Optional[str]
    insight: Optional[str]
    action: Optional[str]


def build_main_graph():
    # Main graph
    graph = StateGraph(state_schema=SessionState)

    # Subgraph
    theme_graph = build_theme_graph()
    reflection_graph = build_reflection_graph()
    insight_graph = build_insight_graph()
    action_graph = build_action_graph()

    # Add nodes
    graph.add_node("decide_theme", theme_graph)
    graph.add_node("do_reflection", reflection_graph)
    graph.add_node("do_insight", insight_graph)
    graph.add_node("do_action", action_graph)

    # Connect processes
    graph.set_entry_point("decide_theme")
    graph.add_edge("decide_theme", "do_reflection")
    graph.add_edge("do_reflection", "do_insight")
    graph.add_edge("do_insight", "do_action")
    graph.set_finish_point("do_action")

    return graph.compile()
