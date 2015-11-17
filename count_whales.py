with open("training/train.csv") as training_data:
    training_data_contents = training_data.readlines()[1:]
training_data_contents = [entry.strip().split(',') for entry in training_data_contents]
whales_list_full = [entry[1] for entry in training_data_contents]
whales_set = set(whales_list_full) # number of different whales is len(whales_set)
whales_list = list(whales_set)
whales_list.sort()
with open("training/count.csv","w") as out:
    for whale in whales_list:
        out.write(whale + "," + str(whales_list_full.count(whale)) + '\n')
