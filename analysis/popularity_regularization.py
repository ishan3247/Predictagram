# TODO: obtain linear regression of timestamp vs likescount and loop through df_main altering ACTUAL like count.

# get time into proper format
df_main['normalizedTime'] = df_main['timestamp'].map(lambda x: x.to_pydatetime().timestamp())

# stores entries in the form username: [m, b]
coefficient_dict = {}
for artist in list(df_main.username.drop_duplicates()):
    f_artist = df_main[df_main.username==artist]
    X = np.array(df_artist['normalizedTime']).reshape(-1,1)
    y = np.array(df_artist['likesCount']).reshape(-1,1)
    regression = LinearRegression()
    regression.fit(X,y)
    coefficient_dict[artist] = regression.coef_[0][0], regression.intercept_[0]
    
# print(df_main.iloc[0]['username'])    
for i in range(len(df_main)):
    
    likes = df_main.iloc[i]['likesCount']
    username = df_main.iloc[i]['username']
    timestamp = df_main.iloc[i]['normalizedTime']
    # likes = likes * (likes/(mX+b))
    df_main.at[i, 'likesCount'] = likes * (likes/(coefficient_dict[username][0]*timestamp + coefficient_dict[username][1]))

df_main.head()