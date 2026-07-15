import boto3
import json

from config import AWS_REGION, BEDROCK_MODEL_ID


# Create Bedrock Runtime client
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)


def ask_bedrock(prompt):
    """
    Sends a prompt to Amazon Nova Lite
    and returns only the AI-generated response text.
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
            "maxTokens": 800,
            "temperature": 0.3
        }
    }

    response = bedrock_client.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        body=json.dumps(request_body),
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(
        response["body"].read()
    )

    # Extract only the AI-generated text
    ai_response = response_body["output"]["message"]["content"][0]["text"]

    return ai_response


if __name__ == "__main__":

    prompt = """
You are a Senior AWS Support Engineer.

Analyze this AWS issue:

S3 upload fails with AccessDenied.

Provide the response in this format:

## Summary
Explain the issue.

## Possible Root Causes
List the likely causes.

## Troubleshooting Steps
Provide detailed steps.

## AWS CLI Commands
Provide useful commands.

## Recommended Fix
Explain the resolution.
"""

    answer = ask_bedrock(prompt)

    print(answer)