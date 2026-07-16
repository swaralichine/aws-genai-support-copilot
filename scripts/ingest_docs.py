import os
import json
import requests

from bs4 import BeautifulSoup


OUTPUT_DIR = "data/processed_docs"


AWS_DOCS = {

    "Amazon S3":
        "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html",

    "Amazon EC2":
        "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html",

    "AWS IAM":
        "https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html",

    "AWS Lambda":
        "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html",

    "Amazon CloudWatch":
        "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html",

    "Amazon VPC":
        "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",

    "AWS KMS":
        "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html",

    "AWS STS":
        "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html",

    "Amazon EBS":
        "https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html",

    "Amazon Route 53":
        "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html"

}


def extract_text(url):

    response = requests.get(
        url,
        timeout=20
    )

    response.raise_for_status()


    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )


    for tag in soup(
        ["script", "style", "nav", "footer"]
    ):
        tag.decompose()


    text = soup.get_text(
        separator="\n"
    )


    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]


    return "\n".join(lines)



def save_document(service, url, text):

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )


    file_path = os.path.join(
        OUTPUT_DIR,
        f"{service.replace(' ', '_')}.json"
    )


    document = {

        "service": service,

        "url": url,

        "content": text

    }


    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            document,
            file,
            indent=4,
            ensure_ascii=False
        )



def main():

    for service, url in AWS_DOCS.items():

        print(
            f"Downloading {service} documentation..."
        )


        try:

            text = extract_text(
                url
            )


            save_document(
                service,
                url,
                text
            )


            print(
                f"Saved {service}"
            )


        except Exception as error:

            print(
                f"Failed {service}: {error}"
            )



if __name__ == "__main__":

    main()