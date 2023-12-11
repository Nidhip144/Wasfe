document.getElementById('upload-btn').addEventListener('click', function () {
    document.getElementById('file-input').click();
});

document.getElementById('file-input').addEventListener('change', function (event) {
    const file = event.target.files[0];

    if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();

        reader.onload = function (e) {
            const imageUrl = e.target.result;

            // Display the image
            const imgElement = document.createElement('img');
            imgElement.src = imageUrl;
            imgElement.style.maxWidth = '100%';
            document.getElementById('result-container').innerHTML = '';
            document.getElementById('result-container').appendChild(imgElement);
        };

        reader.readAsDataURL(file);
    } else {
        alert('Please select a valid image file.');
    }
});

// async function prediction(){
//     let response = await fetch("/predict").then((response)=>response.json())
//     // console.log(response['otp'])

//     const para = document.createElement("p")
//     para.id = "result"
//     para.innerHTML = response['predicted_class']

//     // document.getElementById("result-container").innerHTML = `<p id="result" >${response['otp']}</p>`
//     document.getElementById("result-container").appendChild(para)


//     setTimeout(() => {
//         para.style.opacity = '0';
//     }, 20000);
//     errorBox.addEventListener('transitionend', () => errorBox.remove());


// }