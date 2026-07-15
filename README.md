# ☁️ AWS GenAI Support Engineer Copilot

An AI-powered AWS troubleshooting assistant built using **Amazon Bedrock and Amazon Nova Lite**.

This application helps cloud engineers analyze AWS issues, identify probable root causes, generate troubleshooting workflows, and provide AWS CLI remediation steps using Generative AI.

---

## 🚀 Project Overview

Cloud support engineers spend significant time investigating production incidents, analyzing error messages, and searching documentation to identify solutions.

The **AWS GenAI Support Engineer Copilot** uses Amazon Bedrock to provide an AI-powered assistant that can:

- Analyze AWS cloud errors
- Identify possible root causes
- Generate troubleshooting steps
- Recommend AWS CLI commands
- Suggest remediation actions

The goal is to accelerate cloud incident resolution and improve support engineering workflows.

---

## 🏗️ Architecture

```
User
 |
 |
Streamlit Web Application
 |
 |
Python Application Layer
 |
 |
Amazon Bedrock Runtime API
 |
 |
Amazon Nova Lite Foundation Model
 |
 |
AI Generated Troubleshooting Response
```

---

## ✨ Features

✅ AI-powered AWS incident analysis  
✅ Cloud troubleshooting assistant  
✅ Root cause analysis generation  
✅ AWS CLI command recommendations  
✅ Interactive Streamlit interface  
✅ Amazon Bedrock integration  
✅ Low-cost serverless GenAI architecture  

---

## 🛠️ Technology Stack

### Cloud & AI

- Amazon Bedrock
- Amazon Nova Lite
- AWS CLI

### Programming

- Python

### Frameworks & Libraries

- Streamlit
- boto3
- python-dotenv

---

## 📂 Project Structure

```
aws-genai-support-copilot/

│
├── app.py                  # Streamlit frontend application
├── bedrock.py              # Amazon Bedrock API integration
├── config.py               # AWS configuration management
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore
└── .env                    # Local environment configuration
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/swaralichine/aws-genai-support-copilot.git

cd aws-genai-support-copilot
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate the environment:

### macOS/Linux

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure AWS Credentials

Configure AWS CLI:

```bash
aws configure
```

Verify AWS identity:

```bash
aws sts get-caller-identity
```

---

### 5. Configure Environment Variables

Create a `.env` file:

```env
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
```

---

### 6. Run Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Application will be available at:

```
http://localhost:8501
```

---

## 🧪 Example Use Cases

### Amazon S3 Troubleshooting

Input:

```
AccessDenied error while uploading objects to S3 bucket.
How do I troubleshoot?
```

The AI assistant provides:

- Possible IAM permission issues
- Bucket policy checks
- KMS permission validation
- AWS CLI troubleshooting commands
- Recommended resolution steps

---

### Amazon EC2 Troubleshooting

Input:

```
My EC2 instance is unreachable.
System status check failed.
```

The AI assistant provides:

- Root cause analysis
- Instance health checks
- Network troubleshooting steps
- Recovery recommendations

---

## 🔐 Security Considerations

- AWS credentials are stored locally using environment variables
- `.env` files are excluded from Git tracking
- No credentials or secrets are committed to the repository

---

## 💰 Cost Optimization

This project uses Amazon Bedrock serverless foundation models.

Development cost remains minimal because:

- No EC2 infrastructure required
- No always-running services
- Pay-per-request model invocation
- Serverless architecture

Estimated development/testing cost:

```
< $5
```

---

## 🔮 Future Enhancements

Planned improvements:

- Retrieval Augmented Generation (RAG) using AWS documentation
- Vector database integration
- AWS service classification
- CloudWatch log analysis
- Incident severity prediction
- Automated remediation recommendations
- Enterprise knowledge base integration

---

## 👩‍💻 Author

**Swarali Chine**

Senior Technical Support Engineer | AWS | Cloud Computing | Generative AI

---

## ⭐ Project Highlights

Built using:

- Amazon Bedrock
- Amazon Nova Lite
- Python
- Streamlit

Demonstrates practical application of Generative AI for cloud operations, troubleshooting automation, and support engineering workflows.
