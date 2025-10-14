# Dynamo db schema

### ECSTaskConfig dynamodb table:
```
TaskID => UniqueID
ProjectName => Project Name
S3Key => .py or .zip file path
MainFileName => main file or File Entry to start executing
Bucket => where the code solution is located in s3
Cluster => ecs Cluster name
TaskDependencyID => if task depends on another task
LaunchType => FARGATE or EC2
TargetPhase => the ddefinedresources tag
AuditCreateDate => when this task has been created 
AuditUpdateDate  => last time this task was updated 
RetryInterval: 0 if no retry/ A number if there is a retry
RetryCooldown: 1/2 hour/min between reties.... if RetryInterval > 1
```


### ECSTaskLog dynamodb table:
```

TaskID => UniqueID
LastRunDateTime => last time this task ran
Status => if the task is Queue/running/failed/Success/QueuedToRetry
```

# project paths
project paths 
```
s3://Bucket/ProjectName/S3Key
```
example
```
s3://data-lake-post-elt-projects/testingECSTask/CodeTest.py
s3://data-lake-post-elt-projects/testingECSTask/CodeTest.zip
```