import boto3
import csv
from boto3.dynamodb.conditions import Key

class AWS_NoSQL():
    def __init__(self) -> None:
        self.s3 = boto3.resource('s3',aws_access_key_id='',
        aws_secret_access_key='')

    def create_s3_Bucket(self):
        self.s3.create_bucket(Bucket = 'examplebucket1-14848',CreateBucketConfiguration={'LocationConstraint':'us-west-2'})

    def create_DynamoDB_table(self):
        dynamodb = boto3.resource('dynamodb',region_name='us-west-2',aws_access_key_id='',
        aws_secret_access_key='')
        
        table = dynamodb.create_table(
            TableName='DataTable',
            KeySchema=[
                {'AttributeName': 'PartitionKey', 'KeyType':'HASH'},
                {'AttributeName': 'RowKey', 'KeyType':'RANGE'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'PartitionKey', 'AttributeType':'S'},
                {'AttributeName': 'RowKey', 'AttributeType':'S'}
            ],
            ProvisionedThroughput={
                # ReadCapacityUnits set to 10 strongly consistent reads per second
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10  # WriteCapacityUnits set to 10 writes per second
            }     
        )
        
        table.meta.client.get_waiter('table_exists').wait(TableName='DataTable')
        print("Table status:", table.table_status)

    def upload_CSV_data(self):
        dynamodb = boto3.resource('dynamodb',region_name='us-west-2',aws_access_key_id='',
        aws_secret_access_key='')
        table = dynamodb.Table('DataTable')
        urlbase = 'https://s3-us-west-2.amazonaws.com/examplebucket1-14848/'
        with open('experiments.csv','r') as csvfile:
            csvf = csv.reader(csvfile,delimiter=',',quotechar='|')
            next(csvf)
            for item in csvf:
                body = open(item[4],'rb')
                self.s3.Object('examplebucket1-14848',item[4]).put(Body=body)
                md = self.s3.Object('examplebucket1-14848',item[4]).Acl().put(ACL='public-read')
                url = urlbase+item[4]
                metadata_item={'PartitionKey':item[0],'RowKey':item[1],
                                'description':item[4],'date':item[2],'url':url}
                table.put_item(Item=metadata_item)

    def query(self):
        dynamodb = boto3.resource('dynamodb',region_name='us-west-2',aws_access_key_id='',
        aws_secret_access_key='')
        table = dynamodb.Table('DataTable')
        for i in range(3):
            resp = table.query(KeyConditionExpression=Key('PartitionKey').eq(str(i+1)))
            print(resp)
            # if 'Items' in resp:
            #     print(resp['Items'][0])

mNoSQL = AWS_NoSQL()
mNoSQL.create_DynamoDB_table()
mNoSQL.upload_CSV_data()
mNoSQL.query()
