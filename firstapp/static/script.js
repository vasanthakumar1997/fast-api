async function registerform(e) {
    console.log("hiii")
    e.preventDefault()
    formdata = new FormData(e.target)
    const data = Object.fromEntries(formdata.entries())
    try{
    const response = await fetch('http://localhost:8000/users/register',{
        'method': 'POST',
        'headers': { "Content-Type": "application/json" },
        'body': JSON.stringify(data),

    })
    const result = await response.json()
    console.log("result", result)
    if (result.success) {
        alert("Registration successfull please login to continue")
    }
    else {
        alert("Registration failed" + result.error)
    }
}
catch (err) {
    alert("Error" + err)
}
    
}

document.getElementById("register-form").addEventListener("submit", registerform)