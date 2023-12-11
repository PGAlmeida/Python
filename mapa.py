import pandas as pd
mundo = pd.read_csv("dados/mundo.csv")
mundo.head()

import plotly.express as px

fig = px.treemap(
    mundo,
    path=["continent", "name"],
    values="pop_est",
    color="pop_est",
    color_continuous_scale="cividis",
)

fig.update_layout(
    autosize=False,
    width=800,
    height=600,
)

fig.show()