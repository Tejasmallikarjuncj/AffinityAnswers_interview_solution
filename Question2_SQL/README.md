The solution for sql questions are in the file rfam_query.sql

There are four sub question.

a. How many types of tigers can be found in the taxonomy table of the dataset? What is the 'ncbi_id' of the Sumatran Tiger? 
What is the 'ncbi_id' of the Sumatran Tiger?

b. Find all the columns that can be used to connect the tables in the given database

c. Which type of rice has the longest DNA sequence?

d. We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length)
where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return
the 9th page when there are 15 results per page.

The answer for each questions is written below the question, where question are wriiten in comments.
for instance.

``` SQL Query
-- a1. How many types of tigers can be found in the taxonomy table of the dataset? What is the 'ncbi_id' of the Sumatran Tiger?
SELECT COUNT(*) typ_Tigers
FROM (
    SELECT tx.species
    FROM taxonomy tx
    WHERE tx.species LIKE '%Panthera tigris%') sub; -- HERE species name of tiger is Panthera tigris
```
