from langgraph.graph import StateGraph, END
from typing import TypedDict


class InsightState(TypedDict):
    get_deep_insight: bool
    insightSessionSummary: str
    insightCounter: int
    reflectionSummary: str
    theme: str
    messages: list

# 1. 洞察を引き出すための質問
def propose_insight_question():
    pass

# 2. 質問に対する回答を受け取る
def receive_insight_response():
    pass

# 3. 深い洞察を得られたか判定
def judge_insight_depth():
    pass


def should_continue_insight(state: InsightState) -> InsightState:
    if state.get("get_deep_insight", False):
        return "loop"
    return "end"

# グラフ作成
def build_insight_graph():
    sg = StateGraph(InsightState)

    sg.add_node("propose_insight", propose_insight_question)
    sg.add_node("receive_response", receive_insight_response)
    sg.add_node("judge_insight", judge_insight_depth)

    sg.set_entry_point("propose_insight")
    sg.add_edge("propose_insight", "receive_response")
    sg.add_edge("receive_response", "judge_insight")
    sg.add_conditional_edges(
        "judge_insight",
        should_continue_insight,
        {
            "loop": "propose_insight",
            "end": END
        }
    )

    return sg.compile()
