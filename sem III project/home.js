document.getElementById("loan-form").addEventListener("submit", function(e) {
  e.preventDefault(); // Prevent form submission

  const formData = new FormData();
  formData.append("name", document.getElementById("name").value);
  formData.append("dob", document.getElementById("dob").value);
  formData.append("email", document.getElementById("email").value);
  formData.append("phone", document.getElementById("phone").value);
  formData.append("loanAmount", document.getElementById("loanAmount").value);
  formData.append("loanPurpose", document.getElementById("loanPurpose").value);
  formData.append("loanDuration", document.getElementById("loanDuration").value);
  formData.append("document", document.getElementById("document").files[0]);

  fetch("http://localhost:5000/api/submit", {
    method: "POST",
    body: formData,
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("status-message").innerText = "Application submitted successfully!";
  })
  .catch(error => {
    document.getElementById("status-message").innerText = "Error submitting application. Please try again.";
  });
});
