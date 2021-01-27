# CombinePlans

CombinePlans.py - Combine RTML files with different targets into one plan

Example usage: 
>python CombinePlans.py StandardStar.rtml Target.rtml

There is no maximum to the number of files that can be combined.
Each file should only contain one plan and one target, otherwise only the first plan and target is used.
Only the constraints from the first plan are used for the output
Output file will be overwritten if it already exists
