#Importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Reading in data
df = pd.read_csv('A_vs_B.deseq2.results.tsv', sep='\t')
#Removing rows which have missing or NA values
df = df.dropna()
#Getting summary statistics for df including for p values and log fold changes
print("Summary statistics for A vs B File:")
print(df.describe())

#Adding new up/down column to df
df['Up_Down'] = 'NA'
#up if positive log2foldchange, down if negative
df.loc[df['log2FoldChange'] < 0, 'Up_Down'] = 'down'
df.loc[df['log2FoldChange'] >= 0, 'Up_Down'] = 'up'
#creating new df with only sig genes
df_p_sig = df[df['pvalue'] < 0.05]
#Total number of significant genes
print("Total number of genes where gene expression is significantly altered:")
print(len(df_p_sig))
#Number of sig upregulated genes
print("Total number of significantly upregulated genes:")
print((df_p_sig['Up_Down'] == 'up').sum())
#Number of sig downregulated genes
print("Total number of significantly downregulated genes:")
print((df_p_sig['Up_Down'] == 'down').sum())

#creating scatter graph with log2foldchange and pvalue as axes, hue as pvalue, 
plt.figure() #clearing any previous graph
sns.scatterplot(data=df, x='log2FoldChange', y='pvalue', hue='pvalue', palette='icefire')
#adding lines at -1 and 1 log2foldchange
plt.axvline(x=1, color='grey', linestyle='--')
plt.axvline(x=-1, color='grey', linestyle='--')
#adding title and legend
plt.title('Volcano Plot')
plt.legend(title='p-value', loc='upper right')
plt.show()
#saving plot
plt.savefig('volcanoplot_AvsB.jpeg', format='jpeg', dpi=300)

#Histogram of all p values
#creating histogram with pvalue, choosing number of bins and colour
plt.figure() #clearing previous graph
plt.hist(df['pvalue'], bins=40, color='blue')
#labelling axes
plt.xlabel('p-value')
plt.ylabel('Frequency')
#adding title
plt.title('Histogram of p-values')
#showing graph
plt.show()
#saving plot
plt.savefig('histogram_AvsB.jpeg', format='jpeg', dpi=300)


#creating new df of only significant genes, with only gene id, p value and log2foldchange columns
df_subset = df_p_sig[['gene_id', 'pvalue', 'log2FoldChange']]
#creating ordered df of top10 significant genes
df_ordered = df_subset.sort_values('pvalue').head(10)
#losing p value column
df_subset = df_ordered[['gene_id', 'log2FoldChange']]
#setting gene_id to be an index
df_subset.set_index('gene_id', inplace=True)
#creating heatmap
plt.figure() #clearing previous graph
sns.heatmap(df_subset, annot=True)
#saving plot
plt.savefig('heatmap_AvsB.jpeg', format='jpeg', dpi=300)

#creating ma plot
plt.figure() #clearing previous graph
#Selecting columns for input as x and y, making points transparent to see overlapping, choosing colour
plt.scatter(df['baseMean'], df['log2FoldChange'], alpha = 0.5, color='green')
#creating mid line
plt.axhline(0, color='black', linestyle='--')
#Labelling axes
plt.xlabel('Base Mean Expression)')
plt.ylabel('Log 2-Fold Change')
#Giving title
plt.title('MA Plot of Base Mean Expression vs Log 2-Fold Change')
#showing graph
plt.show()
#saving plot
plt.savefig('maplot_AvsB.jpeg', format='jpeg', dpi=300)

#creating new df of only significant genes, with only gene id, p value and log2foldchange columns
df_subset1 = df_p_sig[['gene_id', 'log2FoldChange', 'pvalue', 'padj']]
#sorting by p value
df_subset1 = df_subset1.sort_values('pvalue')
print("Table of significantly altered genes for AvsB")
print(df_subset1)

print("#################################################################################################################")
print("Starting analysis of A vs D file")
print("#################################################################################################################")

#Reading in data
df1 = pd.read_csv('A_vs_D.deseq2.results.tsv', sep='\t')
#Removing rows which have missing or NA values
df1 = df1.dropna()
#Getting summary statistics for df including for p values and log fold changes
print("Summary statistics for A vs D File:")
print(df1.describe())

#Adding new up/down column to df
df1['Up_Down'] = 'NA'
#up if positive log2foldchange, down if negative
df1.loc[df1['log2FoldChange'] < 0, 'Up_Down'] = 'down'
df1.loc[df1['log2FoldChange'] >= 0, 'Up_Down'] = 'up'
#creating new df with only sig genes
df_p_sig1 = df1[df1['pvalue'] < 0.05]
#Total number of significant genes
print("Total number of genes where gene expression is significantly altered:")
print(len(df_p_sig1))
len(df_p_sig1)
#Number of sig upregulated genes
print("Total number of significantly upregulated genes:")
print((df_p_sig1['Up_Down'] == 'up').sum())
#Number of sig downregulated genes
print("Total number of significantly downregulated genes:")
print((df_p_sig1['Up_Down'] == 'down').sum())

#creating scatter graph with log2foldchange and pvalue as axes, hue as pvalue, 
plt.figure() #clearing previous graph
sns.scatterplot(data=df1, x='log2FoldChange', y='pvalue', hue='pvalue', palette='icefire')
#adding lines at -1 and 1 log2foldchange
plt.axvline(x=1, color='grey', linestyle='--')
plt.axvline(x=-1, color='grey', linestyle='--')
plt.title('Volcano Plot')
plt.legend(title='p-value', loc='upper right')
plt.show()
#saving plot
plt.savefig('volcanoplot_AvsD.jpeg', format='jpeg', dpi=300)

#Histogram of all p values
plt.figure() #clearing previous graph
#creating histogram with pvalue, choosing number of bins and colour
plt.hist(df1['pvalue'], bins=40, color='blue')
#labelling axes
plt.xlabel('p-value')
plt.ylabel('Frequency')
#adding title
plt.title('Histogram of p-values')
#showing graph
plt.show()
#saving plot
plt.savefig('histogram_AvsD.jpeg', format='jpeg', dpi=300)


#creating new df of only significant genes, with only gene id, p value and log2foldchange columns
df_subset1 = df_p_sig1[['gene_id', 'pvalue', 'log2FoldChange']]
#creating ordered df of top10 significant genes
df_ordered1 = df_subset1.sort_values('pvalue').head(10)
#losing p value column
df_subset1 = df_ordered1[['gene_id', 'log2FoldChange']]
#setting gene_id to be an index
df_subset1.set_index('gene_id', inplace=True)
#clearing previous graph
plt.figure()
#creating heatmap
sns.heatmap(df_subset1, annot=True)
#saving plot
plt.savefig('heatmap_AvsD.jpeg', format='jpeg', dpi=300)

#ma plot
#clearing previous graph
plt.figure()
#Selecting columns for input as x and y, making points transparent to see overlapping, choosing colour
plt.scatter(df1['baseMean'], df1['log2FoldChange'], alpha = 0.5, color='green')
#creating mid line
plt.axhline(0, color='black', linestyle='--')
#Labelling axes
plt.xlabel('Base Mean Expression)')
plt.ylabel('Log 2-Fold Change')
#Giving title
plt.title('MA Plot of Base Mean Expression vs Log 2-Fold Change')
#showing graph
plt.show()
#saving plot
plt.savefig('maplot_AvsD.jpeg', format='jpeg', dpi=300)

#creating new df of only significant genes, with only gene id, p value and log2foldchange columns
df_subset2 = df_p_sig1[['gene_id', 'log2FoldChange', 'pvalue', 'padj']]
#sorting by p value
df_subset2 = df_subset2.sort_values('pvalue')
#printing table
print("Table of significantly altered genes for AvsD")
print(df_subset2)
