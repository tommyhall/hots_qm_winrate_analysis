import os
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


table_header = ['name', 'gp','popularity','winrate']
filename_mapping_all = {
    'BoE': 'battlefield_of_eternity.txt',
    'Braxis Holdout': 'braxis_holdout.txt',
    'Cursed Hollow': 'cursed_hollow.txt',
    'Dragon Shire': 'dragon_shire.txt',
    'Towers of Doom': 'towers_of_doom.txt',
    'Warhead Junction': 'warhead_junction.txt',
}
filename_mapping_gold = {
    'BoE': 'battlefield_of_eternity_gold.txt',
    'Braxis Holdout': 'braxis_holdout_gold.txt',
    'Cursed Hollow': 'cursed_hollow_gold.txt',
    'Dragon Shire': 'dragon_shire_gold.txt',
    'Towers of Doom': 'towers_of_doom_gold.txt',
    'Warhead Junction': 'warhead_junction_gold.txt',
}

def load_map_data(filename_mapping):
    """ Given a filename mapping, loads data from CSV into a DataFrame """
    df = pd.DataFrame()
    for map_name, filename in filename_mapping.iteritems():
        # read in csv (actually a text file) into a DataFrame
        filepath = os.path.join(os.getcwd(), 'data', filename)
        temp_df = pd.read_csv(filepath, sep='\t', header=None, names=table_header)
        # strip the % and whitespace away from our winrates
        temp_df['winrate'] = temp_df['winrate'].str.rstrip(" %")
        # get our winrate column (column index 3) and convert to numeric
        s = temp_df.ix[:,3]
        s = s.apply(pd.to_numeric)
        df[map_name] = s  # add it to the DataFrame
    return df

def plot_data(df, figures=[1,2], titles=None):
    """ Given a DataFrame, plots some data. """

    # create a stripplot on top of a boxplot
    plt.figure(figures[0],figsize=(10,7))
    ax1 = plt.axes()
    sns.boxplot(data=df, ax=ax1)
    sns.stripplot(data=df, jitter=True, color='.2', ax=ax1)
    ax1.set(ylabel='Win rate')
    ax1.set(ylim=(35,65))
    if titles:
        ax1.set_title(titles[0])

    # create a density plot
    plt.figure(figures[1], figsize=(10,7))
    ax2 = plt.axes()
    for x in df.columns.values.tolist():
        sns.kdeplot(df[x], ax=ax2) #shade=True
    ax2.set(xlabel='Win rate')
    ax2.set(ylabel='Density')
    ax2.set(xlim=(20,80))
    ax2.set(ylim=(0,.12))
    if titles:
        ax2.set_title(titles[1])

if __name__ == '__main__':
    all_df = load_map_data(filename_mapping_all)
    gold_df = load_map_data(filename_mapping_gold)
    sns.set_style("whitegrid")
    sns.set_context("notebook")
    plot_data(all_df,
        figures=[1,2],
        titles=[
            "Hero win rates by map (All skill levels, Quickmatch)",
            "Hero win rate density (All skill levels, Quickmatch)",
        ])
    plot_data(gold_df,
        figures=[3,4],
        titles=[
            "Hero win rates by map (Gold skill level, Quickmatch)",
            "Hero win rate density (Gold skill level, Quickmatch)",
        ])
    plt.show()
