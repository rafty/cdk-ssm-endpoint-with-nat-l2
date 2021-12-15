import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_ssm_endpoint_with_nat_l2.cdk_ssm_endpoint_with_nat_l2_stack import CdkSsmEndpointWithNatL2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_ssm_endpoint_with_nat_l2/cdk_ssm_endpoint_with_nat_l2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkSsmEndpointWithNatL2Stack(app, "cdk-ssm-endpoint-with-nat-l2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
