# Import the pandas library
import pandas as pd
import os
os.chdir('/users/joshcolclough/desktop')

# Read in the data
data = pd.read_csv("gz_decals_volunteers_5.csv")

# First data selection
# Select galaxies whith featured-or-disk
featuresordisk1 = data[data["smooth-or-featured_featured-or-disk_fraction"] > 0.8]

# Print the selected rows
#print(featuresordisk1)

# Select galaxies with edgeondisk
edgeon1 = featuresordisk1[featuresordisk1["disk-edge-on_yes_fraction"] > 0.8]

#print(edgeon1)

# Select galaxies whith noedgeonbulge
edgeonbulge1 = edgeon1[edgeon1["edge-on-bulge_none_fraction"] > 0.8]

print(edgeonbulge1)


# Second data selection
# Select galaxies whith featured-or-disk
featuresordisk2 = data[data["smooth-or-featured_featured-or-disk_fraction"] > 0.8]

# Select galaxies with noedgeondisk
noedgeon2 = featuresordisk2[featuresordisk2["disk-edge-on_no_fraction"] > 0.8]

nospiralarms2 = noedgeon2[noedgeon2["has-spiral-arms_no_fraction"] > 0.8]

nobulge2 = nospiralarms2[nospiralarms2["bulge-size_none_fraction"] > 0.8]

print(nobulge2)

yesspiralarms2 = noedgeon2[noedgeon2["has-spiral-arms_yes_fraction"] > 0.8]

nobulgespiral2 = yesspiralarms2[yesspiralarms2["bulge-size_none_fraction"] > 0.8]

print(nobulgespiral2)

dataset = pd.concat([edgeonbulge1,nobulge2,nobulgespiral2]).drop_duplicates().reset_index(drop=True)

dataset.to_csv('dataset.csv')

