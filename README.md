# Benford-Like-Example
2021-10-24. An example showing how we can fit a Benford-like distribution to data using Python.

Benford's Law assumes a specific, familiar shape. 1 should account for 30.1% of first significant digits, etc. However, it is possible to parameterize Benford's Law to include a variety of different shapes. Deciding what the values of those parameters are for any data set is a necessary, but not entirely easy, step.

This is an example of using scipy.optimize.curve_fit to select those parameters. It ingests a data file (provided in the repo), extracts the significant digits, and then optimizes the parameters of the Benford-like Law. 
