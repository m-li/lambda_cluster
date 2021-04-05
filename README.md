Lambda Cluster
==============
A cluster that uses lambda or similar serverless framework to run parallel jobs.  
The concept is each work load should be completed in 15 minutes.  
This allows lambdas to be used but also enforces check pointing so spot instances can be used as well.  
Check pointing ideally would be done by an in memory cache but an alternative has been to use aurora severless.  
This allows the cache to scale as needed but not have any idle costs.  
Given lambda now uses containers the idea is to ship the base requirements as a container then send small bits of code that will be eval'd in the lambda.  
This allows for very fast iteration time.  
After this is done it should be easy enough to package it up into a script and container so batch can be done.  
Ideally wrapper scrips and functions will be used to make everything transparent.  

Containers
----------
Base: This image contains only the libraries needed  
Lambda: This image is derived from the base and contains the thin handler to execute sent code  
Batch: This image is derived from the base and contains all batch scripts  

The idea is that code is developed using small functions and building blocks that are parallelized using lambda.  
Then batched using aws batch. Both use the same container to allow for rapid scaling.  
