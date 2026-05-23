from flask import Flask, request, jsonify

import os
from sentence_transformers import SentenceTransformer
import chromadb

app = Flask(__name__)

# Load embedding model
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")
# Create ChromaDB client
client = chromadb.Client()

collection = client.get_or_create_collection(name="policies")

# Load documents
policy_folder = "policies"

documents = []
ids = []

for filename in os.listdir(policy_folder):
    filepath = os.path.join(policy_folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

        documents.append(text)
        ids.append(filename)

# Create embeddings
embeddings = model.encode(documents).tolist()

# Add to database
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Policy RAG Chatbot</title>
        <style>
            body{
                margin:0;
                font-family: Arial, sans-serif;
                min-height:100vh;
                background: radial-gradient(circle at top left,#7f7cff,#00d4ff,#06b6a7);
                overflow:hidden;
            }
            .shape{
                position:absolute;
                border-radius:50%;
                filter:blur(2px);
                opacity:.35;
            }
            .s1{width:220px;height:220px;background:white;top:60px;left:80px;}
            .s2{width:300px;height:300px;background:#ffdd57;bottom:40px;right:90px;}
            .container{
                position:relative;
                width:65%;
                margin:70px auto;
                padding:35px;
                border-radius:28px;
                background:rgba(255,255,255,.82);
                box-shadow:0 25px 60px rgba(0,0,0,.25);
                backdrop-filter: blur(12px);
                transform: perspective(900px) rotateX(3deg);
            }
            h1{
                text-align:center;
                font-size:36px;
                color:#222;
            }
            .bot{
                font-size:70px;
                text-align:center;
                animation: float 3s ease-in-out infinite;
            }
            @keyframes float{
                0%,100%{transform:translateY(0);}
                50%{transform:translateY(-12px);}
            }
            .search{
                display:flex;
                gap:10px;
                margin-top:25px;
            }
            input{
                flex:1;
                padding:16px;
                border-radius:14px;
                border:1px solid #ddd;
                font-size:16px;
            }
            button{
                padding:16px 24px;
                border:none;
                border-radius:14px;
                background:linear-gradient(135deg,#2563eb,#06b6d4);
                color:white;
                font-weight:bold;
                cursor:pointer;
                box-shadow:0 8px 18px rgba(37,99,235,.35);
            }
            button:hover{transform:translateY(-2px);}
            .chips button{
                margin:15px 8px 0 0;
                padding:10px 14px;
                font-size:13px;
                background:#eef2ff;
                color:#1e3a8a;
                box-shadow:none;
            }
            .answer-box{
                margin-top:28px;
                padding:24px;
                border-radius:22px;
                background:linear-gradient(135deg,#ffffff,#eef7ff);
                box-shadow: inset 0 0 0 1px rgba(0,0,0,.05);
                min-height:120px;
            }
            .source{
                margin-top:14px;
                padding:10px;
                border-radius:10px;
                background:#e0f2fe;
                color:#075985;
                font-size:14px;
            }
        </style>
    </head>
    <body>
        <div class="shape s1"></div>
        <div class="shape s2"></div>

        <div class="container">
            <div class="bot">🤖</div>
            <h1>Policy RAG Assistant</h1>

            <div class="search">
                <input type="text" id="question" placeholder="Ask about PTO, remote work, security, or expenses...">
                <button onclick="askQuestion()">Ask</button>
            </div>

            <div class="chips">
                <button onclick="setQuestion('How many PTO days do employees receive?')">PTO Policy</button>
                <button onclick="setQuestion('What is the remote work policy?')">Remote Work</button>
                <button onclick="setQuestion('What are the security requirements?')">Security</button>
                <button onclick="setQuestion('How are expenses reimbursed?')">Expenses</button>
            </div>

            <div class="answer-box">
                <h3>Answer</h3>
                <div id="result">Ask a question to see the answer with source citation.</div>
            </div>
        </div>

        <script>
            function setQuestion(q){
                document.getElementById("question").value = q;
            }

            async function askQuestion(){
                const question = document.getElementById("question").value;

                document.getElementById("result").innerHTML = "Thinking...";

                const response = await fetch("/chat", {
                    method:"POST",
                    headers:{"Content-Type":"application/json"},
                    body: JSON.stringify({question:question})
                });

                const data = await response.json();

                document.getElementById("result").innerHTML =
                    "<p>" + data.answer + "</p>" +
                    "<div class='source'><b>Source:</b> " + data.source + "</div>";
            }
        </script>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    question = data.get("question")

    question_embedding = model.encode([question]).tolist()[0]

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    documents = results["documents"][0]
    sources = results["ids"][0]

    answer = ""

    for doc in documents:
        answer += doc + "\\n\\n"

    source = ", ".join(sources)

    return jsonify({
        "answer": answer,
        "source": source
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)