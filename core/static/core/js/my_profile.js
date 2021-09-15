// console.log("funcionando")
// const sugestions_following = document.getElementById('sugestions_following')
//
// $.ajax({
//     type: 'GET',
//     url: '/my-data/',
//     success: function (response) {
//         console.log(response.sf_data)
//         const sug_following = response.sf_data
//         sug_following.forEach(sf => {
//             sugestions_following.innerHTML += `
//                 <div class="row mb-2 align-items-center">
//                     <div class="col-2">
//                         <img class="img_avatar" src="${sf.image}" alt="${sf.user}">
//                     </div>
//                     <div class="col-3">
//                         <div class="text-muted">${sf.user}</div>
//                     </div>
//                     <div class="col text-right">
//                         <button class="btn btn-success">Seguir</button>
//                     </div>
//                 </div>
//              `
//         })
//     },
//     error: function (error) {
//         console.log(error)
//     }
// })
