function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const init = () => {
    const cards = document.querySelectorAll('.card')

    for (const card of cards){

        const likeButton = card.querySelector('.like-button')
        const likeCounter = card.querySelector('.like-counter')
        const questionId = Number(card.dataset.questionId)
        console.log(card.dataset)


        likeButton.addEventListener('click', () => {
            const request = new Request(`${questionId}/like_async`, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                }
            })
            fetch(request)
                .then((response ) => response.json())
                .then((data) => likeCounter.value = data.likes_count)


        })
    }
}
console.log("Hi")
init()