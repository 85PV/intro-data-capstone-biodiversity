
# coding: utf-8

# # Capstone 2: Biodiversity Project

# # Introduction
# You are a biodiversity analyst working for the National Parks Service.  You're going to help them analyze some data about species at various national parks.
# 
# Note: The data that you'll be working with for this project is *inspired* by real data, but is mostly fictional.

# # Step 1
# Import the modules that you'll be using in this assignment:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd


# # Step 2
# You have been given two CSV files. `species_info.csv` with data about different species in our National Parks, including:
# - The scientific name of each species
# - The common names of each species
# - The species conservation status
# 
# Load the dataset and inspect it:
# - Load `species_info.csv` into a DataFrame called `species`

# In[2]:


species = pd.read_csv('AnacondaProjects/biodiversity/species_info.csv')
species.head()


# Inspect each DataFrame using `.head()`.

# # Step 3
# Let's start by learning a bit more about our data.  Answer each of the following questions.

# How many different species are in the `species` DataFrame?

# In[5]:


species.scientific_name.nunique()


# In[80]:


species.scientific_name.count()


# # duplicates? there are more scientific name counts than unique names
# unique scientific names = 5541
# total  scinetific names = 5824
# 

# In[81]:


species.describe()


# In[84]:


species[species.duplicated(['scientific_name'], keep=False)].describe()


# In[85]:


species[species.scientific_name == 'Procyon lotor']


# In[ ]:


# are some of the duplicates also protected?


# In[87]:


species_dupli = species[species.duplicated(['scientific_name'], keep=False)]


# In[88]:


species_dupli.groupby('conservation_status').scientific_name.count()


# In[ ]:


# are any duplicate scientific names in more than one conservation_status
# if so, why ... can a species have a different conservation status depending on the Park? ... no


# In[90]:


species_dupli[species_dupli.conservation_status == 'Endangered']


# In[200]:


species_dupli[species_dupli.scientific_name == 'Canis lupus']


# In[ ]:


# Canis lupus has duplicates and is in more than one conservation status
# searched the web and confirmed Canis lupus status is 'Endangered'
# the 'first' or 'last' duplicate may be retained
# lots of duplicates in conservation status 'Species of Concern'


# In[93]:


species_dupli[species_dupli.conservation_status == 'Species of Concern'].sort_values('scientific_name')


# In[ ]:


# new specie DataFrame with duplicates removed with correct Canis lupus conservation satus
# called species2


# In[94]:


species2 = species.drop_duplicates(['scientific_name'], keep='last')


# In[ ]:


# check duplicates are removed on Canis lupus and Procyon lotor


# In[95]:


species2[species2.scientific_name == 'Canis lupus']


# In[96]:


species2[species2.scientific_name == 'Procyon lotor']


# What are the different values of `category` in `species`?

# In[7]:


species.category.nunique()


# What are the different values of `conservation_status`?

# In[8]:


species.conservation_status.unique()


# In[199]:


species2[species.conservation_status == 'Endangered']


# In[133]:


species2[species2.conservation_status == 'In Recovery']


# In[204]:


species2[species.conservation_status == 'Threatened']


# In[135]:


species2[species2.conservation_status == 'Species of Concern']


# # Step 4
# Let's start doing some analysis!
# 
# The column `conservation_status` has several possible values:
# - `Species of Concern`: declining or appear to be in need of conservation
# - `Threatened`: vulnerable to endangerment in the near future
# - `Endangered`: seriously at risk of extinction
# - `In Recovery`: formerly `Endangered`, but currnetly neither in danger of extinction throughout all or a significant portion of its range
# 
# We'd like to count up how many species meet each of these criteria.  Use `groupby` to count how many `scientific_name` meet each of these criteria.

# In[138]:


species2.groupby(['conservation_status', 'category']).scientific_name.count().reset_index()


# In[194]:


species_concern_an = 4 + 68 + 4 + 22 + 5
species_concern_pl = 5 + 43
species_concern_an


# In[195]:


species_concern2_pl


# In[196]:


no_interven_an = 72 + 413 + 114 + 146 +73
no_interven_an


# In[197]:


no_interven_pl = 328 + 4216
no_interven_pl


# In[13]:


species.groupby('conservation_status').scientific_name.count()


# As we saw before, there are far more than 200 species in the `species` table.  Clearly, only a small number of them are categorized as needing some sort of protection.  The rest have `conservation_status` equal to `None`.  Because `groupby` does not include `None`, we will need to fill in the null values.  We can do this using `.fillna`.  We pass in however we want to fill in our `None` values as an argument.
# 
# Paste the following code and run it to see replace `None` with `No Intervention`:
# ```python
# species.fillna('No Intervention', inplace=True)
# ```

# In[14]:


species.fillna('No Intervention', inplace=True)


# Great! Now run the same `groupby` as before to see how many species require `No Protection`.

# In[15]:


species.groupby('conservation_status').scientific_name.count()


# In[ ]:


# the 'No Intervention' is greater than the number of unique scientific names in species.DataFrame
# run with species2 and the count sum is now 5541 and equal to unique scientific names


# In[98]:


species2.groupby('conservation_status').scientific_name.count()


# Let's use `plt.bar` to create a bar chart.  First, let's sort the columns by how many species are in each categories.  We can do this using `.sort_values`.  We use the the keyword `by` to indicate which column we want to sort by.
# 
# Paste the following code and run it to create a new DataFrame called `protection_counts`, which is sorted by `scientific_name`:
# ```python
# protection_counts = species.groupby('conservation_status')\
#     .scientific_name.count().reset_index()\
#     .sort_values(by='scientific_name')
# ```

# In[16]:


protection_counts = species.groupby('conservation_status')    .scientific_name.count().reset_index()    .sort_values(by='scientific_name')


# In[ ]:


# new protection_counts with species2 named 'protection_counts2


# In[102]:


protection_counts2 = species2.groupby('conservation_status')    .scientific_name.count().reset_index()    .sort_values(by='scientific_name')


# In[130]:


from pandas.tools.plotting import table
ax = plt.subplot(111, frame_on=False) # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis

table(ax, protection_counts2)  # where df is your data frame

plt.savefig('mytable.png')


# In[131]:


protection_counts2


# In[192]:


protection = 5541 - 5362
protection


# In[193]:


percent_protec = 179 / 5541 * 100
percent_protec


# Now let's create a bar chart!
# 1. Start by creating a wide figure with `figsize=(10, 4)`
# 1. Start by creating an axes object called `ax` using `plt.subplot`.
# 2. Create a bar chart whose heights are equal to `scientific_name` column of `protection_counts`.
# 3. Create an x-tick for each of the bars.
# 4. Label each x-tick with the label from `conservation_status` in `protection_counts`
# 5. Label the y-axis `Number of Species`
# 6. Title the graph `Conservation Status by Species`
# 7. Plot the grap using `plt.show()`

# In[19]:


plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)), protection_counts.scientific_name)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Spceies')
plt.title('Conservation Status by Species')
plt.show()


# In[103]:


plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts2)), protection_counts2.scientific_name)
ax.set_xticks(range(len(protection_counts2)))
ax.set_xticklabels(protection_counts2.conservation_status.values)
plt.ylabel('Number of Spceies')
plt.title('Conservation Status by Species')
plt.show()


# # Step 4
# Are certain types of species more likely to be endangered?

# Let's create a new column in `species` called `is_protected`, which is `True` if `conservation_status` is not equal to `No Intervention`, and `False` otherwise.

# In[21]:


species['is_protected'] = species.conservation_status != 'No Intervention'
        


# Let's group by *both* `category` and `is_protected`.  Save your results to `category_counts`.

# In[24]:


category_count = species.groupby(['category', 'is_protected'])    .scientific_name.nunique().reset_index()


# Examine `category_count` using `head()`.

# In[25]:


category_count.head()


# In[ ]:


# redo with species2


# In[113]:


category_count2 = species2.groupby(['category', 'is_protected'])    .scientific_name.nunique().reset_index()


# In[114]:


category_count2.head()


# It's going to be easier to view this data if we pivot it.  Using `pivot`, rearange `category_counts` so that:
# - `columns` is `conservation_status`
# - `index` is `category`
# - `values` is `scientific_name`
# 
# Save your pivoted data to `category_pivot`. Remember to `reset_index()` at the end.

# In[30]:


category_pivot = category_count.pivot(columns='is_protected',
                                     index='category',
                                     values='scientific_name')\
                                     .reset_index()


# Examine `category_pivot`.

# In[31]:


category_pivot


# In[ ]:


# redo with species2


# In[112]:


category_pivot2 = category_count2.pivot(columns='is_protected',
                                      index='category',
                                      values='scientific_name')\
                                      .reset_index()
category_pivot2


# Use the `.columns` property to  rename the categories `True` and `False` to something more description:
# - Leave `category` as `category`
# - Rename `False` to `not_protected`
# - Rename `True` to `protected`

# In[32]:


category_pivot.columns = ['category', 'not_protected', 'protected']


# Let's create a new column of `category_pivot` called `percent_protected`, which is equal to `protected` (the number of species that are protected) divided by `protected` plus `not_protected` (the total number of species).

# In[48]:


category_pivot['percent_protected'] = round((category_pivot.protected / (category_pivot.protected + category_pivot.not_protected) *100), 1)


# Examine `category_pivot`.

# In[49]:


category_pivot


# In[ ]:


# redue with specie2
# expected more of a numerical change with species2, the tables are about the same


# In[115]:


category_pivot2.columns = ['category', 'not_protected', 'protected']
category_pivot2['percent_protected'] = round((category_pivot2.protected / (category_pivot2.protected + category_pivot2.not_protected) *100), 1)
category_pivot2


# In[141]:


plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(category_pivot2)), category_pivot2.percent_protected.values)
ax.set_xticks(range(len(category_pivot2)))
ax.set_xticklabels(category_pivot2.category.values)
plt.ylabel('percent_protected')
plt.title('Overall Percent Protected by Category')
plt.show()


# It looks like species in category `Mammal` are more likely to be endangered than species in `Bird`.  We're going to do a significance test to see if this statement is true.  Before you do the significance test, consider the following questions:
# - Is the data numerical or categorical?
# - How many pieces of data are you comparing?

# Based on those answers, you should choose to do a *chi squared test*.  In order to run a chi squared test, we'll need to create a contingency table.  Our contingency table should look like this:
# 
# ||protected|not protected|
# |-|-|-|
# |Mammal|?|?|
# |Bird|?|?|
# 
# Create a table called `contingency` and fill it in with the correct numbers

# In[52]:


contingency = [[30, 146], [75, 413]]


# In order to perform our chi square test, we'll need to import the correct function from scipy.  Past the following code and run it:
# ```py
# from scipy.stats import chi2_contingency
# ```

# In[54]:


from scipy.stats import chi2_contingency


# Now run `chi2_contingency` with `contingency`.

# In[55]:


chi2_contingency(contingency)


# In[56]:


chi2_stat, pval, dof, t = chi2_contingency(contingency)
pval


# It looks like this difference isn't significant!
# 
# Let's test another.  Is the difference between `Reptile` and `Mammal` significant?

# In[57]:


contingency2 = [[30, 146], [5, 73]]
chi2_contingency(contingency2)


# Yes! It looks like there is a significant difference between `Reptile` and `Mammal`!

# # Step 5

# Conservationists have been recording sightings of different species at several national parks for the past 7 days.  They've saved sent you their observations in a file called `observations.csv`.  Load `observations.csv` into a variable called `observations`, then use `head` to view the data.

# In[59]:


observations = pd.read_csv('AnacondaProjects/biodiversity/observations.csv')
observations.head()


# In[ ]:


# the scientific_name unique count in observations is the same as in series


# In[118]:


observations.describe(include='all')


# Some scientists are studying the number of sheep sightings at different national parks.  There are several different scientific names for different types of sheep.  We'd like to know which rows of `species` are referring to sheep.  Notice that the following code will tell us whether or not a word occurs in a string:

# In[1]:


# Does "Sheep" occur in this string?
str1 = 'This string contains Sheep'
'Sheep' in str1


# In[2]:


# Does "Sheep" occur in this string?
str2 = 'This string contains Cows'
'Sheep' in str2


# Use `apply` and a `lambda` function to create a new column in `species` called `is_sheep` which is `True` if the `common_names` contains `'Sheep'`, and `False` otherwise.

# In[67]:


species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
species.head()


# In[ ]:


# try with species2


# In[143]:


species['is_sheep'] = species2.common_names.apply(lambda x: 'Sheep' in x)


# Select the rows of `species` where `is_sheep` is `True` and examine the results.

# In[68]:


species2[species.is_sheep]


# Many of the results are actually plants.  Select the rows of `species` where `is_sheep` is `True` and `category` is `Mammal`.  Save the results to the variable `sheep_species`.

# In[70]:


sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
sheep_species


# In[120]:


sheep_species2 = species2[(species2.is_sheep) & (species2.category == 'Mammal')]
sheep_species2


# Now merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.  Save this DataFrame as `sheep_observations`.

# In[71]:


sheep_observations = observations.merge(sheep_species)
sheep_observations


# In[121]:


sheep_observations2 = observations.merge(sheep_species2)
sheep_observations2


# How many total sheep observations (across all three species) were made at each national park?  Use `groupby` to get the `sum` of `observations` for each `park_name`.  Save your answer to `obs_by_park`.
# 
# This is the total number of sheep observed in each park over the past 7 days.

# In[72]:


obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
obs_by_park


# In[122]:


obs_by_park2 = sheep_observations2.groupby('park_name').observations.sum().reset_index()
obs_by_park2


# In[147]:


obs_by_park3 = sheep_observations2.groupby(['park_name', 'scientific_name']).observations.sum().reset_index()
obs_by_park3


# In[150]:


obs_by_park4 = sheep_observations2.groupby('scientific_name').observations.sum().reset_index()
obs_by_park4


# In[152]:


obs_by_park5 = sheep_observations2.groupby('park_name').observations.describe().reset_index()
obs_by_park5


# In[190]:


plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park5)), obs_by_park5.mean.values)
ax.set_xticks(range(len(obs_by_park5)))
ax.set_xticklabels(obs_by_park5.park_name.values)
plt.ylabel('Number of observations')
plt.title('Observations of Sheep per Week')
plt.savefig('ob_sheep.png')
plt.show()
plt.close()


# In[154]:


obs_by_sheep = sheep_observations2.groupby('scientific_name').observations.describe().reset_index()
obs_by_sheep


# Create a bar chart showing the different number of observations per week at each park.
# 
# 1. Start by creating a wide figure with `figsize=(16, 4)`
# 1. Start by creating an axes object called `ax` using `plt.subplot`.
# 2. Create a bar chart whose heights are equal to `observations` column of `obs_by_park`.
# 3. Create an x-tick for each of the bars.
# 4. Label each x-tick with the label from `park_name` in `obs_by_park`
# 5. Label the y-axis `Number of Observations`
# 6. Title the graph `Observations of Sheep per Week`
# 7. Plot the grap using `plt.show()`

# In[188]:


obs_by_park.info()


# In[144]:


plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)), obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of observations')
plt.title('Observations of Sheep per Week')
plt.savefig('ob_sheep.png')
plt.show()
plt.close()


# Our scientists know that 15% of sheep at Bryce National Park have foot and mouth disease.  Park rangers at Yellowstone National Park have been running a program to reduce the rate of foot and mouth disease at that park.  The scientists want to test whether or not this program is working.  They want to be able to detect reductions of at least 5 percentage point.  For instance, if 10% of sheep in Yellowstone have foot and mouth disease, they'd like to be able to know this, with confidence.
# 
# Use the sample size calculator at <a href="https://www.optimizely.com/sample-size-calculator/">Optimizely</a> to calculate the number of sheep that they would need to observe from each park.  Use the default level of significance (90%).
# 
# Remember that "Minimum Detectable Effect" is a percent of the baseline.

# In[76]:


minimum_detectable_effect = 100 * 0.05 / 0.15
minimum_detectable_effect


# How many weeks would you need to observe sheep at Bryce National Park in order to observe enough sheep?  How many weeks would you need to observe at Yellowstone National Park to observe enough sheep?

# In[78]:


bryce_weeks = 520 / 250
yellowstone_weeks = 520 / 507
bryce_weeks


# In[79]:


yellowstone_weeks


# yellowstone at 10% disease 

# In[201]:


min_detec_effect_05 = 100 * 0.05 / 0.10
min_detec_effect_05


# In[203]:


yellowstone10_weeks = 890 / 507
yellowstone10_weeks 

