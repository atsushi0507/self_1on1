from IPython.display import Image
from states.graph import build_1on1_graph
import os

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

graph = build_1on1_graph()

img = Image(graph.get_graph().draw_mermaid_png())

with open(f"{output_dir}/graph_image.png", "wb") as f:
    f.write(img.data)
