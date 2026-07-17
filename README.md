# AWS GenAI Support Engineer Copilot

An AI-powered AWS troubleshooting assistant built using **Amazon Bedrock, Amazon Nova Lite, and Retrieval Augmented Generation (RAG)**.

This application helps cloud engineers analyze AWS issues, retrieve relevant AWS documentation, identify probable root causes, generate troubleshooting workflows, and provide AWS CLI remediation steps using Generative AI.

---

# Project Overview

Cloud support engineers spend significant time investigating production incidents, analyzing error messages, and searching through documentation to identify solutions.

The **AWS GenAI Support Engineer Copilot** combines:

- Generative AI using Amazon Bedrock
- Amazon Nova Lite foundation model
- Retrieval Augmented Generation (RAG)
- AWS documentation knowledge retrieval
- Semantic search using vector embeddings

The goal is to accelerate cloud incident resolution and provide accurate, documentation-grounded troubleshooting guidance.

---

# Architecture

```
                    User
                      |
                      |
              Streamlit Application
                      |
                      |
              User AWS Issue
                      |
                      |
              RAG Retrieval Layer
                      |
        --------------------------------
        |                              |
 AWS Documentation              FAISS Vector DB
        |                              |
        |                       Semantic Search
        |
 Official AWS Documentation
        |
        |
 Retrieved Context
                      |
                      |
          Amazon Bedrock Runtime API
                      |
                      |
             Amazon Nova Lite Model
                      |
                      |
       AI Generated Troubleshooting Response
```

---

# Features

## Completed Features

✅ AI-powered AWS incident analysis  
✅ Amazon Bedrock integration  
✅ Amazon Nova Lite foundation model  
✅ Retrieval Augmented Generation (RAG) pipeline  
✅ AWS documentation ingestion pipeline  
✅ Semantic document search  
✅ FAISS vector database integration  
✅ AWS documentation-grounded responses  
✅ Root cause analysis generation  
✅ Troubleshooting workflow generation  
✅ AWS CLI command recommendations  
✅ Interactive Streamlit interface  
✅ AWS service documentation references  

---

# RAG Implementation

The application uses a Retrieval Augmented Generation architecture.

## Document Ingestion Pipeline

Official AWS documentation is collected and processed:

Supported services:

- Amazon S3
- Amazon EC2
- AWS IAM
- AWS Lambda
- Amazon CloudWatch
- Amazon VPC
- AWS KMS
- AWS STS
- Amazon EBS
- Amazon Route 53


Pipeline:

```
AWS Documentation
        |
        |
HTML Extraction
        |
        |
Text Processing
        |
        |
Document Chunking
        |
        |
Embedding Generation
        |
        |
FAISS Vector Database
```


## Retrieval Workflow

When a user submits an AWS issue:

```
User Question

      |

Generate Query Embedding

      |

FAISS Similarity Search

      |

Retrieve Relevant AWS Documentation

      |

Send Context + Question to Amazon Nova Lite

      |

Generate Grounded Troubleshooting Response
```

---

# Technology Stack

## Cloud & AI

- Amazon Bedrock
- Amazon Nova Lite
- AWS Documentation
- AWS CLI


## Programming

- Python


## Frameworks & Libraries

- Streamlit
- boto3
- FAISS
- Sentence Transformers
- LangChain Text Splitters
- BeautifulSoup
- Requests

---

# Project Structure

```
aws-genai-support-copilot/

│
├── app.py                    # Streamlit frontend application
│
├── bedrock.py                # Amazon Bedrock integration and prompt handling
│
├── rag.py                    # Vector search and context retrieval
│
├── vector_store.py           # Embedding generation and FAISS index creation
│
├── config.py                 # AWS configuration management
│
├── scripts/
│   └── ingest_docs.py        # AWS documentation ingestion pipeline
│
├── data/
│   ├── raw_docs/             # Downloaded AWS documentation
│   └── processed_docs/       # Processed text documents
│
├── vector_db/                # FAISS vector index storage
│
├── screenshots/              # Application screenshots
│
├── requirements.txt          # Python dependencies
│
├── README.md                 # Project documentation
│
└── .gitignore
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/swaralichine/aws-genai-support-copilot.git

cd aws-genai-support-copilot
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate:

### macOS/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure AWS Credentials

Configure AWS CLI:

```bash
aws configure
```

Verify:

```bash
aws sts get-caller-identity
```

---

## 5. Configure Environment Variables

Create `.env`

```env
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
```

---

## 6. Download AWS Documentation

Run:

```bash
python scripts/ingest_docs.py
```

This downloads official AWS documentation for supported services.

---

## 7. Build Vector Database

Generate embeddings and create FAISS index:

```bash
python vector_store.py
```

---

## 8. Run Application

Start Streamlit:

```bash
streamlit run app.py
```

Application:

```
http://localhost:8501
```

---

# Example Use Cases

## Amazon S3 Troubleshooting

Input:

```
My S3 upload is failing with AccessDenied error.
How do I troubleshoot?
```


The AI assistant provides:

- IAM permission analysis
- Bucket policy checks
- KMS permission validation
- AWS CLI troubleshooting commands
- Recommended remediation steps

---

## Amazon EC2 Troubleshooting

Input:

```
My EC2 instance is unreachable.
System status check failed.
```


The AI assistant provides:

- Instance health analysis
- Networking troubleshooting
- Security group validation
- Recovery recommendations

---

# Security Considerations

- AWS credentials are stored locally
- `.env` files are excluded from Git tracking
- AWS keys are not committed
- Sensitive files are protected using `.gitignore`

---

# Cost Optimization

This project uses serverless AWS Generative AI services.

Cost optimization:

- No EC2 infrastructure required
- No always-running backend services
- Pay-per-request Bedrock invocation
- Local FAISS vector database

Estimated development/testing cost:

```
< $5
```

---

# Future Enhancements

## Conversation Memory

Add multi-turn troubleshooting conversations.

Planned capabilities:

- Maintain previous user queries
- Enable follow-up troubleshooting questions
- Provide context-aware recommendations


## Confidence Score

Add AI-generated confidence scoring.

Planned capabilities:

- Display confidence percentage
- Explain confidence reasoning
- Improve transparency of AI responses


## AWS Issue Classification

Automatically classify incoming AWS issues.

Planned capabilities:

- Identify AWS service involved
- Categorize issue type
- Assign severity level
- Improve troubleshooting workflow routing


## Additional Enhancements

Future improvements:

- CloudWatch log analysis
- Automated remediation workflows
- AWS Well-Architected Framework integration
- Enterprise knowledge base integration
- Advanced observability metrics

---

# Author

**Swarali Chine**

Senior Technical Support Engineer | AWS | Cloud Computing | Generative AI

---

# Project Highlights

Built using:

- Amazon Bedrock
- Amazon Nova Lite
- Retrieval Augmented Generation
- FAISS Vector Search
- Python
- Streamlit


This project demonstrates a practical Generative AI application for cloud operations, troubleshooting automation, and AWS support engineering workflows.
