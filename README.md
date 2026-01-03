##Project Title:
MediMind – An AI-Powered Medication Reminder & Drug Information Assistant

##Problem Statement:
Many patients fail to take medications on time or misunderstand drug instructions due to complex medical terminology and lack of proper guidance. This often leads to poor treatment outcomes and health risks. There is a need for an intelligent system that provides accurate drug information in a simple way and helps patients follow their medication schedules correctly.

##Proposed Solution:
MediMind is an AI-powered medication assistant that uses Retrieval Augmented Generation (RAG) to answer user questions based on official drug label information. The system also generates personalized medication reminder schedules, helping patients understand and follow their prescriptions more effectively.

##Proposed Technologies:
- Python  
- LangChain  
- ChromaDB  
- Large Language Model (OpenAI / Gemini)  
- FastAPI

##Data Source:
This project uses publicly available drug label information from the openFDA Drug Label API.
For the hackathon prototype, a limited subset of drug label records was retrieved and used
to demonstrate the RAG-based medication information system.

Source: https://open.fda.gov/apis/drug/label/

##How the System Works:
1. The user asks a question related to a medicine.
2. The system retrieves relevant drug information from stored documents.
3. The AI model generates a clear and accurate response using RAG.
4. A structured medication reminder plan is generated for the user.

##Key Features:
- Accurate drug information using official sources
- AI-powered question answering
- Personalized medication reminder generation
- Simple and user-friendly responses

##Future Scope:
In the future, this system can be enhanced with mobile notifications, multi-language support, voice assistance, doctor dashboards, and integration with electronic health records.

