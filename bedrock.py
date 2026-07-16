import boto3
import json

from config import AWS_REGION, BEDROCK_MODEL_ID


bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)



def ask_bedrock(question, context):
    """
    Sends user question + retrieved AWS documentation context
    to Amazon Nova Lite through Amazon Bedrock.
    """


    prompt = f"""
You are a Senior AWS Support Engineer.

You troubleshoot AWS cloud issues using the provided AWS documentation context.

Rules:
- Use the documentation context as the primary source.
- Do not hallucinate unsupported information.
- Provide practical troubleshooting steps.
- Include AWS CLI commands when useful.

AWS Documentation Context:

{context}


Customer Issue:

{question}


Generate the response in this format:

## Summary

Briefly explain the issue.


## Root Cause

Explain the most likely causes.


## Troubleshooting Steps

Provide detailed step-by-step troubleshooting.


## AWS CLI Commands

Provide relevant AWS CLI commands.


## Recommended Fix

Provide the recommended resolution.
"""


    request_body = {

        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],

        "inferenceConfig": {

            "maxTokens": 1000,

            "temperature": 0.2

        }

    }



    try:

        response = bedrock_client.invoke_model(

            modelId=BEDROCK_MODEL_ID,

            body=json.dumps(request_body),

            contentType="application/json",

            accept="application/json"

        )


        response_body = json.loads(

            response["body"].read()

        )


        return (
            response_body
            .get("output", {})
            .get("message", {})
            .get("content", [{}])[0]
            .get("text", "No response generated.")
        )


    except Exception as error:

        return f"""
## Error

Unable to generate response from Amazon Bedrock.

Details:

{error}
"""




if __name__ == "__main__":


    test_question = """
My S3 upload is failing with AccessDenied.
"""


    test_context = """
Amazon S3 access is controlled using IAM policies,
bucket policies, and access control mechanisms.
AccessDenied occurs when the requesting identity
does not have sufficient permissions.
"""


    answer = ask_bedrock(

        test_question,

        test_context

    )


    print(answer)