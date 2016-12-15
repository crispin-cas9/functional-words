import functional_words
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tempest = functional_words.tempest
much_ado = functional_words.much_ado

def drawmap(play):

	data = [play[key] for key in play]
	index = [key for key in play]
	df = pd.DataFrame(data=data)

	sns.set(context="paper", font="monospace", font_scale=.5)

	# Set up the matplotlib figure
	f, ax = plt.subplots(figsize=(12, 9))

	# Draw the heatmap using seaborn
	heatmap = sns.heatmap(df, vmax=df.max().max(), square=True, yticklabels=index, cmap="RdBu_r")

	# f.tight_layout()
	plt.xticks(rotation=-90)
	plt.yticks(rotation=0)

	fig = heatmap.get_figure()
	fig.savefig("plot.png", dpi=300)

	sns.plt.show()

drawmap(much_ado)
