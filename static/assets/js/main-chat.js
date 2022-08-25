const userMessageForm = document.getElementById("user-form")
const formSender = document.getElementById("sender").value
const formReciever = document.getElementById("reciever").value
const fullSender = document.getElementById("full-sender").value
const fullReciever = document.getElementById("full-reciever").value
const otherSender = document.getElementById("other-sender").value
const formRoom = document.getElementById("room").value
const formToken = document.getElementById("csrf-token").value
const messagesDiv = document.querySelector(".messages")
ajax = new XMLHttpRequest()

const config = {
    headers: {
        'Content-Type': 'application/json'
    }
}

// Get Messages
setInterval(() => {
    // Form Data
    const data = new FormData()

    data.append('sender', formSender)
    data.append('reciever', formReciever)
    data.append('room', formRoom)
    data.append('csrfmiddlewaretoken', formToken)

    axios({
        url: '/get-messages',
        method: 'post',
        baseURL: '',
        headers: config.headers,
        data
    }).then(response => {
        // console.log("Get Messages Response Recieved", response.data)
        // Update Div
        messagesDiv.innerHTML = '<div class="messages"></div>'
        const div = document.createElement("div")
        response.data.forEach(message => {
            // console.log("Message For Each", message.value)
            if (formReciever === 'all') {
                if (message.sender === formSender) {
                    div.classList.add('chat-message-right', 'mb-4')
                    div.innerHTML = `
                        <div>
                            <img src="https://bootdey.com/img/Content/avatar/avatar1.png" class="rounded-circle mr-1" alt="${ fullSender }" width="40" height="40">
                        </div>
                        <div class="flex-shrink-1 bg-light rounded py-2 px-3 mr-3">
                            <div class="font-weight-bold mb-1 text-right">${ fullSender }</div>
                            <div class="text-primary mb-1 text-right"><i>You (${ formSender })</i></div>
                            <p id="sender-message" class="text-primary">${ message.value }</p>
                            <div class="text-muted small text-nowrap mt-2">${ message.date }</div>
                        </div>
                    `
                } else {
                    div.classList.add('chat-message-left', 'pb-4')
                    div.innerHTML = `
                        <div>
                            <img src="https://bootdey.com/img/Content/avatar/avatar3.png" class="rounded-circle mr-1" alt="${ message.sender }" width="40" height="40">
                        </div>
                        <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                            <div class="font-weight-bold mb-1">${ message.sender.toUpperCase() }</div>
                            <div class="text-success mb-1"><i>(${ message.sender })</i></div>
                            <p id="reciever-message" class="text-success">${ message.value }</p>
                            <div class="text-muted small text-nowrap mt-2">${ message.date }</div>
                        </div>
                    `
                }
                messagesDiv.appendChild(div)
            } else {
                if (message.sender === formSender && message.reciever === formReciever) {
                    div.classList.add('chat-message-right', 'mb-4')
                    div.innerHTML = `
                        <div>
                            <img src="https://bootdey.com/img/Content/avatar/avatar1.png" class="rounded-circle mr-1" alt="${ fullSender }" width="40" height="40">
                        </div>
                        <div class="flex-shrink-1 bg-light rounded py-2 px-3 mr-3">
                            <div class="font-weight-bold mb-1 text-right">${ fullSender }</div>
                            <div class="text-primary mb-1 text-right"><i>You (${ formSender })</i></div>
                            <p id="sender-message" class="text-primary">${ message.value }</p>
                            <div class="text-muted small text-nowrap mt-2">${ message.date }</div>
                        </div>
                    `
                }

                if (message.sender === formReciever && message.reciever === formSender) {
                    div.classList.add('chat-message-left', 'pb-4')
                    div.innerHTML = `
                        <div>
                            <img src="https://bootdey.com/img/Content/avatar/avatar3.png" class="rounded-circle mr-1" alt="${ fullReciever }" width="40" height="40">
                        </div>
                        <div class="flex-shrink-1 bg-light rounded py-2 px-3 ml-3">
                            <div class="font-weight-bold mb-1">${ fullReciever }</div>
                            <div class="text-success mb-1"><i>(${ formReciever })</i></div>
                            <p id="reciever-message" class="text-success">${ message.value }</p>
                            <div class="text-muted small text-nowrap mt-2">${ message.date }</div>
                        </div>
                    `
                }
                messagesDiv.appendChild(div)
            }
        })
    }).error(error => console.log("Get Messages Error Recieved", error))
}, 3000)

// Submit Chat Form
userMessageForm.addEventListener("submit", (event) => {

    // Prevent Default Submission
    event.preventDefault()

    // Form Data
    const data = new FormData()

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
    data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)

    // form_data = {
    //     message,
    //     room,
    //     sender,
    //     reciever,
    //     csrfmiddlewaretoken
    // }
    // payload = JSON.stringify(form_data)

    // console.log("Ajax Recieved The Data", form_data)
    // console.log("Ajax Recieved The Payload", payload)

    // ajax.open('POST', '/send-message', payload)
    // ajax.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    // ajax.send(
    //     `csrfmiddlewaretoken=${encodeURIComponent(csrfmiddlewaretoken)}`
    // )

    axios({
        url: '/send-message',
        method: 'post',
        baseURL: '',
        headers: config.headers,
        data
    }).then(response => {
        console.log("Send Message Response Recieved", response)
        // Clear Input
        event.target.elements.message.value = ""
        event.target.elements.message.focus()
    }).error(error => console.log("Send Message Error Recieved", error))
})