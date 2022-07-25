import seaborn as sns
import matplotlib.pyplot as plt


def ranklist(df, column_name)->[str,str]:
    """
        This function provides the barplot for the each series in a column and plot it in bar plot

        Input:
        column_name

        Output:
        plt bar plot of the column variable in descending order
        return the strings of the top five and the bottom five products in the rank list of the column category
    """

    df = df.sort_values([column_name], ascending=False).reset_index(drop=True)
    sns.set(font_scale=1)
    plt.figure(figsize=(20, 20))
    sns.barplot(x=df[column_name], y=df["name"])
    plt.ylabel("Product Name", fontsize=21)
    plt.xlabel(column_name, fontsize=21)
    plt.title(column_name, fontsize=30)
    plt.show()
    string1 = ", ".join(str(i) for i in list(df['name'].head()))
    string1 = ['Top: '].append(string1)
    return string1
    string2 = ", ".join(str(i) for i in list(df['name'].tail()))
    return string2


print(ranklist.__doc__)