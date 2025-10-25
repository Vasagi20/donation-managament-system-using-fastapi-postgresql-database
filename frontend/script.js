const API_URL = "http://127.0.0.1:8000/api/donations/";

async function loadDonations() {
    const response = await fetch(API_URL);
    const donations = await response.json();

    const table = document.getElementById("donationList");
    table.innerHTML = "";

    donations.forEach(donation => {
        const date = new Date(donation.date).toLocaleString();
        const row = `
            <tr>
                <td>${donation.id}</td>
                <td>${donation.donor_name}</td>
                <td>${donation.donation_type}</td>
                <td>${donation.amount}</td>
                <td>${date}</td>
                <td>${donation.remarks || ""}</td>
                <td><button onclick="deleteDonation(${donation.id})">Delete</button></td>
            </tr>`;
        table.innerHTML += row;
    });
}

async function addDonation() {
    const donor_name = document.getElementById("donor_name").value;
    const donation_type = document.getElementById("donation_type").value;
    const amount = parseFloat(document.getElementById("amount").value);
    const remarks = document.getElementById("remarks").value;

    if (!donor_name || !donation_type || !amount) {
        alert("Please fill all required fields!");
        return;
    }

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ donor_name, donation_type, amount, remarks })
    });

    document.getElementById("donor_name").value = "";
    document.getElementById("donation_type").value = "";
    document.getElementById("amount").value = "";
    document.getElementById("remarks").value = "";

    loadDonations();
}

async function deleteDonation(id) {
    if (!confirm("Are you sure you want to delete this donation?")) return;
    await fetch(`${API_URL}${id}`, { method: "DELETE" });
    loadDonations();
}

window.onload = loadDonations;
