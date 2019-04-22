
## Pandas is a Python library that primarily adds two new data types in Python：
- Series: a sequence of items, where each item has a unique label, called an index; 
- Dataframe: is a table of data, each row has a unique label, called row index, 
    and each column has a unique label, called column index
- Each column in the dataframe can be considered as a Series.

These data types use NumPy library. NumPy primarily adds the ndarry datatype to Pandas.
ndarry is similar to a Python list, which stores ordered data, but it is different in three aspects:
- Each element has the same data type
- Elements are stored contiguously (immediately after each other)
- The total size of an ndarray is fixed


```python
! python --version
```

    Python 3.6.8 :: Anaconda, Inc.
    


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

### Handling NA

- Count how many NA,or Nans What percentage of the data row columns ?
- Decide if data is recoverable or not
- if yes, get new data to update or augment frame 
- if no, then you may have to average or fill in or use sampling
- You may need to impute the data. Refer to Mice package in R. Use R then save R's df then read into Pandas.
- If the NA's are approx 1 -5 % of Total data then you might be able to remove. If the data id OBVIOUSLY WRONG like negative prices for example when it is not expected remove the rows or change the data items appropriately.

Warning none == none but np.nan!=np.nan


```python
a=np.nan
b=np.nan
a==b
```




    False




```python
c=None
d=None
c==d
```




    True



##### First Step : ISNULL()  Count How Many NA or Null in the data


```python
df= pd.read_csv("ozone.csv")
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Month</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41.0</td>
      <td>190.0</td>
      <td>7.4</td>
      <td>67</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36.0</td>
      <td>118.0</td>
      <td>8.0</td>
      <td>72</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12.0</td>
      <td>149.0</td>
      <td>12.6</td>
      <td>74</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18.0</td>
      <td>313.0</td>
      <td>11.5</td>
      <td>62</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.3</td>
      <td>56</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 153 entries, 0 to 152
    Data columns (total 6 columns):
    Ozone      116 non-null float64
    Solar.R    146 non-null float64
    Wind       153 non-null float64
    Temp       153 non-null int64
    Month      153 non-null int64
    Day        153 non-null int64
    dtypes: float64(3), int64(3)
    memory usage: 7.2 KB
    


```python
# the sum of NA in the dataframe
df.isnull().sum()
```




    Ozone      37
    Solar.R     7
    Wind        0
    Temp        0
    Month       0
    Day         0
    dtype: int64




```python
# the percentage of NA in the dataframe
round((df.isnull().sum()/len(df))*100,2)
```




    Ozone      24.18
    Solar.R     4.58
    Wind        0.00
    Temp        0.00
    Month       0.00
    Day         0.00
    dtype: float64




```python
# Use loc to assign a new value in the dataframe and examplify None is treated as NA
df.loc[4,'Temp']= None
print(df.loc[3:5,:])
df.isnull().sum()
```

       Ozone  Solar.R  Wind  Temp  Month  Day
    3   18.0    313.0  11.5  62.0      5    4
    4    NaN      NaN  14.3   NaN      5    5
    5   28.0      NaN  14.9  66.0      5    6
    




    Ozone      37
    Solar.R     7
    Wind        0
    Temp        1
    Month       0
    Day         0
    dtype: int64




```python
# Use a mask to see the missing values or vice versa
Mask = df.loc[:,:].isnull()
# To see the entries with NA in Ozone column
df[Mask.loc[:,'Ozone']]
#df.loc[Mask.loc[:,'Ozone']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Month</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.3</td>
      <td>NaN</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>194.0</td>
      <td>8.6</td>
      <td>69.0</td>
      <td>5</td>
      <td>10</td>
    </tr>
    <tr>
      <th>24</th>
      <td>NaN</td>
      <td>66.0</td>
      <td>16.6</td>
      <td>57.0</td>
      <td>5</td>
      <td>25</td>
    </tr>
    <tr>
      <th>25</th>
      <td>NaN</td>
      <td>266.0</td>
      <td>14.9</td>
      <td>58.0</td>
      <td>5</td>
      <td>26</td>
    </tr>
    <tr>
      <th>26</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>8.0</td>
      <td>57.0</td>
      <td>5</td>
      <td>27</td>
    </tr>
    <tr>
      <th>31</th>
      <td>NaN</td>
      <td>286.0</td>
      <td>8.6</td>
      <td>78.0</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>32</th>
      <td>NaN</td>
      <td>287.0</td>
      <td>9.7</td>
      <td>74.0</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>33</th>
      <td>NaN</td>
      <td>242.0</td>
      <td>16.1</td>
      <td>67.0</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>34</th>
      <td>NaN</td>
      <td>186.0</td>
      <td>9.2</td>
      <td>84.0</td>
      <td>6</td>
      <td>4</td>
    </tr>
    <tr>
      <th>35</th>
      <td>NaN</td>
      <td>220.0</td>
      <td>8.6</td>
      <td>85.0</td>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>36</th>
      <td>NaN</td>
      <td>264.0</td>
      <td>14.3</td>
      <td>79.0</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>38</th>
      <td>NaN</td>
      <td>273.0</td>
      <td>6.9</td>
      <td>87.0</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>41</th>
      <td>NaN</td>
      <td>259.0</td>
      <td>10.9</td>
      <td>93.0</td>
      <td>6</td>
      <td>11</td>
    </tr>
    <tr>
      <th>42</th>
      <td>NaN</td>
      <td>250.0</td>
      <td>9.2</td>
      <td>92.0</td>
      <td>6</td>
      <td>12</td>
    </tr>
    <tr>
      <th>44</th>
      <td>NaN</td>
      <td>332.0</td>
      <td>13.8</td>
      <td>80.0</td>
      <td>6</td>
      <td>14</td>
    </tr>
    <tr>
      <th>45</th>
      <td>NaN</td>
      <td>322.0</td>
      <td>11.5</td>
      <td>79.0</td>
      <td>6</td>
      <td>15</td>
    </tr>
    <tr>
      <th>51</th>
      <td>NaN</td>
      <td>150.0</td>
      <td>6.3</td>
      <td>77.0</td>
      <td>6</td>
      <td>21</td>
    </tr>
    <tr>
      <th>52</th>
      <td>NaN</td>
      <td>59.0</td>
      <td>1.7</td>
      <td>76.0</td>
      <td>6</td>
      <td>22</td>
    </tr>
    <tr>
      <th>53</th>
      <td>NaN</td>
      <td>91.0</td>
      <td>4.6</td>
      <td>76.0</td>
      <td>6</td>
      <td>23</td>
    </tr>
    <tr>
      <th>54</th>
      <td>NaN</td>
      <td>250.0</td>
      <td>6.3</td>
      <td>76.0</td>
      <td>6</td>
      <td>24</td>
    </tr>
    <tr>
      <th>55</th>
      <td>NaN</td>
      <td>135.0</td>
      <td>8.0</td>
      <td>75.0</td>
      <td>6</td>
      <td>25</td>
    </tr>
    <tr>
      <th>56</th>
      <td>NaN</td>
      <td>127.0</td>
      <td>8.0</td>
      <td>78.0</td>
      <td>6</td>
      <td>26</td>
    </tr>
    <tr>
      <th>57</th>
      <td>NaN</td>
      <td>47.0</td>
      <td>10.3</td>
      <td>73.0</td>
      <td>6</td>
      <td>27</td>
    </tr>
    <tr>
      <th>58</th>
      <td>NaN</td>
      <td>98.0</td>
      <td>11.5</td>
      <td>80.0</td>
      <td>6</td>
      <td>28</td>
    </tr>
    <tr>
      <th>59</th>
      <td>NaN</td>
      <td>31.0</td>
      <td>14.9</td>
      <td>77.0</td>
      <td>6</td>
      <td>29</td>
    </tr>
    <tr>
      <th>60</th>
      <td>NaN</td>
      <td>138.0</td>
      <td>8.0</td>
      <td>83.0</td>
      <td>6</td>
      <td>30</td>
    </tr>
    <tr>
      <th>64</th>
      <td>NaN</td>
      <td>101.0</td>
      <td>10.9</td>
      <td>84.0</td>
      <td>7</td>
      <td>4</td>
    </tr>
    <tr>
      <th>71</th>
      <td>NaN</td>
      <td>139.0</td>
      <td>8.6</td>
      <td>82.0</td>
      <td>7</td>
      <td>11</td>
    </tr>
    <tr>
      <th>74</th>
      <td>NaN</td>
      <td>291.0</td>
      <td>14.9</td>
      <td>91.0</td>
      <td>7</td>
      <td>14</td>
    </tr>
    <tr>
      <th>82</th>
      <td>NaN</td>
      <td>258.0</td>
      <td>9.7</td>
      <td>81.0</td>
      <td>7</td>
      <td>22</td>
    </tr>
    <tr>
      <th>83</th>
      <td>NaN</td>
      <td>295.0</td>
      <td>11.5</td>
      <td>82.0</td>
      <td>7</td>
      <td>23</td>
    </tr>
    <tr>
      <th>101</th>
      <td>NaN</td>
      <td>222.0</td>
      <td>8.6</td>
      <td>92.0</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>102</th>
      <td>NaN</td>
      <td>137.0</td>
      <td>11.5</td>
      <td>86.0</td>
      <td>8</td>
      <td>11</td>
    </tr>
    <tr>
      <th>106</th>
      <td>NaN</td>
      <td>64.0</td>
      <td>11.5</td>
      <td>79.0</td>
      <td>8</td>
      <td>15</td>
    </tr>
    <tr>
      <th>114</th>
      <td>NaN</td>
      <td>255.0</td>
      <td>12.6</td>
      <td>75.0</td>
      <td>8</td>
      <td>23</td>
    </tr>
    <tr>
      <th>118</th>
      <td>NaN</td>
      <td>153.0</td>
      <td>5.7</td>
      <td>88.0</td>
      <td>8</td>
      <td>27</td>
    </tr>
    <tr>
      <th>149</th>
      <td>NaN</td>
      <td>145.0</td>
      <td>13.2</td>
      <td>77.0</td>
      <td>9</td>
      <td>27</td>
    </tr>
  </tbody>
</table>
</div>




```python
# To see the entires Solar.R is not null
df.loc[Mask['Solar.R']!= True]
# To see all the missing values
df[(Mask['Ozone']==True) | (Mask['Solar.R']==True) | (Mask['Temp']==True)]
# To see all the non-null values
df[(Mask['Ozone']!=True) & (Mask['Solar.R']!=True) & (Mask['Temp']!=True)]
# also check notnull() function
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Month</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41.0</td>
      <td>190.0</td>
      <td>7.4</td>
      <td>67.0</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36.0</td>
      <td>118.0</td>
      <td>8.0</td>
      <td>72.0</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12.0</td>
      <td>149.0</td>
      <td>12.6</td>
      <td>74.0</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18.0</td>
      <td>313.0</td>
      <td>11.5</td>
      <td>62.0</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.0</td>
      <td>299.0</td>
      <td>8.6</td>
      <td>65.0</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>19.0</td>
      <td>99.0</td>
      <td>13.8</td>
      <td>59.0</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8.0</td>
      <td>19.0</td>
      <td>20.1</td>
      <td>61.0</td>
      <td>5</td>
      <td>9</td>
    </tr>
    <tr>
      <th>11</th>
      <td>16.0</td>
      <td>256.0</td>
      <td>9.7</td>
      <td>69.0</td>
      <td>5</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>11.0</td>
      <td>290.0</td>
      <td>9.2</td>
      <td>66.0</td>
      <td>5</td>
      <td>13</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14.0</td>
      <td>274.0</td>
      <td>10.9</td>
      <td>68.0</td>
      <td>5</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>18.0</td>
      <td>65.0</td>
      <td>13.2</td>
      <td>58.0</td>
      <td>5</td>
      <td>15</td>
    </tr>
    <tr>
      <th>15</th>
      <td>14.0</td>
      <td>334.0</td>
      <td>11.5</td>
      <td>64.0</td>
      <td>5</td>
      <td>16</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.0</td>
      <td>307.0</td>
      <td>12.0</td>
      <td>66.0</td>
      <td>5</td>
      <td>17</td>
    </tr>
    <tr>
      <th>17</th>
      <td>6.0</td>
      <td>78.0</td>
      <td>18.4</td>
      <td>57.0</td>
      <td>5</td>
      <td>18</td>
    </tr>
    <tr>
      <th>18</th>
      <td>30.0</td>
      <td>322.0</td>
      <td>11.5</td>
      <td>68.0</td>
      <td>5</td>
      <td>19</td>
    </tr>
    <tr>
      <th>19</th>
      <td>11.0</td>
      <td>44.0</td>
      <td>9.7</td>
      <td>62.0</td>
      <td>5</td>
      <td>20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1.0</td>
      <td>8.0</td>
      <td>9.7</td>
      <td>59.0</td>
      <td>5</td>
      <td>21</td>
    </tr>
    <tr>
      <th>21</th>
      <td>11.0</td>
      <td>320.0</td>
      <td>16.6</td>
      <td>73.0</td>
      <td>5</td>
      <td>22</td>
    </tr>
    <tr>
      <th>22</th>
      <td>4.0</td>
      <td>25.0</td>
      <td>9.7</td>
      <td>61.0</td>
      <td>5</td>
      <td>23</td>
    </tr>
    <tr>
      <th>23</th>
      <td>32.0</td>
      <td>92.0</td>
      <td>12.0</td>
      <td>61.0</td>
      <td>5</td>
      <td>24</td>
    </tr>
    <tr>
      <th>27</th>
      <td>23.0</td>
      <td>13.0</td>
      <td>12.0</td>
      <td>67.0</td>
      <td>5</td>
      <td>28</td>
    </tr>
    <tr>
      <th>28</th>
      <td>45.0</td>
      <td>252.0</td>
      <td>14.9</td>
      <td>81.0</td>
      <td>5</td>
      <td>29</td>
    </tr>
    <tr>
      <th>29</th>
      <td>115.0</td>
      <td>223.0</td>
      <td>5.7</td>
      <td>79.0</td>
      <td>5</td>
      <td>30</td>
    </tr>
    <tr>
      <th>30</th>
      <td>37.0</td>
      <td>279.0</td>
      <td>7.4</td>
      <td>76.0</td>
      <td>5</td>
      <td>31</td>
    </tr>
    <tr>
      <th>37</th>
      <td>29.0</td>
      <td>127.0</td>
      <td>9.7</td>
      <td>82.0</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>39</th>
      <td>71.0</td>
      <td>291.0</td>
      <td>13.8</td>
      <td>90.0</td>
      <td>6</td>
      <td>9</td>
    </tr>
    <tr>
      <th>40</th>
      <td>39.0</td>
      <td>323.0</td>
      <td>11.5</td>
      <td>87.0</td>
      <td>6</td>
      <td>10</td>
    </tr>
    <tr>
      <th>43</th>
      <td>23.0</td>
      <td>148.0</td>
      <td>8.0</td>
      <td>82.0</td>
      <td>6</td>
      <td>13</td>
    </tr>
    <tr>
      <th>46</th>
      <td>21.0</td>
      <td>191.0</td>
      <td>14.9</td>
      <td>77.0</td>
      <td>6</td>
      <td>16</td>
    </tr>
    <tr>
      <th>47</th>
      <td>37.0</td>
      <td>284.0</td>
      <td>20.7</td>
      <td>72.0</td>
      <td>6</td>
      <td>17</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>122</th>
      <td>85.0</td>
      <td>188.0</td>
      <td>6.3</td>
      <td>94.0</td>
      <td>8</td>
      <td>31</td>
    </tr>
    <tr>
      <th>123</th>
      <td>96.0</td>
      <td>167.0</td>
      <td>6.9</td>
      <td>91.0</td>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <th>124</th>
      <td>78.0</td>
      <td>197.0</td>
      <td>5.1</td>
      <td>92.0</td>
      <td>9</td>
      <td>2</td>
    </tr>
    <tr>
      <th>125</th>
      <td>73.0</td>
      <td>183.0</td>
      <td>2.8</td>
      <td>93.0</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <th>126</th>
      <td>91.0</td>
      <td>189.0</td>
      <td>4.6</td>
      <td>93.0</td>
      <td>9</td>
      <td>4</td>
    </tr>
    <tr>
      <th>127</th>
      <td>47.0</td>
      <td>95.0</td>
      <td>7.4</td>
      <td>87.0</td>
      <td>9</td>
      <td>5</td>
    </tr>
    <tr>
      <th>128</th>
      <td>32.0</td>
      <td>92.0</td>
      <td>15.5</td>
      <td>84.0</td>
      <td>9</td>
      <td>6</td>
    </tr>
    <tr>
      <th>129</th>
      <td>20.0</td>
      <td>252.0</td>
      <td>10.9</td>
      <td>80.0</td>
      <td>9</td>
      <td>7</td>
    </tr>
    <tr>
      <th>130</th>
      <td>23.0</td>
      <td>220.0</td>
      <td>10.3</td>
      <td>78.0</td>
      <td>9</td>
      <td>8</td>
    </tr>
    <tr>
      <th>131</th>
      <td>21.0</td>
      <td>230.0</td>
      <td>10.9</td>
      <td>75.0</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>132</th>
      <td>24.0</td>
      <td>259.0</td>
      <td>9.7</td>
      <td>73.0</td>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>133</th>
      <td>44.0</td>
      <td>236.0</td>
      <td>14.9</td>
      <td>81.0</td>
      <td>9</td>
      <td>11</td>
    </tr>
    <tr>
      <th>134</th>
      <td>21.0</td>
      <td>259.0</td>
      <td>15.5</td>
      <td>76.0</td>
      <td>9</td>
      <td>12</td>
    </tr>
    <tr>
      <th>135</th>
      <td>28.0</td>
      <td>238.0</td>
      <td>6.3</td>
      <td>77.0</td>
      <td>9</td>
      <td>13</td>
    </tr>
    <tr>
      <th>136</th>
      <td>9.0</td>
      <td>24.0</td>
      <td>10.9</td>
      <td>71.0</td>
      <td>9</td>
      <td>14</td>
    </tr>
    <tr>
      <th>137</th>
      <td>13.0</td>
      <td>112.0</td>
      <td>11.5</td>
      <td>71.0</td>
      <td>9</td>
      <td>15</td>
    </tr>
    <tr>
      <th>138</th>
      <td>46.0</td>
      <td>237.0</td>
      <td>6.9</td>
      <td>78.0</td>
      <td>9</td>
      <td>16</td>
    </tr>
    <tr>
      <th>139</th>
      <td>18.0</td>
      <td>224.0</td>
      <td>13.8</td>
      <td>67.0</td>
      <td>9</td>
      <td>17</td>
    </tr>
    <tr>
      <th>140</th>
      <td>13.0</td>
      <td>27.0</td>
      <td>10.3</td>
      <td>76.0</td>
      <td>9</td>
      <td>18</td>
    </tr>
    <tr>
      <th>141</th>
      <td>24.0</td>
      <td>238.0</td>
      <td>10.3</td>
      <td>68.0</td>
      <td>9</td>
      <td>19</td>
    </tr>
    <tr>
      <th>142</th>
      <td>16.0</td>
      <td>201.0</td>
      <td>8.0</td>
      <td>82.0</td>
      <td>9</td>
      <td>20</td>
    </tr>
    <tr>
      <th>143</th>
      <td>13.0</td>
      <td>238.0</td>
      <td>12.6</td>
      <td>64.0</td>
      <td>9</td>
      <td>21</td>
    </tr>
    <tr>
      <th>144</th>
      <td>23.0</td>
      <td>14.0</td>
      <td>9.2</td>
      <td>71.0</td>
      <td>9</td>
      <td>22</td>
    </tr>
    <tr>
      <th>145</th>
      <td>36.0</td>
      <td>139.0</td>
      <td>10.3</td>
      <td>81.0</td>
      <td>9</td>
      <td>23</td>
    </tr>
    <tr>
      <th>146</th>
      <td>7.0</td>
      <td>49.0</td>
      <td>10.3</td>
      <td>69.0</td>
      <td>9</td>
      <td>24</td>
    </tr>
    <tr>
      <th>147</th>
      <td>14.0</td>
      <td>20.0</td>
      <td>16.6</td>
      <td>63.0</td>
      <td>9</td>
      <td>25</td>
    </tr>
    <tr>
      <th>148</th>
      <td>30.0</td>
      <td>193.0</td>
      <td>6.9</td>
      <td>70.0</td>
      <td>9</td>
      <td>26</td>
    </tr>
    <tr>
      <th>150</th>
      <td>14.0</td>
      <td>191.0</td>
      <td>14.3</td>
      <td>75.0</td>
      <td>9</td>
      <td>28</td>
    </tr>
    <tr>
      <th>151</th>
      <td>18.0</td>
      <td>131.0</td>
      <td>8.0</td>
      <td>76.0</td>
      <td>9</td>
      <td>29</td>
    </tr>
    <tr>
      <th>152</th>
      <td>20.0</td>
      <td>223.0</td>
      <td>11.5</td>
      <td>68.0</td>
      <td>9</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
<p>111 rows × 6 columns</p>
</div>




```python
# stats check of dataframe
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Month</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>116.000000</td>
      <td>146.000000</td>
      <td>153.000000</td>
      <td>152.000000</td>
      <td>153.000000</td>
      <td>153.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>42.129310</td>
      <td>185.931507</td>
      <td>9.957516</td>
      <td>78.026316</td>
      <td>6.993464</td>
      <td>15.803922</td>
    </tr>
    <tr>
      <th>std</th>
      <td>32.987885</td>
      <td>90.058422</td>
      <td>3.523001</td>
      <td>9.326987</td>
      <td>1.416522</td>
      <td>8.864520</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>1.700000</td>
      <td>57.000000</td>
      <td>5.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>18.000000</td>
      <td>115.750000</td>
      <td>7.400000</td>
      <td>72.750000</td>
      <td>6.000000</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>31.500000</td>
      <td>205.000000</td>
      <td>9.700000</td>
      <td>79.000000</td>
      <td>7.000000</td>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>63.250000</td>
      <td>258.750000</td>
      <td>11.500000</td>
      <td>85.000000</td>
      <td>8.000000</td>
      <td>23.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>168.000000</td>
      <td>334.000000</td>
      <td>20.700000</td>
      <td>97.000000</td>
      <td>9.000000</td>
      <td>31.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# customized stats check
df.describe(percentiles=[0.125,0.25,0.5,0.75])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Month</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>116.000000</td>
      <td>146.000000</td>
      <td>153.000000</td>
      <td>152.000000</td>
      <td>153.000000</td>
      <td>153.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>42.129310</td>
      <td>185.931507</td>
      <td>9.957516</td>
      <td>78.026316</td>
      <td>6.993464</td>
      <td>15.803922</td>
    </tr>
    <tr>
      <th>std</th>
      <td>32.987885</td>
      <td>90.058422</td>
      <td>3.523001</td>
      <td>9.326987</td>
      <td>1.416522</td>
      <td>8.864520</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>1.700000</td>
      <td>57.000000</td>
      <td>5.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>12.5%</th>
      <td>12.000000</td>
      <td>59.625000</td>
      <td>6.300000</td>
      <td>66.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>18.000000</td>
      <td>115.750000</td>
      <td>7.400000</td>
      <td>72.750000</td>
      <td>6.000000</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>31.500000</td>
      <td>205.000000</td>
      <td>9.700000</td>
      <td>79.000000</td>
      <td>7.000000</td>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>63.250000</td>
      <td>258.750000</td>
      <td>11.500000</td>
      <td>85.000000</td>
      <td>8.000000</td>
      <td>23.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>168.000000</td>
      <td>334.000000</td>
      <td>20.700000</td>
      <td>97.000000</td>
      <td>9.000000</td>
      <td>31.000000</td>
    </tr>
  </tbody>
</table>
</div>



### Filetring Out Missing Values dropna()


```python
cleaned = df.dropna(axis=0,inplace=False) # axis=1 will drop the entire column with NA
cleaned.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 111 entries, 0 to 152
    Data columns (total 6 columns):
    Ozone      111 non-null float64
    Solar.R    111 non-null float64
    Wind       111 non-null float64
    Temp       111 non-null float64
    Month      111 non-null int64
    Day        111 non-null int64
    dtypes: float64(4), int64(2)
    memory usage: 6.1 KB
    


```python
# drop columns
df.dropna(axis=1,inplace=False).head()
df.drop(labels=['Ozone','Solar.R','Temp'],axis=1,inplace=False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Wind</th>
      <th>Month</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.4</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8.0</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12.6</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.5</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14.3</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# drop rows
df.drop(labels=np.arange(0,5),axis=0,inplace=False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Month</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>28.0</td>
      <td>NaN</td>
      <td>14.9</td>
      <td>66.0</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.0</td>
      <td>299.0</td>
      <td>8.6</td>
      <td>65.0</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>19.0</td>
      <td>99.0</td>
      <td>13.8</td>
      <td>59.0</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8.0</td>
      <td>19.0</td>
      <td>20.1</td>
      <td>61.0</td>
      <td>5</td>
      <td>9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>194.0</td>
      <td>8.6</td>
      <td>69.0</td>
      <td>5</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



##### df.dropna(how='all'/'any',axis=0/1,inplace=True/False)

### Filling in Missing Values


```python
df2=pd.DataFrame(np.random.randn(6,3))
df2.iloc[4:,2]=None
df2.iloc[2:,1]=None
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.625757</td>
      <td>-0.331247</td>
      <td>-0.035861</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.770574</td>
      <td>-0.433586</td>
      <td>0.465793</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.583958</td>
      <td>NaN</td>
      <td>-1.002063</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.730456</td>
      <td>NaN</td>
      <td>-1.859202</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.130777</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.154202</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Use fillna() funcion to fill NA with a specific value
df2.fillna(0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.625757</td>
      <td>-0.331247</td>
      <td>-0.035861</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.770574</td>
      <td>-0.433586</td>
      <td>0.465793</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.583958</td>
      <td>0.000000</td>
      <td>-1.002063</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.730456</td>
      <td>0.000000</td>
      <td>-1.859202</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.130777</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.154202</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# fill NA with prespecified values by column index
df2.fillna({1:7,2:77})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.625757</td>
      <td>-0.331247</td>
      <td>-0.035861</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.770574</td>
      <td>-0.433586</td>
      <td>0.465793</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.583958</td>
      <td>7.000000</td>
      <td>-1.002063</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.730456</td>
      <td>7.000000</td>
      <td>-1.859202</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.130777</td>
      <td>7.000000</td>
      <td>77.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.154202</td>
      <td>7.000000</td>
      <td>77.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[4]=[0.0343,0.244,-0.936,None,0.7128,1.415]
# fill na with the mean of non na's in the column
df2.fillna(value=df2.mean())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.625757</td>
      <td>-0.331247</td>
      <td>-0.035861</td>
      <td>0.03430</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.770574</td>
      <td>-0.433586</td>
      <td>0.465793</td>
      <td>0.24400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.583958</td>
      <td>-0.382417</td>
      <td>-1.002063</td>
      <td>-0.93600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.730456</td>
      <td>-0.382417</td>
      <td>-1.859202</td>
      <td>0.29402</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.130777</td>
      <td>-0.382417</td>
      <td>-0.607833</td>
      <td>0.71280</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.154202</td>
      <td>-0.382417</td>
      <td>-0.607833</td>
      <td>1.41500</td>
    </tr>
  </tbody>
</table>
</div>



## Data Transformation
Instead of looping though a dataframe, Pandas favors using vectorized functions that operate column by column.

### Remove Duplicates


```python
df3=pd.DataFrame({'Mark':[19,93,0,9,0,4],'Jackson':[19,94,0,3,0,28],'JB':[19,94,0,1,0]+[6]})
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mark</th>
      <th>Jackson</th>
      <th>JB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>19</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>93</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>28</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# dataframe.duplicated returns boolean
df3.duplicated()
```




    0    False
    1    False
    2    False
    3    False
    4     True
    5    False
    dtype: bool




```python
# dataframe.unique() to check the unique values in a column/ array
df3.JB.unique()
```




    array([19, 94,  0,  1,  6], dtype=int64)




```python
# get the number of unique values in a column
df3.Jackson.nunique()
```




    5



#### drop_duplicates() function


```python
df3.drop_duplicates(inplace=False)
# by default the drop_duplicates() function will drop the duplicated rows
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mark</th>
      <th>Jackson</th>
      <th>JB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>19</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>93</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>28</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3['savage']=[1,2,1,2,1,2]
df3.drop_duplicates(['savage'])
# assign specific column index to drop the row with duplicated values in this column
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mark</th>
      <th>Jackson</th>
      <th>JB</th>
      <th>savage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>93</td>
      <td>94</td>
      <td>94</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Transpose Dataframe


```python
df3.T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mark</th>
      <td>19</td>
      <td>93</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Jackson</th>
      <td>19</td>
      <td>94</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>28</td>
    </tr>
    <tr>
      <th>JB</th>
      <td>19</td>
      <td>94</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>savage</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.T.drop_duplicates([1])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mark</th>
      <td>19</td>
      <td>93</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Jackson</th>
      <td>19</td>
      <td>94</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>28</td>
    </tr>
    <tr>
      <th>savage</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Transformaing Data Using a Function or Mapping


```python
df4=pd.DataFrame({'GOT7':['JB','Mark','Jackson','Jinyoung','Youngjae','Bambam','Yugyeom'], 'birthmonth': [1,9,3,9,9,5,11]})
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>birthmonth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JB</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# using a dict as a map to transform
# create a dictionary
nickname={'JB':'Def','Mark':'XCIII','Jackson':'Sennie','Jinyoung':'JYP','Youngjae':'ARS','Yugyeom':'YG','Bambam':'Doubel B'}
nickname
```




    {'JB': 'Def',
     'Mark': 'XCIII',
     'Jackson': 'Sennie',
     'Jinyoung': 'JYP',
     'Youngjae': 'ARS',
     'Yugyeom': 'YG',
     'Bambam': 'Doubel B'}




```python
track={'JB':'Sunrise','Mark':'OMW','Jackson':'Made It','Jinyoung':'My Youth','Youngjae':'Nobody Knows','Bambam':'Party','Yugyeom':'Fine'
      }
track
```




    {'JB': 'Sunrise',
     'Mark': 'OMW',
     'Jackson': 'Made It',
     'Jinyoung': 'My Youth',
     'Youngjae': 'Nobody Knows',
     'Bambam': 'Party',
     'Yugyeom': 'Fine'}




```python
# use the map() 
df4['nickname']=df4['GOT7'].map(nickname) # notice dataframe object has no attribute 'map' 
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>birthmonth</th>
      <th>nickname</th>
      <th>Track</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JB</td>
      <td>1</td>
      <td>Def</td>
      <td>Sunrise</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
      <td>XCIII</td>
      <td>OMW</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
      <td>Sennie</td>
      <td>Made It</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
      <td>JYP</td>
      <td>My Youth</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
      <td>ARS</td>
      <td>Nobody Knows</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
      <td>Doubel B</td>
      <td>Party</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
      <td>YG</td>
      <td>Fine</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4['Track']=df4['GOT7'].map(lambda x: track[x])
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>birthmonth</th>
      <th>nickname</th>
      <th>Track</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JB</td>
      <td>1</td>
      <td>Def</td>
      <td>Sunrise</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
      <td>XCIII</td>
      <td>OMW</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
      <td>Sennie</td>
      <td>Made It</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
      <td>JYP</td>
      <td>My Youth</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
      <td>ARS</td>
      <td>Nobody Knows</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
      <td>Doubel B</td>
      <td>Party</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
      <td>YG</td>
      <td>Fine</td>
    </tr>
  </tbody>
</table>
</div>



#### Use apply() to transform dataframe


```python
df.apply(lambda x: x.max())
```




    Ozone      168.0
    Solar.R    334.0
    Wind        20.7
    Temp        97.0
    Month        9.0
    Day         31.0
    dtype: float64




```python
df.apply(lambda x:x.mean())
# or df.apply(lambda x:np.mean(x))
```




    Ozone       42.129310
    Solar.R    185.931507
    Wind         9.957516
    Temp        78.026316
    Month        6.993464
    Day         15.803922
    dtype: float64




```python
# apply function to specifc columns
df.iloc[:,1:3].apply(lambda x: x.mean())
```




    Solar.R    185.931507
    Wind         9.957516
    dtype: float64




```python
df['max-min']=df.loc[:,['Ozone','Temp']].apply(lambda x: abs(max(x)-min(x)), axis=1)
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
      <th>Solar.R</th>
      <th>Wind</th>
      <th>Temp</th>
      <th>Month</th>
      <th>Day</th>
      <th>max-min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41.0</td>
      <td>190.0</td>
      <td>7.4</td>
      <td>67.0</td>
      <td>5</td>
      <td>1</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36.0</td>
      <td>118.0</td>
      <td>8.0</td>
      <td>72.0</td>
      <td>5</td>
      <td>2</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12.0</td>
      <td>149.0</td>
      <td>12.6</td>
      <td>74.0</td>
      <td>5</td>
      <td>3</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18.0</td>
      <td>313.0</td>
      <td>11.5</td>
      <td>62.0</td>
      <td>5</td>
      <td>4</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.3</td>
      <td>NaN</td>
      <td>5</td>
      <td>5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>28.0</td>
      <td>NaN</td>
      <td>14.9</td>
      <td>66.0</td>
      <td>5</td>
      <td>6</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.0</td>
      <td>299.0</td>
      <td>8.6</td>
      <td>65.0</td>
      <td>5</td>
      <td>7</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>19.0</td>
      <td>99.0</td>
      <td>13.8</td>
      <td>59.0</td>
      <td>5</td>
      <td>8</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8.0</td>
      <td>19.0</td>
      <td>20.1</td>
      <td>61.0</td>
      <td>5</td>
      <td>9</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>194.0</td>
      <td>8.6</td>
      <td>69.0</td>
      <td>5</td>
      <td>10</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 7 entries, 0 to 6
    Data columns (total 4 columns):
    GOT7          7 non-null object
    birthmonth    7 non-null int64
    nickname      7 non-null object
    Track         7 non-null object
    dtypes: int64(1), object(3)
    memory usage: 304.0+ bytes
    


```python
# create a new function
def seven_or_nothing(content):
    if type(content==int):
        return content + 7
    else: raise(TypeError)
```


```python
df4.loc[:,'birthmonth'].apply(seven_or_nothing)
```




    0     8
    1    16
    2    10
    3    16
    4    16
    5    12
    6    18
    Name: birthmonth, dtype: int64




```python
def seven_forever(dataframe):
    if type(dataframe==object):
        return dataframe + "GOT7"        
```


```python
df4.loc[:,'Track'].apply(seven_forever)
```




    0         SunriseGOT7
    1             OMWGOT7
    2         Made ItGOT7
    3        My YouthGOT7
    4    Nobody KnowsGOT7
    5           PartyGOT7
    6            FineGOT7
    Name: Track, dtype: object




```python
type(df[['Ozone']]) # both column index and row index
```




    pandas.core.frame.DataFrame




```python
type(df['Ozone']) # only row index
```




    pandas.core.series.Series



## Replacing Values


```python
# use where function to change/replace values
df[['Ozone']].where((df['Ozone']>20) & (df['Wind']<10), np.nan, axis=0).head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Ozone']].where((df['Ozone']>20) & (df['Wind']<10), 777 , axis=0).head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ozone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>777.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>777.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>777.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>777.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>777.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>777.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>777.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#replace()
df4.replace(['JB','YG'],['Jaebeom','Gyeomy'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>birthmonth</th>
      <th>nickname</th>
      <th>Track</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jaebeom</td>
      <td>1</td>
      <td>Def</td>
      <td>Sunrise</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
      <td>XCIII</td>
      <td>OMW</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
      <td>Sennie</td>
      <td>Made It</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
      <td>JYP</td>
      <td>My Youth</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
      <td>ARS</td>
      <td>Nobody Knows</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
      <td>Doubel B</td>
      <td>Party</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
      <td>Gyeomy</td>
      <td>Fine</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.replace({'JB':'Strawberry Milk','YG':'Ice Choco'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>birthmonth</th>
      <th>nickname</th>
      <th>Track</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Strawberry Milk</td>
      <td>1</td>
      <td>Def</td>
      <td>Sunrise</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
      <td>XCIII</td>
      <td>OMW</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
      <td>Sennie</td>
      <td>Made It</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
      <td>JYP</td>
      <td>My Youth</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
      <td>ARS</td>
      <td>Nobody Knows</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
      <td>Doubel B</td>
      <td>Party</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
      <td>Ice Choco</td>
      <td>Fine</td>
    </tr>
  </tbody>
</table>
</div>



## Rename or Add Columns


```python
df4.rename(columns={'birthmonth':'Month','Track':'Song'},inplace=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>Month</th>
      <th>nickname</th>
      <th>Song</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JB</td>
      <td>1</td>
      <td>Def</td>
      <td>Sunrise</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
      <td>XCIII</td>
      <td>OMW</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
      <td>Sennie</td>
      <td>Made It</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
      <td>JYP</td>
      <td>My Youth</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
      <td>ARS</td>
      <td>Nobody Knows</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
      <td>Doubel B</td>
      <td>Party</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
      <td>YG</td>
      <td>Fine</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.columns=['GOT7','Month','Nickname','Song']
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>Month</th>
      <th>Nickname</th>
      <th>Song</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JB</td>
      <td>1</td>
      <td>Def</td>
      <td>Sunrise</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
      <td>XCIII</td>
      <td>OMW</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
      <td>Sennie</td>
      <td>Made It</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
      <td>JYP</td>
      <td>My Youth</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
      <td>ARS</td>
      <td>Nobody Knows</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
      <td>Doubel B</td>
      <td>Party</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
      <td>YG</td>
      <td>Fine</td>
    </tr>
  </tbody>
</table>
</div>



## Merge/Join and Concatenate


```python
df5 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df6 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': [0,1,2]})
df7 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data3': [10,11,12]})
df8 = pd.DataFrame({'key': ['a', 'b', 'd','e','f'],
                    'data4': [0,1,2,3,4]})
```


```python
# Merge same shape and keys
# Pandas will merge on the intersection of common named columns or index
pd.merge(df6,df7)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>data2</th>
      <th>data3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>2</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df6,df7,on='key')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>data2</th>
      <th>data3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>2</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
df6.join(df7.data3,how='inner')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>data2</th>
      <th>data3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>2</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df5,df6, on='key')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>data1</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>a</td>
      <td>5</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df5.join(df6,how='outer',lsuffix='_a', rsuffix='_b')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key_a</th>
      <th>data1</th>
      <th>key_b</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>0</td>
      <td>a</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>b</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>2</td>
      <td>d</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>a</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>b</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df5,df6,on='key',how='left')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>data1</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>2</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>4</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>a</td>
      <td>5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>b</td>
      <td>6</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df5,df6,on='key',how='right')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>data1</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>6.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>2.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>4.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>a</td>
      <td>5.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>d</td>
      <td>NaN</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df5,df6,on='key',how='outer')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>data1</th>
      <th>data2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>6.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>a</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>c</td>
      <td>3.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>d</td>
      <td>NaN</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



### Concatination of data frames


```python
DF=pd.DataFrame({'GOT7':['JB','Mark','Jackson','Jinyoung'],'Month':[1,9,3,9]})
DF2=pd.DataFrame({'GOT7':['Youngjae','Bambam','Yugyeom'],'Month':[9,5,11]})
```


```python
GOT7=pd.concat([DF,DF2],axis=0,ignore_index=True)
GOT7
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JB</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
DF3=pd.DataFrame({'Track':['Sunrise','OMW','Made It','My Youth','Nobody Knows','Party','Fine']})
```


```python
GOT7=pd.concat([GOT7,DF3],axis=1,ignore_index=False)
GOT7
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GOT7</th>
      <th>Month</th>
      <th>Track</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JB</td>
      <td>1</td>
      <td>Sunrise</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mark</td>
      <td>9</td>
      <td>OMW</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jackson</td>
      <td>3</td>
      <td>Made It</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jinyoung</td>
      <td>9</td>
      <td>My Youth</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Youngjae</td>
      <td>9</td>
      <td>Nobody Knows</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bambam</td>
      <td>5</td>
      <td>Party</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yugyeom</td>
      <td>11</td>
      <td>Fine</td>
    </tr>
  </tbody>
</table>
</div>


