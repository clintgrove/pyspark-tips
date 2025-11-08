# in a noteobook you can have a command box like this
dbutils.jobs.taskValues.set(key="has_duplicates", value=duplicate_exists)

# where duplicate_exists is a dataframe of duplicate values if there are any (executed in the notebook)
# then in your Jobs pipeline you add a task "if /else condition", then in jobs pipeline task window look for "condition" and "tasks.notebookname.values.has_duplicates"
