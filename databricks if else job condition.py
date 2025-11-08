# in a noteobook you can have a command box like this
dbutils.jobs.taskValues.set(key="has_duplicates", value=duplicate_exists)

# where duplicate_exists is a dataframe of duplicate values if there are any (executed in the notebook)
# then in your Jobs pipeline you add a task "if /else condition", then in jobs pipeline task window look for "condition" and "tasks.notebookname.values.has_duplicates"

#from databricks engineering learning path. https://customer-academy.databricks.com/learn/learning-plans/10/data-engineer-learning-plan/courses/1365/deploy-workloads-with-lakeflow-jobs/lessons/45959/demo-building-dynamic-workloads-with-advanced-tasks
