from datetime import datetime

from flask import Response, request, jsonify, Flask
import boto3

app = Flask(__name__)


# http://localhost:5000/metric/getAwsMetrics
@app.route('/metric/getAwsMetrics', methods=['POST'])
def get_aws_metrics():
    payload = request.get_json()
    # client = boto3.client('ec2')
    # response = client.describe_instances(
    #     Filters=[],
    #     InstanceIds=['i-07ecf9941ca09c3ee']
    # )

    client = boto3.client('cloudwatch')

    response = client.get_metric_statistics(
        Namespace='CPUUtilization',
        MetricName='CPUUtilization',
        # Dimensions=[
        #     {
        #         'Name': 'string',
        #         'Value': 'string'
        #     },
        # ],
        StartTime=datetime(2020, 4, 18),
        EndTime=datetime(2020, 4, 20),
        Period=120,
        Statistics=['Average'],
        # ExtendedStatistics=[
        #     'string',
        # ],
        Unit='Percent'
    )

    print(response)

    return response, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
