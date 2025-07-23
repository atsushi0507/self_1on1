from IPython.display import Image
from states.graph import build_main_graph
from states.state_theme import build_theme_graph
from states.state_reflection import build_reflection_graph
from states.state_insight import build_insight_graph
from states.state_action import build_action_graph
import os

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

graph = build_main_graph()
img = Image(graph.get_graph().draw_mermaid_png())

with open(f"{output_dir}/main_graph_image.png", "wb") as f:
    f.write(img.data)

graph = build_theme_graph()
img = Image(graph.get_graph().draw_mermaid_png())

with open(f"{output_dir}/theme_graph_image.png", "wb") as f:
    f.write(img.data)

graph = build_reflection_graph()
img = Image(graph.get_graph().draw_mermaid_png())

with open(f"{output_dir}/reflection_graph_image.png", "wb") as f:
    f.write(img.data)

graph = build_insight_graph()
img = Image(graph.get_graph().draw_mermaid_png())

with open(f"{output_dir}/insight_graph_image.png", "wb") as f:
    f.write(img.data)

graph = build_action_graph()
img = Image(graph.get_graph().draw_mermaid_png())

with open(f"{output_dir}/action_graph_image.png", "wb") as f:
    f.write(img.data)
