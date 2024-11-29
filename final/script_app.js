function addDocumentField() {
    const documentSelect = document.getElementById("documentSelect");
    const selectedDocument = documentSelect.options[documentSelect.selectedIndex].value;

    if (!selectedDocument) return; // Exit if no document is selected

    // Create a container for the document fields
    const container = document.createElement("div");
    container.className = "document-field";
    
    // Label and input for the document number
    const label = document.createElement("label");
    label.innerText = `${selectedDocument.replace('_', ' ')} Number:`;
    const input = document.createElement("input");
    input.type = "text";
    input.name = `${selectedDocument}_number`;
    input.placeholder = `Enter ${selectedDocument.replace('_', ' ')} number`;
    input.required = true;

    // File upload input
    const fileLabel = document.createElement("label");
    fileLabel.innerText = `Upload ${selectedDocument} (PDF/JPEG):`;
    const fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.name = `${selectedDocument}_file`;
    fileInput.accept = ".pdf, .jpg, .jpeg";
    fileInput.required = true;

    // Append elements to container
    container.appendChild(label);
    container.appendChild(input);
    container.appendChild(fileLabel);
    container.appendChild(fileInput);

    // Append container to form
    document.getElementById("documentContainer").appendChild(container);

    // Remove selected document from dropdown
    documentSelect.remove(documentSelect.selectedIndex);
}
