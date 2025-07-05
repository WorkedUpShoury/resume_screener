from graphviz import Digraph

dot = Digraph('AI_Architecture', format='png')

# Global graph style
dot.attr(rankdir='LR', size='10,5')
dot.attr('node', shape='box', style='filled', color='lightgray', fontname='Helvetica')

# Nodes
dot.node('A', 'Data Sources\n(APIs, DBs, Files, IoT)', fillcolor='lightblue')
dot.node('B', 'Data Ingestion\n(ETL, Stream Processing)', fillcolor='lightyellow')
dot.node('C', 'Data Storage\n(Data Lake, S3, BigQuery)', fillcolor='lightgreen')
dot.node('D', 'Data Preprocessing\n(Cleaning, Labeling, Feature Engg.)', fillcolor='lightpink')
dot.node('E', 'Model Training\n(ML/DL Models - PyTorch, TF)', fillcolor='orange')
dot.node('F', 'Model Evaluation\n(Metrics, Tuning, Validation)', fillcolor='gold')
dot.node('G', 'Model Deployment\n(REST API, Docker, CI/CD)', fillcolor='lightcyan')
dot.node('H', 'Inference & Serving\n(Real-time Predictions)', fillcolor='lightgrey')
dot.node('I', 'Monitoring & Feedback\n(Drift Detection, Logs, Retraining)', fillcolor='wheat')

# Edges
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'I')

# Render
dot.render('presentation_ai_architecture', cleanup=True)
