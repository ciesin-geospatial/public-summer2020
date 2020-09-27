Data cleaning on DRC data

Data sources include DRC_Acasus_health_facility_all_merged and DRC_WHO_health_facility_all_merged.

**Single Source Evaluation.ipynb:**

evaluate points in a single data source, drop duplicates and unreliable data poitns.

- first phase: 
  - find clusters of radius 100m and conduct fuzzy match on cleaned facility names.
  - points within the same cluster and matched to the same name are considered one subcluster.
  - cluster ratio is calculated using subcluster size / cluster size.
  - subclusters are evaluated based on cluster size and cluster ratio. (0: drop, 1: keep, 2: maybe)
  - subclusters with eval=0 are dropped, for subclusters with eval=1 or 2, the most recent data entry is kept such that only one point is representing a subcluster.

- second phase:
  - find new clusters of radius 1km.
  - 2nd round evaluation within the new cluster based on 1st round evaluation values (eval_1). (0: drop, 1: keep)
  - if the new cluster contains points with both eval_1=1 and eval_1=2, only points with eval_1=1 are kept.
  - if there are either eval_1=1 points or eval_1=2 points, the point with largest subcluster size is kept.
  
**Combining Sources.ipynb:**

Combine 2 data sources and find facilities that exist in both datasets.

- New clusters created using the combined dataset and a radius of 100m.
- Fuzzy match on facility name is applied to points within a cluster. Points within the same cluster and matched to the same name are considered one subcluster.
- Create a `val` column. (1: points in the subcluster are from both sources. 0: otherwise)
- The same approach is also applied but considers facility type as well.
