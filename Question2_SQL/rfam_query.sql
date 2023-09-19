
-- In This query as coonected to Database Rfam in server mysql-rfam-public.ebi.ac.uk

-- a1. How many types of tigers can be found in the taxonomy table of the dataset? What is the 'ncbi_id' of the Sumatran Tiger?
SELECT COUNT(*) typ_Tigers
FROM (
    SELECT tx.species
    FROM taxonomy tx
    WHERE tx.species LIKE '%Panthera tigris%') sub; -- HERE species name of tiger is Panthera tigris
-- The answerser form the database I got answer 8.

-- a2. What is the 'ncbi_id' of the Sumatran Tiger?
SELECT tx.ncbi_id
FROM taxonomy tx
WHERE tx.species LIKE '%Panthera tigris sumatrae%';
-- The ncbi_id from database is 9695

--b. Find all the columns that can be used to connect the tables in the given database
DESC TABLE_NAME; -- Here TABLE_NMAE ARE 'taxonomy', 'rfamseq', 'family', 'clan', 'clan_membership', 'full_region'
--in KEY column look for the value MUL as I am in mysql server.
--           OR
-- I assumed that column_name in every table will have the same name
SELECT sub.COLUMN_NAME
FROM (
    SELECT DISTINCT TABLE_NAME, COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'Rfam' AND
    TABLE_NAME IN ('taxonomy', 'rfamseq', 'family', 'clan', 'clan_membership', 'full_region')
    ) sub
GROUP BY sub.COLUMN_NAME
HAVING COUNT(DISTINCT sub.TABLE_NAME) > 1;

-- c.	Which type of rice has the longest DNA sequence?
SELECT tx.species AS species
FROM rfamseq rf
JOIN taxonomy tx
ON tx.ncbi_id = rf.ncbi_id AND tx.species LIKE '%Oryza sativa%'
ORDER BY rf.length DESC
LIMIT 1;

-- d. We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length)
--    where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return
--    the 9th page when there are 15 results per page.
SELECT fr.rfam_acc, rf.length -- Here rfam_acc is family access and rfam_id is family name
FROM rfamseq rf
JOIN full_region fr
ON rf.rfamseq_acc = fr.rfamseq_acc
JOIN family fa
ON fr.rfam_acc = fa.rfam_acc
ORDER BY rf.length DESC
LIMIT 15 OFFSET 120; --skips the first 8 pages (8 * 15 = 120 rows) to get to the 9th page of results
