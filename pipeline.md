# Pipeline of the rest work:

## 0.Preprocessing
  Check if T1~T8 satisfies lognormal, if yes, apply lambda x:ln(1+x) to them

## 1.Dimension Reduction
  We use t-SNE, to dimension 2 or 3 for visualization, to higher dimensions
  for persistent homology computation

## 2.Clustering
  Using hdbscan, or k-means. Using the label and TX data to plot the interactive
  graph in plotly

## 3.Summarizing by clusters
  Using statistical tool. And/Or tools from TDA
  Plot radar charts for each group

## 4.PH in higher dimension?
