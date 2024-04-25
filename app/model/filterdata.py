import pandas as pd
import emoji
import tensorflow as tf

dataset_path = './media/datasets/'


#check data
df_train = pd.read_csv(ds_path+'twitter_training.csv', 
                       names=['ID','user','SC','Comment'])
df_test = pd.read_csv(ds_path+'twitter_validation.csv', 
                      names=['ID','user','SC','Comment'])


def dropRowValue(dataframe,column,values):
    return dataframe[~dataframe[column].isin(values)]


# categorizing in positive and negative, and dropping unnecessary columns
filter_df_train = dropRowValue(df_train,'SC',['Neutral','Irrelevant']).drop(['ID','user'], axis=1)
filter_df_test = dropRowValue(df_train,'SC',['Neutral','Irrelevant']).drop(['ID','user'], axis=1)


x_train = filter_df_train['Comment'].to_list()
y_train = filter_df_train['SC'].to_list()
x_test = filter_df_train['Comment'].to_list()
y_test = filter_df_train['SC'].to_list()


y_train_num = []
y_test_num = []
for row_train, row_test in zip(y_train,y_test):
    if row_train == 'Positive' or row_test == 'Positive':
        y_train_num.append(1)
        y_test_num.append(1)
    else:
        y_train_num.append(0)
        y_test_num.append(0)



# generating the emoji mask


def emojiMask(sentence):
    sentenceEmojiMask = emoji.replace_emoji(sentence,
                        replace=lambda chars,
                        data_dict: chars.encode('ascii', 'namereplace').decode())
    return sentenceEmojiMask


x_train_emojimask = [emojiMask(str(row)) for row in x_train]
x_test_emojimask = [emojiMask(str(row)) for row in x_test]



# tensor vector for model
def trainTensorSlice(xtrain,ytrain):
    x_tensor = tf.constant(xtrain)
    y_tensor = tf.constant(ytrain)
    dataset_tensor = tf.data.Dataset.from_tensor_slices((x_tensor,y_tensor)) # no batching, the batching will be later on
    return dataset_tensor

train_ds = trainTensorSlice(x_train_emojimask,y_train_num)
test_ds = trainTensorSlice(x_test_emojimask,y_test_num)



BUFFER_SIZE = 10000
BATCH_SIZE = 64

train_dataset = train_ds.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
test_dataset = test_ds.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)




