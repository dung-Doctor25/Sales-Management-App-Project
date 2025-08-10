// function selectOrder(orderId) {
//     fetch('/select_order/', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//         'X-CSRFToken': csrftoken,
//       },
//       body: JSON.stringify({
//         'orderId': orderId,
//       })
//     })
//     .then((response) => response.json())
//     .then((data) => {
//       console.log('Selected Order ID:', data.orderId);
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
//   }


var updateBtns = document.getElementsByClassName('update-order')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		
		if (this.dataset.product !== undefined){
			var productId = this.dataset.product
		}else{
			var productId = ''
		}

		if(this.dataset.customer !== undefined){
			var customerId = this.dataset.customer
		}else{
			var customerId = ''
		}

		
		var action = this.dataset.action
		console.log('productId:', productId,'customerId:', customerId, 'action:', action)

        
		updateUserOrder(productId,customerId, action)
		
	})
}

function updateUserOrder(productId,customerId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId,'customerId':customerId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
			console.log('data:', data)
		    location.reload()
		});
}

