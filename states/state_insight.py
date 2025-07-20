from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_core.messages import HumanMessage, AIMessage


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

# 4. 洞察を得るための質問を続ける
def continue_extract_insight_question():
    pass

# グラフ作成
def build_insight_graph():
    pass
