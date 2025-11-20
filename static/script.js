async function generateText() {
    const prompt = document.getElementById("prompt").value;
    const outputDiv = document.getElementById("output");

    if (!prompt.trim()) {
        outputDiv.innerHTML = "<p style='color:red;'>Please enter a prompt.</p>";
        return;
    }

    outputDiv.innerHTML = "<p>Generating...</p>";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();

        if (data.error) {
            outputDiv.innerHTML = `<p style='color:red;'>${data.error}</p>`;
        } else {
            outputDiv.innerHTML = `<p>${data.result}</p>`;
        }
    } catch (err) {
        outputDiv.innerHTML = "<p style='color:red;'>Something went wrong.</p>";
    }
}

