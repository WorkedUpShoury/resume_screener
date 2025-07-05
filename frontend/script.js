async function uploadResume() {
  const file = document.getElementById("resumeFile").files[0];
  if (!file) return alert("Please select a PDF file first.");

  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("/resumes/extract", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("uploadResult").innerText = JSON.stringify(data, null, 2);
}

async function askChatbot() {
  const question = document.getElementById("question").value;
  if (!question.trim()) return alert("Please enter a question.");

  const res = await fetch(`/chatbot/query?question=${encodeURIComponent(question)}`);
  const data = await res.json();
  document.getElementById("chatResult").innerText = JSON.stringify(data, null, 2);
}
