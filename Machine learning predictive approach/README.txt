This is a response to a prompt regarding analysis of chilhood development 
across primary health networks in Australia.

Approach:
The approach in this attempt was centred around machine learning algorithms trained
on past PHIDU data in an attempt to create an model that can predict factors of risk 
for development in a population to better target preventative health programs to reduce
burden of disease and mitigate developmental issues in the population.

The data used is from the PHIDU report every year the AEDC is conducted

This was then compared to the demographic of each LGA, to understand and evaluate if there
are any populations that are more at risk compared to others and what can be done to 
begin to make decisions to solve this issue.

Parser:
the parser splits the data up into machine readable format. to pull dataset that will be used
for machine learning, use the .dataset method. to pull an individual sheet, use the .data('sheetname') method.
hospital admission data has been abbrivated to hosp_ad, all other sheets remain as they are in the PHIDU
dataset.