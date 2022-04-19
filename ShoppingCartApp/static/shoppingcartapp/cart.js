window.onload = function() {

    var updateButtons = document.getElementsByClassName('update-cart')

    for (var i = 0; i < updateButtons.length; i++) {
        updateButtons[i].addEventListener('click', function() {
            var productId = this.dataset.product
            var action = this.dataset.action
            console.log('productId:', productId, 'Action:', action)
            console.log('USER:', user)
            if (user === 'AnonymousUser') {
                console.Log('Not logged in')
            } else {
                updateUserOrder(productId, action)
            }
        })
    }

    function updateUserOrder(productId, action) {
        console.log('User is logged in, sending data')
        var url = '/add-to-cart/'

        fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                mode: 'same-origin',
                body: JSON.stringify({
                    'productId': productId,
                    'action': action,
                })
            })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                location.reload()
            })
    }
}