function deleteHistory(HistoryId) {
    fetch('/delete-history', {
        method: 'POST',
        body: JSON.stringify({HistoryId: HistoryId})
    }).then((_res) => {
        window.location.href = "/history";
    })
}
function report(){
    let printContents = document.getElementById('printArea').innerHTML;
    console.log(printContents)
    let originalContents = document.body.innerHTML;

     document.body.innerHTML = printContents;
     document.querySelector('textarea').classList.add('printing')

     window.print();

     document.body.innerHTML = originalContents;
}

function recognize() {
    let recognition = new webkitSpeechRecognition();
    recognition.lang = "en-GB";

    recognition.onresult = function (event) {
      console.log(event);
      document.querySelector("#input_text").value =
        event.results[0][0].transcript;
    };
    recognition.start();
  }