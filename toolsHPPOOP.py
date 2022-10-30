def misc1():
    hddf1=df1.head()
    shpdf1 = df1.shape
    print(hddf1)
    df1.columns
    df1['area_type'].unique()
    df1['area_type'].value_counts()

def misc2():
    df2.shape
    df2.isnull().sum()
    df2.shape

def misc3():
    df3.isnull().sum()
    df3.shape

def misc4():
    df3.bhk.unique()

def misc5():
    df3[~df3['total_sqft'].apply(is_float)].head(10)

def misc6():
    df4.head(2)
    df4.loc[30]

def misc7():
    df5.head()
    df5_stats = df5['price_per_sqft'].describe()
    df5_stats
    df5.to_csv("bhp.csv",index=False)

def misc8():
    location_stats
    location_stats.values.sum()
    len(location_stats[location_stats>10])
    len(location_stats)
    len(location_stats[location_stats<=10])

def misc9():
    location_stats_less_than_10
    len(df5.location.unique())

def misc10():
    len(df5.location.unique())
    df5.head(10)
    df5[df5.total_sqft/df5.bhk<300].head()
    df5.shape

def misc10():
    df6.shape
    df6.price_per_sqft.describe()

def misc11():
    df7.shape

def misc11():
    df8.shape
    plot_scatter_chart(df8,"Rajaji Nagar")
    plot_scatter_chart(df8,"Hebbal")

def misc12():
    import matplotlib
    matplotlib.rcParams["figure.figsize"] = (20,10)
    plt.hist(df8.price_per_sqft,rwidth=0.8)
    plt.xlabel("Price Per Square Feet")
    plt.ylabel("Count")

def misc13():
    df8.bath.unique()
    plt.hist(df8.bath,rwidth=0.8)
    plt.xlabel("Number of bathrooms")
    plt.ylabel("Count")

def misc14():
    df8[df8.bath>10]
    df8[df8.bath>df8.bhk+2]

def misc15():
    df9.shape
    df9.head(2)

def misc16():
    df10.head(3)

def misc17():
    dummies.head(3)

def misc18():
    df11.head()

def misc19():
    df12.head(2)
    df12.shape
