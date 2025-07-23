from langgraph.graph import StateGraph, END
from typing import TypedDict


class ActionState(TypedDict):
    commit_action: bool
    actionSessionSummary: str
    actionCounter: int
    theme: str
    reflectionSummary: str
    insightSummary: str
    messages: str

# 1. 行動を引き出すための質問をする
def propose_ask_action(state: ActionState) -> ActionState:
    pass

# 2. 質問に対する回答を受け取る
def receive_action_response(state: ActionState) -> ActionState:
    pass

# 3. 具体的な行動がコミットできたかチェック (内容、いつ、など)
def judge_commit_action(state: ActionState) -> ActionState:
    pass

def should_continue_action(state: ActionState) -> ActionState:
    if state.get("commit_action", False):
        return "loop"
    return "end"

# グラフ作成
def build_action_graph():
    sg = StateGraph(ActionState)

    sg.add_node("ask_action", propose_ask_action)
    sg.add_node("receive_response", receive_action_response)
    sg.add_node("judge_action", judge_commit_action)

    sg.set_entry_point("ask_action")
    sg.add_edge("ask_action", "receive_response")
    sg.add_edge("receive_response", "judge_action")
    sg.add_conditional_edges(
        "judge_action",
        should_continue_action,
        {
            "loop": "ask_action",
            "end": END
        }
    )

    return sg.compile()
