const userMessageForm = document.getElementById("user-form")
const messageText = document.getElementById("message")
ajax = new XMLHttpRequest()

// Submit Chat Form
userMessageForm.addEventListener("submit", (event) => {

    // Prevent Default Submission
    event.preventDefault()

    // Form Data
    let data = new FormData()

    // Get Text Inputs
    const message = event.target['message'].value
    const room = event.target['room'].value
    const sender = event.target['sender'].value
    const reciever = event.target['reciever'].value
    const csrfmiddlewaretoken = event.target['csrfmiddlewaretoken'].value

    // Append Form Data
    data.append('message', message)
    data.append('room', room)
    data.append('sender', sender)
    data.append('reciever', reciever)
    data.append('csrfmiddlewaretoken', message)

    form_data = {
        message,
        room,
        sender,
        reciever,
        csrfmiddlewaretoken
    }
    payload = JSON.stringify(form_data)

    console.log("Ajax Recieved The Data", form_data)
    console.log("Ajax Recieved The Payload", payload)

    //    ajax.setRequestHeader('Content-Type', 'application/json')
    //    ajax.send(JSON.stringify(data)

    ajax.open('POST', '/send-message', payload)
    ajax.setRequestHeader('Content-Type', 'application/json')
    ajax.send(data)

    // Clear Input
    event.target.elements.message.value = ""
    event.target.elements.message.focus()
})