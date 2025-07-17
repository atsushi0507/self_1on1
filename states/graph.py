from langgraph.graph import StateGraph
from typing import TypedDict, Optional
from states import state_theme, state_reflection, state_insight, state_action, state_fleetalk

class OneOnOneState(TypedDict, total=False):
    theme: Optional[str]
    reflection: Optional[str]
    insight: Optional[str]
    action: Optional[str]

def build_1on1_graph():
    graph = StateGraph(state_schema=OneOnOneState)

    # 各ノードを追加
    graph.add_node("ask_for_theme", state_theme.run)
    graph.add_node("check_reflection", state_reflection.run)
    graph.add_node("check_insight", state_insight.run)
    graph.add_node("check_action", state_action.run)
    graph.add_node("check_fleetalk", state_fleetalk.run)

    # 遷移定義 (とりあえず直列。分岐なし)
    graph.set_entry_point("ask_for_theme")
    graph.add_edge("ask_for_theme", "check_reflection")
    graph.add_edge("check_reflection", "check_insight")
    graph.add_edge("check_insight", "check_action")
    graph.add_edge("check_action", "check_fleetalk")
    graph.set_finish_point("check_fleetalk")

    return graph.compile()
