const chatLog = [{role: "system", content: "You are a helpful therapist versed in techniques for anxiety, depression and other mental health disorders. You are kind and helpful, using supportive language only. You should be soothing and creative. Your purpose is to suggest coping techniques and situational advice."}]
function callAI() {

    const prompt = document.getElementById("sendMessage").value; // grab text from textbox
    console.log(prompt);
    chatLog.push({role: "user", content: prompt}) // add user input

    /*
    const completion = openai.chat.completions.create({
        messages: chatLog,
        model: "gpt-3.5-turbo"
    });

     */

    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/jsonGetInput/"+prompt, false ); // false for synchronous request
    xmlHttp.send( null );

    chatLog.push({role: "assistant", content: xmlHttp.responseText})

    document.getElementById("aiText").innerHTML = xmlHttp.responseText;
    console.log(xmlHttp.responseText)
}