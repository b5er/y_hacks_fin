# Self Organizing Map
# potential fraud from the form

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

for i in range(1, 21):
	# Importing the dataset
	dataset = pd.read_csv('feeds/feed' + str(i) + '.csv')
	copy = pd.read_csv('feeds/feed' + str(i) + '.csv')

	dataset.fillna(0, inplace=True)

	def handle_non_num_data(df):
		columns = df.columns.values

		for column in columns:
			text_digit_vals = {}
			def convert_to_int(val):
				return text_digit_vals[val]

			if df[column].dtype != np.int64 and df[column].dtype != np.float64:
				column_contents = df[column].values.tolist()
				unique_elements = set(column_contents)
				x = 0
				for unique in unique_elements:
					if unique not in text_digit_vals:
						text_digit_vals[unique] = x
						x+=1

				df[column] = list(map(convert_to_int, df[column]))

		return df



	df = handle_non_num_data(dataset)

	X = df.iloc[:, :-1].values
	y = df.iloc[:, -1].values

	# feature scaling
	from sklearn.preprocessing import MinMaxScaler

	# normalizing to default feature_range=(0, 1)
	sc = MinMaxScaler(feature_range=(0, 1))

	# fit to x
	X = sc.fit_transform(X)

	# training the som
	# using the minisom.py file. Has to be in the wd (working directory)
	from som import Som

	# making small maps is not the best. Using bigger maps give more detail if needed.
	# here we don't have many customer in the dataset, thus 10 x 10 is enough
	som = Som(x=15, y=15, input_len=32, sigma = 1.0, learning_rate = .5)
	som.random_weights_init(data=X)
	som.train_random(data=X, num_iteration=200)

	# visualize result
	from pylab import bone, pcolor, pcolormesh, colorbar, plot, show


	# som.quantization(X)
	#initial window
	bone()
	#creates the map from black to white
	pcolormesh(som.distance_map().T, cmap='RdBu_r')
	colorbar()

	coordinates = []
	coor_x = 0
	for dist in som.distance_map():
		coor_y = 0
		for al in dist:
			if al > .9:
				coordinates.append((coor_x,coor_y))
			coor_y = coor_y + 1
		coor_x = coor_x + 1



	# red square didn't get approval. Green circles approved
	markers = ['o', 's']
	color = ['r', 'g']
	# i = all the indexes, x = different vectors of customers (rows)
	for i, x in enumerate(X):
	    w = som.winner(x)
	    plot(w[0] + .5,
	         w[1] + .5,
	         markers[y[i]],
	         markeredgecolor=color[y[i]],
	         markerfacecolor='None',
	         markersize=10,
	         markeredgewidth=2)

	    
	#finding outliers
	mappings = som.win_map(X)
	# axis = concatinate vertically or horizontally; 0 = vertical
	# possible_illegal = np.concatenate((mappings[(0,0)], mappings[(0,1)]), axis=0)

	mapp = []
	for advisor in coordinates:
		mapp.append(mappings[advisor])	

	print(coordinates)

	possible_illegal = np.concatenate((mapp), axis=0)

	# finding outliers
	possible_illegal = sc.inverse_transform(possible_illegal)

	ids = []

	for outliers in possible_illegal:
		ids.append(int(outliers[0]))

	file = open("illegal/possible_illegal" + str(i), "w")
	for person in ids:
		file.write(str(copy.iloc[person,:].values))
		file.write("\n")
	file.close()
	show()














