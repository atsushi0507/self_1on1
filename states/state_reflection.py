from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableLambda, Runnable


class ReflectionState(TypedDict):
    is_goog_reflection: bool
    reflectionSessionSummary: str
    reflectionCounter: int
    messages: list

# 1: 質問を投げる (内省を促す)
def propose_reflection_questoin(state: ReflectionState) -> ReflectionState:
    counter = state.get("reflectionCounter", 0)
    mock_questions = [
        "なぜそう思ったのですか？",
        "それ以外に考えられる理由はありますか？",
        "具体的にはどんな出来事がありましたか？",
        "他の人ならどう感じると思いますか？",
        "それを通じてどんな学びがありましたか？"
    ]
    question = mock_questions[counter % len(mock_questions)]

    state["messages"].append(AIMessage(content=question))
    state["reflectionCounter"] = counter + 1
    return state

# 2: 回答を受け取る (モック)
def receive_user_response(state: ReflectionState) -> ReflectionState:
    mock_response = "なるほど、それは大変でしたね。"
    state["messages"].append(HumanMessage(content=mock_response))
    return state

# 3: 内省の深さを判定
def judge_reflection_depth(state: ReflectionState) -> ReflectionState:
    # モック: 5 回以上繰り返したら十分とみなす
    state["is_good_reflection"] = state.get("reflectionCounter", 0) >= 5
    return state

# 4: 条件判定ノード
def should_continue_reflection(state: ReflectionState) -> ReflectionState:
    if state.get("is_good_reflection", False):
        return "end"
    if state.get("reflectionCounter", 0) >= 10:
        return "additional_reflection"
    return "loop"

def build_reflection_graph() -> Runnable:
    sg = StateGraph(ReflectionState)

    sg.add_node("propose_question", propose_reflection_questoin)
    sg.add_node("receive_response", receive_user_response)
    sg.add_node("judge_reflection", judge_reflection_depth)
    
    sg.set_entry_point("propose_question")
    sg.add_edge("propose_question", "receive_response")
    sg.add_edge("receive_response", "judge_reflection")
    sg.add_conditional_edges(
        "judge_reflection",
        should_continue_reflection,
        {
            "loop": "propose_question",
            "additional_reflection": END,
            "end": END
        }
    )

    return sg.compile()
